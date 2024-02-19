import unittest
from unittest.mock import patch
from weather_data_retrieval import fetch_current_weather

# Define a test case class for testing the fetch_current_weather function, inheriting from unittest.TestCase
class TestFetchCurrentWeather(unittest.TestCase):

    # Use the patch decorator to mock the requests.get method used within the fetch_current_weather function
    @patch('weather_data_retrieval.requests.get')
    def test_fetch_current_weather_success(self, mock_get):
        # Configure the mock object to simulate a successful API response
        mock_get.return_value.status_code = 200  # Simulate HTTP 200 status code
        mock_get.return_value.json.return_value = {
            # Simulate JSON response data structure
            "weather": [{"main": "Clear", "description": "clear sky"}],
            "main": {"temp": 15.0, "humidity": 10},
            "wind": {"speed": 1.5},
            "name": "London"
        }

        # Define test parameters
        api_key = "dummy_api_key"
        city = "London"
        # Call the function with the test parameters
        result = fetch_current_weather(api_key, city)
        
        # Assert that the result is not None, indicating that some data was returned
        self.assertIsNotNone(result)
        # Assert that the city name in the result matches the test city
        self.assertEqual(result['name'], city)
        # Assert that the expected keys are present in the result dictionary
        self.assertIn('weather', result)
        self.assertIn('main', result)

    # Test case to simulate a failure in fetching weather data (e.g., city not found)
    @patch('weather_data_retrieval.requests.get')
    def test_fetch_current_weather_failure(self, mock_get):
        # Configure the mock object to simulate a failure response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 404  # Simulate HTTP 404 status code
        mock_response.json.return_value = None  # Simulate no JSON response

        # Define test parameters for a city that does not exist
        api_key = "dummy_api_key"
        city = "Nowhere"
        # Call the function with the test parameters
        result = fetch_current_weather(api_key, city)
        
        # Assert that the result is None, indicating that no data was returned due to the failure
        self.assertIsNone(result)

# Execute the unit tests when this script is run directly
if __name__ == '__main__':
    unittest.main()
