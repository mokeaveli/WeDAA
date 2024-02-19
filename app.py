import logging
from flask import Flask, jsonify, request
from weather_data_retrieval import fetch_current_weather
from config_utils import load_config

# Initialize the Flask application.
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='wedaa.log', filemode='a')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger('').addHandler(console_handler)

logger = logging.getLogger('WeDAAApp')

# Define the path to the configuration file, assuming it's in the same directory as this script.
CONFIG_FILE_PATH = 'config.json'
# Load the configuration settings from the specified file.
config = load_config(CONFIG_FILE_PATH)

# Log the loaded API key to verify configuration is loaded correctly.
# Important: Avoid logging sensitive information like API keys in a production environment.
logger.info("Application started. Configuration loaded successfully.")

# Define a route for the root URL which returns a welcome message.
@app.route('/')
def home():
    logger.info('Home route accessed')
    return "Welcome to the Weather Data Aggregator and Analyzer (WeDAA)!"

# Define a route for fetching weather data. This route accepts query parameters for city, country, and units.
@app.route('/weather')
def get_weather():
    # Retrieve query parameters with defaults if not provided.
    city = request.args.get('city', default='London', type=str)
    country = request.args.get('country', default='GB', type=str)
    units = request.args.get('units', default='metric', type=str)
    
    logger.debug(f"Fetching weather for {city}, {country} in {units} units")

    # Fetch the weather data using the provided parameters and the API key from the configuration.
    weather_data = fetch_current_weather(config['openweathermap_api_key'], city, country, units)
    
    # Check if weather data was successfully retrieved and return it as JSON; otherwise, return an error message.
    if weather_data:
        return jsonify(weather_data)
    else:
        logger.error(f"Failed to retrieve weather data for {city}, {country}")
        return jsonify({'error': 'Weather data not available'}), 404

# Check if this script is executed as the main program and run the Flask application in debug mode if true.
if __name__ == '__main__':
    app.run(debug=True)
