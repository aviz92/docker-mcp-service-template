import os
from typing import Any

import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
TIMEOUT_SECONDS = 10


class WeatherService:
    def __init__(self) -> None:
        self.api_key = os.getenv("WEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("Missing WEATHER_API_KEY environment variable")

    def fetch_weather(self, city: str) -> dict[str, Any]:
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
        }
        response = requests.get(BASE_URL, params=params, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data.get("name"),
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
