import requests
import time
import sqlite3
from datetime import datetime

API_KEY = "d75499e292d2af46d2f6ebd9274c21f0"
CITIES = ["Guangzhou", "Tianshui", "Jinhua", "Zhaotong", "Jinan"]

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    humidity INTEGER,
    pressure INTEGER,
    weather_desc TEXT,
    wind_speed REAL,
    fetch_time TEXT
)
""")
conn.commit()

for city in CITIES:
	URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

	try:
		response = requests.get(URL, timeout = 10)
		data = response.json()
		
		city_name = data["name"]
		temp = data["main"]["temp"]
		humidity = data["main"]["humidity"]
		pressure = data["main"]["pressure"]
		weather_desc = data["weather"][0]["description"]
		wind_speed = data["wind"]["speed"]
		fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print(city, temp, humidity, pressure, weather_desc, wind_speed)

		cursor.execute("""
            INSERT INTO weather_data (city, temperature, humidity, pressure, weather_desc, wind_speed, fetch_time)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (city_name, temp, humidity, pressure, weather_desc, wind_speed, fetch_time))
		conn.commit()
		
		print("已存入数据库")

	except Exception as e:
		print(f"发生错误, {city} 数据获取失败: {e}")
	
	time.sleep(1)

conn.close()
print("所有数据已存入数据库")