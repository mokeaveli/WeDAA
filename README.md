# Weather Data Aggregator and Analyzer (WeDAA)

## Project Overview
WeDAA is a backend-focused project designed to aggregate real-time and historical weather data from multiple public APIs, store this data efficiently, and provide meaningful analysis or insights. The system targets the general public interested in weather trends and researchers or historians seeking detailed historical weather data across Europe.

## Key Features
- **Real-time Weather Updates**: Access up-to-date weather information for specified locations.
- **Historical Weather Data Analysis**: Query and analyze patterns from historical weather data.
- **Weather Trend Predictions**: Utilize historical data to predict future weather trends.
- **Data Visualization**: Visualize weather data through charts and graphs for enhanced interpretability (minimal frontend involved).

## Technologies Used
- Backend: Python with Flask
- Database: PostgreSQL
- Additional Libraries: requests, psycopg2-binary, pandas, numpy, SQLAlchemy, Flask-RESTful
- Containerization: Docker

## Getting Started

### Prerequisites
- Python 3.8 or later
- Docker and Docker Compose
- Git

### Setup Instructions

1. **Clone the repository**
git clone <git@github.com:mokeaveli/WeDAA.git>
cd WeDAA

2. **Set up a virtual environment** (optional if using Docker)
- Create a virtual environment:
  ```
  python -m venv venv
  ```
- Activate the virtual environment:
  - On Windows: `venv\Scripts\activate`
  - On Unix or MacOS: `source venv/bin/activate`

3. **Install dependencies**
- With virtual environment activated:
  ```
  pip install -r requirements.txt
  ```

4. **Docker Setup** (Skip if not using Docker)
- Ensure Docker and Docker Compose are installed on your system.
- Build and run the containers:
  ```
  docker-compose up --build
  ```

5. **Environment Variables**
- Set up necessary environment variables for database connections and API keys as required.

6. **Running the Application**
- If using Docker, the application should be accessible as configured in `docker-compose.yml`.
- If running locally without Docker, start your Flask application:
  ```
  flask run
  ```

### API Keys
- You will need to obtain API keys for the weather services used (OpenWeatherMap, Met Office API). Please refer to their respective websites for instructions on how to obtain these keys.

## Contributing
Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest features.

## License
Specify your project's license here.
