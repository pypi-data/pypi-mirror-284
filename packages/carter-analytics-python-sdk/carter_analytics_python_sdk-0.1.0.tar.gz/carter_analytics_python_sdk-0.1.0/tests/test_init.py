from asyncio.log import logger

import pytest
from unittest.mock import patch, MagicMock  # Import the patch function from unittest.mock

from src import carter_analytics_client


@pytest.mark.parametrize(
    ("config", "expected_exception"),
    [
        (None, TypeError),  # Expect TypeError for None configuration
        ([], ValueError),  # Expect ValueError for empty list configuration
        ({"key": "value"}, TypeError),  # Expect ValueError for invalid dictionary
        ([{"api_key": "abc"}], ValueError),  # Expect ValueError for invalid list
    ],
)
@patch('requests.post')
def test_initialize_invalid_config(mock_post, config, expected_exception):
    """
    Test initialize method with invalid configurations.
    """
    # Configure the mock to simulate a successful API response
    mock_response = MagicMock()
    mock_response.json.return_value = {'success': False}
    mock_response.raise_for_status = MagicMock()
    mock_post.return_value = mock_response

    with pytest.raises(expected_exception):
        carter_analytics_client.initialize(config)


@patch('requests.post')
def test_initialize_valid_config(
        mock_post
):
    """
    Test initialize method with valid configuration.

    Args:
        mock_post: Mocked version of post request method of requests library.
    """

    # Configure the mock to simulate a successful API response
    mock_response = MagicMock()
    mock_response.json.return_value = {'success': True}
    mock_response.raise_for_status = MagicMock()
    mock_post.return_value = mock_response

    config = [{"api_key": "valid_api_key"}]
    carter_analytics_client.initialize(config)


@patch('requests.post')
def test_publish(mock_post):
    """
    Test publish method with event data.

    Args:
        mock_post: Mocked version of post request method of requests library.
    """
    # Configure the mock to simulate a successful API response
    mock_response = MagicMock()
    mock_response.json.return_value = {'success': True}
    mock_response.raise_for_status = MagicMock()
    mock_post.return_value = mock_response

    event_data = {
        "event": "add_to_cart",
        "event_properties": {
            "cart_amount": 54.98,
            "currency": "USD",
            "cart_items": [
                {
                    "id": "12345",
                    "price": 19.99,
                    "currency": "USD",
                    "title": "T-Shirt",
                    "quantity": 2
                },
                {
                    "id": "67890",
                    "price": 34.99,
                    "currency": "USD",
                    "title": "Hoodie",
                    "quantity": 1,
                    "image_url": "https://example.com/hoodie.jpg",
                    "product_category_1": "Apparel",
                    "product_category_2": "Tops"
                }
            ]
        },
        "user_properties": {
            "id": "user_456",
            "name": "John Doe",
            "email": "johndoe@example.com",
            "is_vip": True
        },
        "meta_parameters": {
            "user_agent": "Mozilla/5.0 (iPad; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, "
                          "like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4",
            "ip_address": "192.168.1.100",
            "referrer": "https://pypi.org/"
        }
    }

    config = [{"api_key": "valid_api_key"}]
    carter_analytics_client.initialize(config)
    carter_analytics_client.publish(event_data)
