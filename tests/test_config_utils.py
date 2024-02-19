import unittest
import json
import os
from config_utils import load_config

# Define a test case class for the load_config function, inheriting from unittest.TestCase
class TestConfigUtils(unittest.TestCase):

    def setUp(self):
        """Prepare the environment for testing.
        
        This method is automatically called before each test method to set up the test environment.
        """
        # Define the path and name of the temporary configuration file to be used in tests
        self.test_config_file = 'test_config.json'
        # Define a dictionary representing the mock configuration settings to be used in testing
        self.test_config = {
            "openweathermap_api_key": "test_key",
            "default_country_code": "us",
            "units": "metric"
        }
        # Create a temporary config file with the test configuration settings before running each test
        with open(self.test_config_file, 'w') as f:
            json.dump(self.test_config, f)

    def tearDown(self):
        """Clean up the test environment after testing.
        
        This method is automatically called after each test method to clean up the test environment.
        """
        # Remove the temporary configuration file after the test completes
        os.remove(self.test_config_file)

    def test_load_config(self):
        """Test if the load_config function correctly loads the configurations from a file.
        
        This test verifies that the load_config function reads the configuration file and the content
        matches the expected configuration dictionary defined in setUp.
        """
        # Call the load_config function with the path to the temporary test configuration file
        config = load_config(self.test_config_file)
        # Assert that the loaded configuration matches the expected test configuration
        self.assertEqual(config, self.test_config, "load_config should correctly load the configurations.")

# Execute the unit tests if this script is run directly
if __name__ == '__main__':
    unittest.main()
