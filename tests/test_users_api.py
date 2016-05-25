import pytest
import requests_mock

from penapi.pentaho import Pentaho
from templates.user_api_return import LIST_USERS


@requests_mock.Mocker()
def test_user_api_list_success(m):
    # mock_api.get('http://test.com/pentaho/api/userroledao/users', text=LIST_USERS)
    pentaho = Pentaho(pentaho_base_url='http://test.com')
    m.register_uri('GET', 'http://test.com/pentaho/api/userroledao/users', text=LIST_USERS)
    user_list = pentaho.users.list()
    assert len(user_list) == 6


def test_user_api_list_fail():
    pentaho = Pentaho(pentaho_base_url='http://test.com')
    user_list = pentaho.users.list()
    assert len(user_list) == 0