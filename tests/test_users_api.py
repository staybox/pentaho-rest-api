import pytest
import requests_mock

import users_api
from pentaho import Pentaho
from templates.user_api_return import LIST_USERS


def test_user_api_missing_pentaho():
    with pytest.raises(ValueError):
        users_api.create_user()
        users_api.list_all_users()


@requests_mock.mock()
def test_user_api_list_users(mock_api):
    mock_api.get('http://test.com/pentaho/api/users', text=LIST_USERS)
    pentaho = Pentaho(pentaho_base_url='http://test.com')
    response, user_list = users_api.list_all_users(pentaho=pentaho)
    assert response.status_code == 200
    assert len(user_list) == 6
