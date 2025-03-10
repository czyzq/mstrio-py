from mstrio.utils.error_handlers import ErrorHandler
from mstrio.utils.helper import response_handler


@ErrorHandler(
    err_msg='Selected project {name} does not exist or is not loaded.'
            ' Please load the project or select a valid project '
            'or create a new project using `create_new` method')
def get_project(connection, name, error_msg=None, throw_error=True,
                whitelist=[('ERR001', 500), ('ERR014', 403)]):
    """Get a specific project that the authenticated user has access to.

    Args:
        connection: MicroStrategy REST API connection object
        name (string): MicroStrategy project name
        error_msg (string, optional): Custom Error Message for Error Handling
        whitelist(list): list of tuples of I-Server Error and HTTP errors codes
            respectively, which will not be handled
            i.e. whitelist = [('ERR001', 500),('ERR004', 404)]

    Returns:
        Complete HTTP response object.
    """
    return connection.get(url=f'{connection.base_url}/api/projects/{name}')


@ErrorHandler(err_msg='Error fetching list of available projects.')
def get_projects(connection, error_msg=None, whitelist=None):
    """Get a list of all projects that the authenticated user has access to.

    Args:
        connection: MicroStrategy REST API connection object
        error_msg (string, optional): Custom Error Message for Error Handling
        whitelist(list): list of tuples of I-Server Error and HTTP errors codes
            respectively, which will not be handled
            i.e. whitelist = [('ERR001', 500),('ERR004', 404)]

    Returns:
        Complete HTTP response object.
    """

    return connection.get(
        url=f'{connection.base_url}/api/projects',
        headers={'X-MSTR-ProjectID': None}
    )


def create_project(connection, body, error_msg=None):
    """Create a new project, either synchronously or asynchronously.

    Args:
        connection: MicroStrategy REST API connection object
        body: JSON-formatted definition of the dataset. Generated by
            `utils.formjson()`.
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    response = connection.post(
        url=connection.base_url + '/api/projects',
        headers={'X-MSTR-ProjectID': None},
        json=body,
    )
    if response.status_code != 201:
        if error_msg is None:
            error_msg = "Project could not be created."
        response_handler(response, error_msg)
    return response


@ErrorHandler(err_msg='Error getting project import quota for project with ID {id}')
def get_project_import_quota(connection, id, error_msg=None):
    """Get the amount of space, in MB, that can be used for the Data Import
    function for a specific project. This is the default value applied to all
    users.

    Args:
        connection: MicroStrategy REST API connection object
        id (string): Project id string
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    return connection.get(url=f'{connection.base_url}/api/projects/{id}/quotas')


@ErrorHandler(err_msg='Error setting import quota for project with ID {id}')
def set_project_import_quota(connection, id, body, error_msg=None):
    """Set the amount of space, in MB, that can be used for the Data Import
    function for a specific project.

    Args:
        connection: MicroStrategy REST API connection object
        id (string): Project id string
        body: JSON-formatted definition of the dataset. Generated by
            `utils.formjson()`.
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    return connection.put(
        url=f'{connection.base_url}/api/projects/{id}/quotas',
        headers={'X-MSTR-ProjectID': None},
        json=body,
    )


@ErrorHandler(err_msg='Error setting user {user_id} import quota for project with ID {id}')
def set_user_import_quota(connection, id, user_id, body, error_msg=None):
    """Set the amount of space, in MB, that can be used for the Data Import
    function for a specific user. The value provided is rounded to an integer.

    Args:
        connection: MicroStrategy REST API connection object
        id (string): Project id string
        user_id (string): User ID string
        body: JSON-formatted definition of the dataset. Generated by
            `utils.formjson()`.
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    return connection.put(
        url=f'{connection.base_url}/api/projects/{id}/users/{user_id}/quotas',
        headers={'X-MSTR-ProjectID': None},
        json=body,
    )


