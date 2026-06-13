# Weather ETL Pipeline

A simple ETL pipeline that fetches real-time weather data from OpenWeatherMap API and stores it into SQLite database.

## Features
- Fetch weather data for multiple cities (Guangzhou, Tianshui, Jinhua, Zhaotong, Jinan)
- Extract temperature, humidity, pressure, weather description, wind speed
- Store data into SQLite database
- Error handling for failed requests
- Schedule daily execution via Windows Task Scheduler

## Tech Stack
- Python 3
- requests, pandas, sqlite3
- OpenWeatherMap API
- SQLite
- Windows Task Scheduler

## How to Run
1. Clone this repository
2. Install dependencies: `pip install requests pandas`
3. Get your API key from [OpenWeatherMap](https://openweathermap.org/api)
4. Replace `API_KEY` in `weather.py`
5. Run: `python weather.py`

## Database Schema
| Column | Type | Description |
|--------|------|-------------|
| city | TEXT | City name |
| temperature | REAL | Temperature in Celsius |
| humidity | INTEGER | Humidity percentage |
| pressure | INTEGER | Atmospheric pressure (hPa) |
| weather_desc | TEXT | Weather description |
| wind_speed | REAL | Wind speed (m/s) |
| fetch_time | TEXT | Timestamp of data fetch |

## Schedule Automation
Use Windows Task Scheduler to run the script daily. See the `run_weather.bat` file for reference.

## Author
hy

## License
MIT
