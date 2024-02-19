import requests
import logging
from config_utils import load_config

# Configure logging at the module level. For larger applications, you might
# do this in your main application file or a separate configuration module.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def fetch_current_weather(api_key, city, country='us', units='metric'):
    """
    Fetch current weather data for a specified city from OpenWeatherMap.

    Parameters:
    - api_key (str): Your API key for the OpenWeatherMap API.
    - city (str): The city name for which to fetch weather data.
    - country (str): The country code (ISO 3166 country code) for the city. Defaults to 'us'.
    - units (str): The unit system for the temperature. Can be 'metric', 'imperial', or 'standard'. Defaults to 'metric'.
    
    Returns:
    - dict: The weather data for the specified city if the request is successful; None otherwise.
    """
    logger = logging.getLogger(__name__)  # Get a logger object for this module

    # Construct the URL for the API request using the provided parameters
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    full_url = f"{base_url}?q={city},{country}&appid={api_key}&units={units}"
    
    try:
        # Make the HTTP GET request to the OpenWeatherMap API
        response = requests.get(full_url)
        # Automatically raise an exception for 4XX and 5XX status codes
        response.raise_for_status()
        # Return the JSON data from the response if the request was successful
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        # Log the HTTP error with exception information
        logger.error(f"HTTP error occurred while fetching weather data for {city}: {http_err}", exc_info=True)
    except Exception as err:
        # Log any other exceptions with exception information
        logger.error(f"An unexpected error occurred while fetching weather data for {city}: {err}", exc_info=True)

    # Return None if an error occurred during the API request
    return None