@ErrorHandler(err_msg='Error getting user import quota for project with ID {id}')
def get_user_import_quota(connection, id, user_id=None, error_msg=None):
    """Get a list of users for whom Data Import quotas have been set and their
    quotas.

    Args:
        connection: MicroStrategy REST API connection object
        id (string): Project id string
        user_id (string, optional): User id string
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    return connection.get(
        url=f'{connection.base_url}/api/projects/{id}/users/quotas',
        headers={'X-MSTR-ProjectID': None},
        params={'user_id': user_id},
    )


@ErrorHandler(err_msg='Error fetching project {id} settings configuration.')
def get_project_settings_config(connection, id, error_msg=None):
    """Get project settings configurations.

    Args:
        connection: MicroStrategy REST API connection object
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    return connection.get(
        url=f'{connection.base_url}/api/v2/projects/{id}/settings/config',
        headers={'X-MSTR-ProjectID': None},
    )


@ErrorHandler(err_msg='Error getting project settings for project with ID {id}')
def get_project_settings(connection, id, error_msg=None, whitelist=None):
    """Get project settings.

    Args:
        connection: MicroStrategy REST API connection object
        id (string): Project id string
        error_msg (string, optional): Custom Error Message for Error Handling
        whitelist(list): list of tuples of I-Server Error and HTTP errors codes
            respectively, which will not be handled
            i.e. whitelist = [('ERR001', 500),('ERR004', 404)]

    Returns:
        Complete HTTP response object.
    """
    return connection.get(
        url=f'{connection.base_url}/api/v2/projects/{id}/settings',
        headers={'X-MSTR-ProjectID': None},
    )


@ErrorHandler(err_msg='Error setting project settings for project with ID {id}')
def set_project_settings(connection, id, body, error_msg=None):
    """Set new project settings.

    Args:
        connection: MicroStrategy REST API connection object
        id (string, optional): Project id string
        body (dict): body of the request
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    return connection.put(
        url=f'{connection.base_url}/api/v2/projects/{id}/settings',
        headers={'X-MSTR-ProjectID': None},
        json=body,
    )


@ErrorHandler(err_msg='Error updating project settings for project with ID {id}')
def update_project_settings(connection, id, body, error_msg=None):
    """Update project settings.

    Args:
        connection: MicroStrategy REST API connection object
        id (string): Project id string
        body (dict): body of the request
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    return connection.patch(
        url=f'{connection.base_url}/api/v2/projects/{id}/settings',
        headers={'X-MSTR-ProjectID': None},
        json=body,
    )


@ErrorHandler(err_msg='Error getting engine setting for project with ID {id}')
def get_engine_settings(connection, id, error_msg=None):
    """Get available and current engine settings for a project.

    Args:
        connection: MicroStrategy REST API connection object
        id (string): Project id string
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    return connection.get(
        url=f'{connection.base_url}/api/projects/{id}/settings/engine',
        headers={'X-MSTR-ProjectID': None},
    )


@ErrorHandler(err_msg='Error getting project startup settings.')
def get_projects_on_startup(connection, error_msg=None, whitelist=None):
    """Get a list of projects along with the nodes on which they would be
    available when the iServer starts up.

    Args:
        connection: MicroStrategy REST API connection object
        error_msg (string, optional): Custom Error Message for Error Handling
        whitelist(list): list of tuples of I-Server Error and HTTP errors codes
            respectively, which will not be handled
            i.e. whitelist = [('ERR001', 500),('ERR004', 404)]

    Returns:
        Complete HTTP response object.
    """
    return connection.get(
        url=f'{connection.base_url}/api/projects/settings/onStartup',
        headers={'X-MSTR-ProjectID': None}
    )


@ErrorHandler(err_msg='Error updating project startup settings.')
def update_projects_on_startup(connection, body, error_msg=None, whitelist=None):
    """Update status of projects on iServer nodes at start up. You provide
    the request body as of list of replace operations to be performed on the
    value of array of nodes with the path URI containing the corresponding
    project id that needs to be updated.

    Args:
        connection: MicroStrategy REST API connection object
        body: {"operationList": [{
                    "op": "replace",
                    "path": "/projects/B7CA92F04B9FAE8D941C3E9B7E0CD754/nodes",
                    "value": ["env-183260laio2use1"]
                    }]
            }
        error_msg (string, optional): Custom Error Message for Error Handling
        whitelist(list): list of tuples of I-Server Error and HTTP errors codes
            respectively, which will not be handled
            i.e. whitelist = [('ERR001', 500),('ERR004', 404)]

    Returns:
        Complete HTTP response object.
    """
    return connection.patch(
        url=f'{connection.base_url}/api/projects/settings/onStartup',
        headers={'X-MSTR-ProjectID': None},
        json=body,
    )
