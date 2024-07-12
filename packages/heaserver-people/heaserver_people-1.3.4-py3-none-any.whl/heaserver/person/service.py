"""
The HEA Person Microservice is a wrapper around a Keycloak server for HEA to access user information. It accesses
Keycloak using an admin account. The default account is 'admin' with password of 'admin'. To configure this (and you
must do this to be secure!), add a Keycloak section to the service's configuration file with the following properties:
    Realm = the Keyclock realm from which to request user information.
    VerifySSL = whether to verify the Keycloak server's SSL certificate (defaults to True).
    Host = The Keycloak host (defaults to https://localhost:8444).
    Username = the admin account username (defaults to admin).
    Password = the admin account password.
    PasswordFile = the path to the filename with the password (overrides use of the PASSWORD property).

This microservice tries getting the password from the following places, in order:
    1) the KEYCLOAK_QUERY_USERS_PASSWORD property in the HEA Server Registry Microservice.
    2) the above config file.

If not present in any of those sources, a password of admin will be used.
"""
import logging

from heaserver.service import response
from heaserver.service.runner import init_cmd_line, routes, start, web
from heaserver.service.wstl import action, builder_factory
from heaserver.service import appproperty
from heaserver.service.heaobjectsupport import new_heaobject_from_type
from heaserver.service.oidcclaimhdrs import SUB
from heaobject.error import DeserializeException
from heaobject.person import Group
from .keycloakmongo import KeycloakMongoManager
from heaobject.user import NONE_USER
from aiohttp import ClientResponseError
from base64 import urlsafe_b64decode
from binascii import Error as B64DecodeError

MONGODB_PERSON_COLLECTION = 'people'


@routes.get('/ping')
async def ping(request: web.Request) -> web.Response:
    """
    For testing whether the service is up.

    :param request: the HTTP request.
    :return: Always returns status code 200.
    """
    return response.status_ok(None)


@routes.get('/people/me')
@action(name='heaserver-people-person-get-properties', rel='hea-properties')
@action(name='heaserver-people-person-get-self', rel='self', path='people/{id}')
@action(name='heaserver-people-person-get-settings', rel='hea-system-menu-item hea-user-menu-item application/x.settingsobject application/x.collection', path='collections/heaobject.settings.SettingsObject')
#@action(name='heaserver-people-person-get-organization-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.organization.Organization')
#@action(name='heaserver-people-person-get-volumes-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.volume.Volume')
@action(name='heaserver-people-person-get-credential-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.keychain.Credentials')
@action(name='heaserver-people-person-get-organizations', rel='application/x.organization', path='organizations/')
@action(name='heaserver-people-person-get-volumes', rel='application/x.volume', path='volumes/')
@action(name='heaserver-people-person-get-desktop-object-actions', rel='application/x.desktopobjectaction', path='desktopobjectactions/')
async def get_me(request: web.Request) -> web.Response:
    """
    Gets the currently logged in person.

    :param request: the HTTP request.
    :return: the requested person or Not Found.
    ---
    summary: A specific person.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    try:
        person = await request.app[appproperty.HEA_DB].get_user(request, request.headers.get(SUB, NONE_USER))
    except ClientResponseError as e:
        if e.status == 404:
            person = None
        else:
            return response.status_generic(e.status, body=e.message)
    if person is not None:
        return await response.get(request, person.to_dict(), permissions=person.get_permissions(sub))
    else:
        return await response.get(request, None)


@routes.get('/people/{id}')
@action(name='heaserver-people-person-get-properties', rel='hea-properties')
@action(name='heaserver-people-person-get-self', rel='self', path='people/{id}')
@action(name='heaserver-people-person-get-settings', rel='hea-system-menu-item hea-user-menu-item application/x.settingsobject application/x.collection', path='collections/heaobject.settings.SettingsObject')
#@action(name='heaserver-people-person-get-organization-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.organization.Organization')
#@action(name='heaserver-people-person-get-volumes-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.volume.Volume')
@action(name='heaserver-people-person-get-credential-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.keychain.Credentials')
@action(name='heaserver-people-person-get-organizations', rel='application/x.organization', path='organizations/')
@action(name='heaserver-people-person-get-volumes', rel='application/x.volume', path='volumes/')
@action(name='heaserver-people-person-get-desktop-object-actions', rel='application/x.desktopobjectaction', path='desktopobjectactions/')
async def get_person(request: web.Request) -> web.Response:
    """
    Gets the person with the specified id.
    :param request: the HTTP request.
    :return: the requested person or Not Found.
    ---
    summary: A specific person.
    tags:
        - heaserver-people
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    try:
        person = await request.app[appproperty.HEA_DB].get_user(request, request.match_info['id'])
    except ClientResponseError as e:
        if e.status == 404:
            person = None
        else:
            return response.status_generic(e.status, body=e.message)
    if person is not None:
        return await response.get(request, person.to_dict(), permissions=person.get_permissions(sub))
    else:
        return await response.get(request, None)


