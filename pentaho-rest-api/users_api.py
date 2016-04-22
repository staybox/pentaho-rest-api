import requests


def create_user(pentaho=None, username=None, password=None):
    """
    Create a user in pentaho
    :param pentaho: the penaho
    :param username: the username to assign to the user
    :param password: the password for the user
    :return: (http/s Response, success/failure )
    :rtype: (String, boolean)
    """
    created = False
    if not pentaho:
        raise ValueError("[ERROR] Pentaho object is missing ... ")
    if not username or not password:
        raise ValueError("[ERROR] user creation parameters missing ... ")
    user_credentials = {
        "userName": username,
        "password": password,
    }
    response = requests.put(pentaho.pentaho_base_url, auth=(pentaho.pentaho_username, pentaho.pentaho_password),
                            json=user_credentials)
    if response.status_code == 200:
        created = True
    return response, created
