# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2024 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Auth Handler

See also :doc:`rattail-manual:base/handlers/other/auth`.
"""

import secrets
import warnings

from sqlalchemy import orm
import sqlalchemy_continuum as continuum

from rattail.app import GenericHandler, MergeMixin


class AuthHandler(GenericHandler, MergeMixin):
    """
    Base class and default implementation for the so-called "auth"
    handler, by which we mean "authentication and authorization".

    In practice this is also responsible for creating new users, and
    various things pertaining to roles, etc.
    """

    def authenticate_user(self, session, username, password):
        """
        Authenticate the given user credentials, and if successful,
        return the user object.

        Default logic will (try to) locate a user record with matching
        username, then confirm the supplied password is also a match.

        You may of course define a custom handler and then could
        authenticate against anything you like, e.g. the POS system or
        LDAP etc.  The only trick is that this must return a Rattail
        user, not some other kind.  So you may have to devisde a way
        to auto-create the Rattail user as needed, when authentication
        for the external system succeeds.

        Generally speaking the credentials passed in will have come
        directly from a user login attempt in the web app etc.  Again
        the default logic assumes a "username" but in practice it may
        be an email address etc. - whatever the user types.

        :param session: Current session for Rattail DB.

        :param username: Username as string.

        :param password: Password as string.

        :returns: On success, a :class:`~rattail.db.model.users.User`
           instance; else ``None``.
        """
        from rattail.db.auth import authenticate_user

        return authenticate_user(session, username, password)

    def authenticate_user_token(self, session, token):
        """
        Authenticate the given user API token string, and if valid,
        return the corresponding User object.
        """
        model = self.model

        try:
            token = session.query(model.UserAPIToken)\
                           .filter(model.UserAPIToken.token_string == token)\
                           .one()
        except orm.exc.NoResultFound:
            pass
        else:
            user = token.user
            if user.active:
                return user

    def get_user(self, obj, **kwargs):
        """
        Return the User associated with the given object, if any.
        """
        model = self.model

        if isinstance(obj, model.User):
            return obj

        else:
            person = self.app.get_person(obj)
            if person and person.users:
                # TODO: what if multiple users / ambiguous?
                return person.users[0]

    def has_permission(self, session, principal, permission,
                       include_guest=True,
                       include_authenticated=True):
        """
        Check if the given user or role has been granted the given
        permission.

        :param session: Current session for Rattail DB.

        :param principal: Either a
           :class:`~rattail.db.model.users.User` or
           :class:`~rattail.db.model.users.Role` instance.  It is also
           expected that this may sometimes be ``None``, in which case
           the "Guest" role will typically be assumed.

        :param permission: Name of the permission for which to check.

        :param include_guest: Whether or not the "Guest" role should
           be included when checking permissions.  If ``False``, then
           Guest's permissions will *not* be consulted.

        :param include_authenticated: Whether or not the
           "Authenticated" role should be included when checking
           permissions.

        :returns: Boolean indicating if the permission has been
           granted.
        """
        perms = self.get_permissions(session, principal,
                                     include_guest=include_guest,
                                     include_authenticated=include_authenticated)
        return permission in perms

    def get_permissions(self, session, principal,
                          include_guest=True,
                          include_authenticated=True):
        """
        Return a set of permission names, which represents all
        permissions effectively granted to the given user or role.

        :param session: Current session for Rattail DB.

        :param principal: Either a
           :class:`~rattail.db.model.users.User` or
           :class:`~rattail.db.model.users.Role` instance.  It is also
           expected that this may sometimes be ``None``, in which case
           the "Guest" role will typically be assumed.

        :param include_guest: Whether or not the "Guest" role should
           be included when checking permissions.  If ``False``, then
           Guest's permissions will *not* be consulted.

        :param include_authenticated: Whether or not the
           "Authenticated" role should be included when checking
           permissions.

        :returns: Set of permission names.
        """
        from rattail.db.auth import guest_role, authenticated_role

        # we will use any `roles` attribute which may be present.  in practice we
        # would be assuming a User in this case
        if hasattr(principal, 'roles'):

            roles = []
            for role in principal.roles:
                include = False
                if role.node_type:
                    if role.node_type == self.config.node_type():
                        include = True
                else:
                    include = True
                if include:
                    roles.append(role)

            # here our User assumption gets a little more explicit
            if include_authenticated:
                roles.append(authenticated_role(session))

        # otherwise a non-null principal is assumed to be a Role
        elif principal is not None:
            roles = [principal]

        # fallback assumption is "no roles"
        else:
            roles = []

        # maybe include guest roles
        if include_guest:
            roles.append(guest_role(session))

        # build the permissions cache
        cache = set()
        for role in roles:
            cache.update(role.permissions)

        return cache

    def cache_permissions(self, *args, **kwargs): # pragma: no cover
        warnings.warn("method is deprecated, please use "
                      "get_permissions() method instead",
                      DeprecationWarning, stacklevel=2)
        return self.get_permissions(*args, **kwargs)

    def grant_permission(self, role, permission):
        """
        Grant a permission to the role.  If the role already has the
        permission, nothing is done.

        :param role: A :class:`~rattail.db.model.users.Role` instance.

        :param permission: Name of the permission as string.
        """
        if permission not in role.permissions:
            role.permissions.append(permission)

    def revoke_permission(self, role, permission):
        """
        Revoke a permission from the role.  If the role does not have
        the permission, nothing is done.

        :param role: A :class:`~rattail.db.model.users.Role` instance.

        :param permission: Name of the permission as string.
        """
        if permission in role.permissions:
            role.permissions.remove(permission)

    def generate_preferred_username(self, session, **kwargs):
        """
        Generate a "preferred" username using data from ``kwargs`` as
        hints.

        Note that ``kwargs`` should be of the same sort that might be
        passed to the constructor for a new
        :class:`~rattail.db.model.users.User` instance.

        So far there is only one "hint" which is honored by the
        default logic; however the intention is to leave this flexible
        as other kinds of hints may be useful in the future.

        This method does not confirm if the username it generates is
        actually "available" for a new user.  If you need confirmation
        then use :meth:`generate_unique_username()` instead.

        :param session: Current session for Rattail DB.

        :param person: Reference to a
           :class:`~rattail.db.model.people.Person` instance.  If you
           specify this hint, then default logic will generate a
           username using first and last names, like ``'first.last'``.
           (You can override with a custom handler if needed.)

        :returns: Generated username as string.
        """
        person = kwargs.get('person')
        if person:
            first = (person.first_name or '').strip().lower()
            last = (person.last_name or '').strip().lower()
            return '{}.{}'.format(first, last)

        return 'newuser'

    def generate_username(self, *args, **kwargs): # pragma: no cover
        warnings.warn("method is deprecated, please use "
                      "generate_preferred_username() method instead",
                      DeprecationWarning, stacklevel=2)
        return self.generate_preferred_username(*args, **kwargs)

    def generate_unique_username(self, session, **kwargs):
        """
        Generate a *unique* username using data from ``kwargs`` as
        hints.

        Note that ``kwargs`` should be of the same sort that might be
        passed to the constructor for a new
        :class:`~rattail.db.model.users.User` instance.

        This method is a convenience which does two things:

        First it calls :meth:`generate_preferred_username()` to obtain
        the "preferred" username.  (It passes ``kwargs`` along when it
        makes the call.  See :meth:`generate_preferred_username()` for
        more info.)

        Then it checks to see if the resulting username is already
        taken.  If it is, then a "counter" is appended to the
        username, and incremented until a username can be found which
        is *not* yet taken.

        It returns the first "available" (hence unique) username which
        is found.  Note that it is considered unique and therefore
        available *at the time*; however this method does not
        "reserve" the username in any way.  It is assumed that you
        would create the user yourself once you have the username.

        :param session: Current session for Rattail DB.

        :returns: Username as string.
        """
        model = self.model

        original_username = self.generate_preferred_username(session, **kwargs)
        username = original_username

        # only if given a session, can we check for unique username
        if session:
            counter = 1
            while True:
                users = session.query(model.User)\
                               .filter(model.User.username == username)\
                               .count()
                if not users:
                    break
                username = "{}{:02d}".format(original_username, counter)
                counter += 1

        return username

    def make_user(self, session=None, **kwargs):
        """
        Make and return a new user.

        This is mostly just a simple wrapper around the normal
        :class:`~rattail.db.model.users.User` constructor.  All
        ``kwargs`` for instance are passed on to the constructor.

        Default logic here only adds one other convenience:

        If there is no ``username`` specified in the ``kwargs`` then
        it will call :meth:`generate_unique_username()` to
        automatically provide a username.  Note that all ``kwargs``
        are passed along in that call.

        :param session: Current session for the Rattail DB.  This is
           "sort of" optional, but please do provide it, as it may
           become requied in the future.

        :returns: A new :class:`~rattail.db.model.users.User` instance.
        """
        model = self.model

        if 'username' not in kwargs:
            kwargs['username'] = self.generate_unique_username(session, **kwargs)

        user = model.User(**kwargs)
        if session:
            session.add(user)
        return user

    def get_role(self, session, key, **kwargs):
        """
        Locate and return a Role for the given key, if possible.

        :param session: App database session.

        :param key: Value to use when searching for the role.  Can
           be a UUID or name of a role.

        :returns: The :class:`~rattail.db.model.Role` instance if
           found; or ``None``.
        """
        model = self.model

        # Role.uuid match?
        role = session.get(model.Role, key)
        if role:
            return role

        # Role.name match?
        try:
            return session.query(model.Role).filter_by(name=key).one()
        except orm.exc.NoResultFound:
            pass

        # try settings, if value then recurse.
        key = self.app.get_setting(session, f'rattail.role.{key}')
        if key:
            return self.get_role(session, key)

    def get_email_address(self, user, **kwargs):
        """
        Get the "best" email address we have on file for the given user.
        """
        warnings.warn("auth.get_email_address(user) is deprecated; please "
                      "use app.get_contact_email_address(user) instead",
                      DeprecationWarning, stacklevel=2)
        return self.app.get_contact_email_address(user)

    def get_short_display_name(self, user, **kwargs):
        """
        Returns "short display name" for the user.  This is for
        convenience of mobile view, at least...
        """
        # TODO: this should reference employee.short_name
        employee = self.app.get_employee(user)
        if employee and employee.display_name:
            return employee.display_name

        person = self.app.get_person(user)
        if person:
            if person.first_name and person.last_name:
                return "{} {}.".format(person.first_name, person.last_name[0])
            if person.first_name:
                return person.first_name

        return user.username

    def generate_raw_api_token(self):
        """
        Generate a new *raw* API token string.
        """
        return secrets.token_urlsafe()

    def add_api_token(self, user, description, **kwargs):
        """
        Add a new API token for the user.
        """
        model = self.model
        session = self.app.get_session(user)

        # generate raw API token, in the form required for use within
        # the API client
        token_string = self.generate_raw_api_token()

        # create DB record for the token
        token = model.UserAPIToken(
            user=user,
            description=description,
            token_string=token_string)
        session.add(token)

        return token

    def delete_api_token(self, token, **kwargs):
        """
        Delete a new API token for the user.
        """
        session = self.app.get_session(token)
        session.delete(token)

    def get_merge_preview_fields(self, **kwargs):
        """
        Returns a sequence of fields which will be used during a merge
        preview.
        """
        F = self.make_merge_field
        return [
            F('uuid'),
            F('username'),
            F('person_uuid', coalesce=True),
            F('person_name', coalesce=True),
            F('role_count'),    # coalesced manually
            F('active', coalesce=True),
            F('sent_message_count', additive=True),
            F('received_message_count', additive=True),
        ]

    def get_merge_preview_data(self, user, **kwargs):
        return {
            'uuid': user.uuid,
            'username': user.username,
            'person_uuid': user.person_uuid,
            'person_name': user.person.display_name if user.person else None,
            '_roles': user.roles, # needed for final role count
            'role_count': len(user.roles),
            'active': user.active,
            'sent_message_count': len(user.sent_messages),
            'received_message_count': len(user._messages),
        }

    def get_merge_resulting_data(self, removing, keeping, **kwargs):
        result = super().get_merge_resulting_data(removing, keeping, **kwargs)

        # nb. must "manually" coalesce the role count
        result['role_count'] = len(set(removing['_roles'] + keeping['_roles']))

        return result

    def why_not_merge(self, removing, keeping, **kwargs):

        if removing.sent_messages:
            return "Cannot (yet) remove a user who has sent messages"

        if removing._messages:
            return "Cannot (yet) remove a user who has received messages"

        if removing._roles:
            return "Cannot (yet) remove a user who is assigned to roles"

    def merge_update_keeping_object(self, removing, keeping):
        super().merge_update_keeping_object(removing, keeping)
        session = self.app.get_session(keeping)
        model = self.model

        # update any notes authored by old user, to reflect new user
        notes = session.query(model.Note)\
                       .filter(model.Note.created_by == removing)\
                       .all()
        for note in notes:
            note.created_by = keeping

    def delete_user(self, user, **kwargs):
        """
        Delete the given user account.  Use with caution!  As this
        generally cannot be undone.

        Default behavior here is of course to delete the account, but
        it also must try to "remove" the user association from various
        places, in particular the continuum transactions table.
        Please note that this will leave certain record versions as
        appearing to be "without an author".

        :param user: Reference to a
           :class:`~rattail.db.model.users.User` to be deleted.

        :returns: Boolean indicating success.

           Note that the utility of this method even having a return
           value is deemed questionable, so it's possible in the
           future this may just return ``None`` on success, and raise
           an error to indicate failure.
        """
        session = self.app.get_session(user)

        # disassociate user from transactions
        if self.config.versioning_has_been_enabled:
            self.remove_user_from_continuum_transactions(user)

        # finally, delete the user outright
        session.delete(user)
        return True

    def remove_user_from_continuum_transactions(self, user):
        """
        Remove the given user from all Continuum transactions,
        i.e. all data versioning tables.

        You probably will not need to invoke this directly; it is
        invoked as needed from within :meth:`delete_user()`.

        :param user: A :class:`~rattail.db.model.users.User` instance
           which should be purged from the versioning tables.
        """
        session = self.app.get_session(user)
        model = self.model

        # remove the user from any continuum transactions
        # nb. we can use "any" model class here, to obtain Transaction
        Transaction = continuum.transaction_class(model.User)
        transactions = session.query(Transaction)\
                              .filter(Transaction.user_id == user.uuid)\
                              .all()
        for txn in transactions:
            txn.user_id = None