@routes.get('/people/byname/{name}')
@action(name='heaserver-people-person-get-self', rel='self', path='people/{id}')
async def get_person_by_name(request: web.Request) -> web.Response:
    """
    Gets the person with the specified id.
    :param request: the HTTP request.
    :return: the requested person or Not Found.
    ---
    summary: A specific person, by name.
    tags:
        - heaserver-people
    parameters:
        - $ref: '#/components/parameters/name'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    try:
        persons = await request.app[appproperty.HEA_DB].get_users(request, params={'name': request.match_info['name']})
        if persons:
            return await response.get(request, persons[0].to_dict(), permissions=persons[0].get_permissions(sub))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        return response.status_generic(e.status, body=e.message)


@routes.get('/people')
@routes.get('/people/')
@action(name='heaserver-people-person-get-properties', rel='hea-properties')
@action(name='heaserver-people-person-get-self', rel='self', path='people/{id}')
@action(name='heaserver-people-person-get-settings', rel='hea-system-menu-item hea-user-menu-item application/x.settingsobject application/x.collection', path='collections/heaobject.settings.SettingsObject')
#@action(name='heaserver-people-person-get-organization-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.organization.Organization')
#@action(name='heaserver-people-person-get-volumes-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.volume.Volume')
@action(name='heaserver-people-person-get-credential-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.keychain.Credentials')
@action(name='heaserver-people-person-get-organizations', rel='application/x.organization', path='organizations/')
@action(name='heaserver-people-person-get-volumes', rel='application/x.volume', path='volumes/')
@action(name='heaserver-people-person-get-desktop-object-actions', rel='application/x.desktopobjectaction', path='desktopobjectactions/')
async def get_all_persons(request: web.Request) -> web.Response:
    """
    Gets all persons.
    :param request: the HTTP request.
    :return: all persons.
    ---
    summary: All persons.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    try:
        persons = await request.app[appproperty.HEA_DB].get_users(request)
        return await response.get_all(request, [person.to_dict() for person in persons],
                                      permissions=[person.get_permissions(sub) for person in persons])
    except ClientResponseError as e:
        return response.status_generic(e.status, body=e.message)

@routes.get('/roles')
@routes.get('/roles/')
@action(name='heaserver-people-role-get-properties', rel='hea-properties')
@action(name='heaserver-people-role-get-self', rel='self', path='roles/{id}')
async def get_all_roles(request: web.Request) -> web.Response:
    """
    Gets all roles that are known to Keycloak.
    :param request: the HTTP request.
    :return: all roles.
    ---
    summary: All roles.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    try:
        roles = await request.app[appproperty.HEA_DB].get_all_roles(request)
        return await response.get_all(request, [role.to_dict() for role in roles],
                                      permissions=[role.get_permissions(sub) for role in roles])
    except ClientResponseError as e:
        if e.status == 404:
            return await response.get_all(request, [])
        else:
            return response.status_generic(e.status, body=e.message)


@routes.get('/roles/{id}')
@action(name='heaserver-people-role-get-properties', rel='hea-properties')
@action(name='heaserver-people-role-get-self', rel='self', path='roles/{id}')
async def get_role(request: web.Request) -> web.Response:
    """
    Gets the requested role.

    :param request: the HTTP request. Requires an Authorization header with a valid Bearer token, in
    addition to the usual OIDC_CLAIM_sub header.
    :return: all roles.
    ---
    summary: All roles.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    id_ = request.match_info['id']
    try:
        roles = await request.app[appproperty.HEA_DB].get_all_roles(request)
        role = next((role for role in roles if role.id == id_), None)
        if role is not None:
            return await response.get(request, role.to_dict(), permissions=role.get_permissions(sub))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)


@routes.get('/roles/byname/{name}')
async def get_role_by_name(request: web.Request) -> web.Response:
    """
    Gets the requested role. Requires an Authorization header with a valid Bearer token, in
    addition to the usual OIDC_CLAIM_sub header.

    :param request: the HTTP request.
    :return: all roles.
    ---
    summary: All roles.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    name = request.match_info['name']
    try:
        roles = await request.app[appproperty.HEA_DB].get_all_roles(request)
        role = next((role for role in roles if role.name == name), None)
        if role is not None:
            return await response.get(request, role.to_dict(), permissions=role.get_permissions(sub))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)

@routes.get('/groups')
@routes.get('/groups/')
@action(name='heaserver-people-group-get-properties', rel='hea-properties')
@action(name='heaserver-people-group-get-self', rel='self', path='groups/{id}')
async def get_all_groups(request: web.Request) -> web.Response:
    """
    Gets all groups that are known to Keycloak.
    :param request: the HTTP request.
    :return: all groups.
    ---
    summary: All groups.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    try:
        groups = await request.app[appproperty.HEA_DB].get_all_groups(request)
        logger.debug('groups: %s', groups)
        return await response.get_all(request, [group.to_dict() for group in groups],
                                      permissions=[group.get_permissions(sub) for group in groups])
    except ClientResponseError as e:
        if e.status == 404:
            return await response.get_all(request, [])
        else:
            return response.status_generic(e.status, body=e.message)


