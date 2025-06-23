import json
import requests
from dotenv import load_dotenv
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

load_dotenv()
    
baseUrl = r'https://api.openweathermap.org/data/2.5/weather?'
# api = open(r"E:\modelContextProtocolServer\__pycache__\apiKey.txt",'r').read()
api = os.getenv("apiWeather")

@mcp.tool()
def currentWeather(city: str = "Jaspur") -> str:
    url = f"{baseUrl}q={city}&APPID={api}&unit=metric"
    status = requests.get(url)
    if status.status_code == 200:
        data = status.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        wind = data.get('wind', {})
        temp = main.get('temp')
        feels_like = main.get('feels_like')
        description = weather.get('description', 'No description')
        wind_speed = wind.get('speed', 'N/A')
        
        return (
            f"Weather in {city}:\n"
            f"Description: {description.capitalize()}\n"
            f"Temperature: {(float(temp) - 273.15):.2f}°C\n"
            f"Feels Like: {(float(feels_like) - 273.15):.2f}°C\n"
            f"Wind Speed: {wind_speed} m/s"
        )
    else:
        raise RuntimeError(f"Failed to get weather data for {city}. Status code: {status.status_code}")

if __name__ == "__main__":
    mcp.run(transport="stdio")