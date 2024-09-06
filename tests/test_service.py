import pytest
import src.service as service
import unittest.mock as mock


@mock.patch('src.service.get_user_from_database')
def test_user_from_database(mocked_service):
    mocked_service.return_value = 'Rachel'
    assert service.get_user_from_database(1) == 'Rachel'
    

@mock.patch('requests.get')
def test_get_user(mocked_service):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "Name": "John"}
    
    mocked_service.return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "Name": "John"}