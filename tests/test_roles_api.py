import pytest
import requests_mock

from penapi.pentaho import Pentaho
from templates.roles_api_return import ROLES_USER


@pytest.fixture
def pentaho():
    pentaho = Pentaho(pentaho_base_url='http://test.com')
    return pentaho


@requests_mock.Mocker(kw='mock_api')
def test_role_api_list_success(mock_api, pentaho=pentaho()):
    mock_api.get('http://test.com/pentaho/api/userroledao/userRoles?userName=test', text=ROLES_USER)
    roles_list = pentaho.roles.list_for_user('test')
    assert len(roles_list) == 3


@requests_mock.Mocker(kw='mock_api')
def test_role_api_list_fail(mock_api, pentaho=pentaho()):
    mock_api.get('http://test.com/pentaho/api/userroledao/userRoles?userName=test', text='', status_code=500)
    roles_list = pentaho.roles.list_for_user('test')
    assert len(roles_list) == 0


@requests_mock.Mocker(kw='mock_api')
def test_role_api_assign_success(mock_api, pentaho=pentaho()):
    mock_api.put('http://test.com/pentaho/api/userroledao/assignRoleToUser?userName=test&roleNames=power', text='')
    success = pentaho.roles.assign_to_user('test', ['power'])
    assert success


@requests_mock.Mocker(kw='mock_api')
def test_role_api_assign_fail(mock_api, pentaho=pentaho()):
    mock_api.put('http://test.com/pentaho/api/userroledao/assignRoleToUser?userName=test&roleNames=power',
                 text='', status_code=403)
    success = pentaho.roles.assign_to_user('test', ['power'])
    assert not success


def test_role_api_assign_fail_2(pentaho=pentaho()):
    with pytest.raises(ValueError):
        pentaho.roles.assign_to_user('test', 'power')


@requests_mock.Mocker(kw='mock_api')
def test_role_api_remove_success(mock_api, pentaho=pentaho()):
    mock_api.put('http://test.com/pentaho/api/userroledao/removeRoleFromUser?userName=test&roleNames=Business', text='')
    success = pentaho.roles.remove_from_user('test', ['Business'])
    assert success


@requests_mock.Mocker(kw='mock_api')
def test_role_api_remove_fail(mock_api, pentaho=pentaho()):
    mock_api.put('http://test.com/pentaho/api/userroledao/removeRoleFromUser?userName=test&roleNames=Business',
                 text='', status_code=403)
    success = pentaho.roles.remove_from_user('test', ['Business'])
    assert not success


def test_role_api_remove_fail_2(pentaho=pentaho()):
    with pytest.raises(ValueError):
        pentaho.roles.remove_from_user('test', 'Business')
