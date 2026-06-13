import sqlite3
import pandas as pd

conn = sqlite3.connect("weather.db")
df = pd.read_sql("SELECT * FROM weather_data ORDER BY id DESC LIMIT 10", conn)
print(df)
conn.close()