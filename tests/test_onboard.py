import pytest
from unittest.mock import patch

# Import the 'app' object from your API file
from api.onboard import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client

# Use @patch to replace the real 'send_slack_notification' function with a mock
@patch('api.onboard.send_slack_notification')
def test_successful_onboarding(mock_slack, client):
    """
    Test the happy path: a valid request should succeed and trigger a notification.
    """
    # Arrange: Prepare the test data
    valid_data = {'supplierName': 'Test Corp', 'gstin': '27ABCDE1234F1Z5'}

    # Act: Make a POST request to the API endpoint
    response = client.post('/api/onboard', json=valid_data)

    # Assert: Check the results
    assert response.status_code == 200
    assert 'Successfully validated' in response.get_json()['message']
    
    # Assert that our mock Slack function was called exactly once
    mock_slack.assert_called_once()

@patch('api.onboard.send_slack_notification')
def test_failed_validation_invalid_gstin(mock_slack, client):
    """
    Test the failure path: an invalid GSTIN should be rejected.
    """
    # Arrange
    invalid_data = {'supplierName': 'Invalid Corp', 'gstin': '99FAILGSTIN'}

    # Act
    response = client.post('/api/onboard', json=invalid_data)

    # Assert
    assert response.status_code == 400
    assert 'Invalid GSTIN' in response.get_json()['message']

    # Assert that the Slack function was NOT called
    mock_slack.assert_not_called()

def test_failed_validation_missing_data(client):
    """
    Test the failure path: a request with missing data should be rejected.
    """
    # Arrange
    missing_data = {'supplierName': 'Missing Data Corp'} # gstin is missing

    # Act
    response = client.post('/api/onboard', json=missing_data)

    # Assert
    assert response.status_code == 400
    assert 'required' in response.get_json()['message']