@routes.get('/groups/{id}')
@action(name='heaserver-people-group-get-properties', rel='hea-properties')
@action(name='heaserver-people-group-get-self', rel='self', path='groups/{id}')
async def get_group(request: web.Request) -> web.Response:
    """
    Gets the requested group. Requires an Authorization header with a valid Bearer token, in
    addition to the usual OIDC_CLAIM_sub header.

    :param request: the HTTP request.
    :return: all groups.
    ---
    summary: All groups.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    id_ = request.match_info['id']
    try:
        groups = await request.app[appproperty.HEA_DB].get_all_groups(request)
        group = next((group for group in groups if group.id == id_), None)
        if group is not None:
            return await response.get(request, group.to_dict(), permissions=group.get_permissions(sub))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)

@routes.get('/groups/byname/{name}')
async def get_group_by_name(request: web.Request) -> web.Response:
    """
    Gets the requested group. Requires an Authorization header with a valid Bearer token, in
    addition to the usual OIDC_CLAIM_sub header.

    :param request: the HTTP request.
    :return: all groups.
    ---
    summary: All groups.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    name = request.match_info['name']
    try:
        groups = await request.app[appproperty.HEA_DB].get_all_groups(request)
        group = next((group for group in groups if group.name == name), None)
        if group is not None:
            return await response.get(request, group.to_dict(), permissions=group.get_permissions(sub))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)

@routes.post('/people/{person_id}/groups')
@routes.post('/people/{person_id}/groups/')
async def post_user_group(request: web.Request) -> web.Response:
    logger = logging.getLogger(__name__)
    person_id = request.match_info['person_id']
    try:
        obj = await new_heaobject_from_type(request, Group)
    except DeserializeException as e:
        return response.status_bad_request(str(e))
    if person_id == 'me':
        coro = request.app[appproperty.HEA_DB].add_current_user_to_group(request, obj.id)
    else:
        coro = request.app[appproperty.HEA_DB].add_user_to_group(request, person_id, obj.id)
    if result := await coro:
        return await response.post(request, obj.id if result else None, 'groups')
    else:
        return response.status_not_found()

@routes.get('/people/{person_id}/groups')
@routes.get('/people/{person_id}/groups/')
async def get_user_group(request: web.Request) -> web.Response:
    """
    Gets all groups for the current user.
    :param request: the HTTP request.
    :return: all groups.
    ---
    summary: All groups.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    person_id = request.match_info['person_id']
    sub = request.headers.get(SUB, NONE_USER)
    try:
        if person_id == 'me':
            groups = await request.app[appproperty.HEA_DB].get_current_user_groups(request)
        else:
            groups = await request.app[appproperty.HEA_DB].get_user_groups(request, person_id)
        return await response.get_all(request, [group.to_dict() for group in groups],
                                      permissions=[group.get_permissions(sub) for group in groups])
    except ClientResponseError as e:
        if e.status == 404:
            return await response.get_all(request, [])
        else:
            return response.status_generic(e.status, body=e.message)

@routes.delete('/people/{person_id}/groups/{id}')
async def delete_user_group(request: web.Request) -> web.Response:
    id_ = request.match_info['id']
    person_id = request.match_info['person_id']
    if person_id == 'me':
        result = await request.app[appproperty.HEA_DB].remove_current_user_group(request, id_)
    else:
        result = await request.app[appproperty.HEA_DB].remove_user_group(request, person_id, id_)
    return await response.delete(result)

@routes.delete('/people/{person_id}/groups/bygroup/{group}')
async def delete_group_by_group(request: web.Request) -> web.Response:
    group = request.match_info['group']
    person_id = request.match_info['person_id']
    if person_id == 'me':
        result = await request.app[appproperty.HEA_DB].remove_current_user_group_by_group(request, group)
    else:
        result = await request.app[appproperty.HEA_DB].remove_user_group_by_group(request, person_id, group)
    return await response.delete(result)

@routes.get('/people/internal/token')
async def get_token(request: web.Request) -> web.Response:
    logger = logging.getLogger(__name__)
    try:
        if logger.getEffectiveLevel() == logging.DEBUG:
            logger.debug('headers %s', request.headers)
        token = await request.app[appproperty.HEA_DB].get_keycloak_alt_access_token(request)
    except ClientResponseError as e:
        logger.exception('Got client response error')
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)
    except B64DecodeError as e:
        return response.status_not_found()
    return await response.get(request, token.to_dict())

def main() -> None:
    config = init_cmd_line(description='Read-only wrapper around Keycloak for accessing user information.',
                           default_port=8080)
    start(package_name='heaserver-people', db=KeycloakMongoManager, config=config, wstl_builder_factory=builder_factory(__package__))


