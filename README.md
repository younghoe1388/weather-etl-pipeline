# Weather ETL Pipeline / 天气数据 ETL 管道

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## English / 英文

A simple ETL pipeline that fetches real-time weather data from OpenWeatherMap API and stores it into SQLite database.

一个简单的 ETL 管道，从 OpenWeatherMap API 获取实时天气数据并存入 SQLite 数据库。

---

## Features / 功能特性

| English | 中文 |
|---------|------|
| Fetch weather data for multiple cities (Guangzhou, Tianshui, Jinhua, Zhaotong, Jinan) | 获取多个城市（广州、天水、金华、昭通、济南）的天气数据 |
| Extract temperature, humidity, pressure, weather description, wind speed | 提取温度、湿度、气压、天气描述、风速 |
| Store data into SQLite database | 将数据存入 SQLite 数据库 |
| Error handling for failed requests | 处理请求失败的错误情况 |
| Schedule daily execution via Windows Task Scheduler | 通过 Windows 任务计划程序实现每日自动执行 |

---

## Tech Stack / 技术栈

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| HTTP Client | requests |
| Data Processing | pandas |
| Database | SQLite |
| Scheduling | Windows Task Scheduler / Task Scheduler |

---

## Database Schema / 数据库表结构

| Column | Type | Description / 描述 |
|--------|------|-------------------|
| city | TEXT | City name / 城市名称 |
| temperature | REAL | Temperature in Celsius / 温度（摄氏度） |
| humidity | INTEGER | Humidity percentage / 湿度百分比 |
| pressure | INTEGER | Atmospheric pressure (hPa) / 气压（百帕） |
| weather_desc | TEXT | Weather description / 天气描述 |
| wind_speed | REAL | Wind speed (m/s) / 风速（米/秒） |
| fetch_time | TEXT | Timestamp of data fetch / 数据获取时间戳 |

---

## Schedule Automation / 日程自动化
Use Windows Task Scheduler to run the script daily. See the `run_weather.bat` file for reference.

使用 Windows 任务计划程序每天运行该脚本。请参阅 `run_weather.bat` 文件以获取更多信息。

## Author / 作者
hy

## License / 许可证
MIT

## License
MIT
