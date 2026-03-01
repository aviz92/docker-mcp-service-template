# pylint: disable=redefined-outer-name
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
import requests.exceptions
from requests.exceptions import HTTPError

from mcp_services.weather_service import WeatherService


@pytest.fixture
def weather_service(monkeypatch: pytest.MonkeyPatch) -> WeatherService:
    monkeypatch.setenv("WEATHER_API_KEY", "test-api-key")
    return WeatherService()


def _mock_response(data: dict[str, Any], status_code: int = 200) -> MagicMock:
    mock = MagicMock()
    mock.status_code = status_code
    mock.json.return_value = data
    mock.raise_for_status = MagicMock()
    return mock


VALID_API_RESPONSE: dict[str, Any] = {
    "name": "Tel Aviv",
    "main": {"temp": 24.3, "humidity": 58},
    "weather": [{"description": "clear sky"}],
    "wind": {"speed": 4.1},
}


class TestWeatherService:
    def test_fetch_weather_missing_api_key_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("WEATHER_API_KEY", raising=False)
        with pytest.raises(ValueError, match="Missing WEATHER_API_KEY"):
            WeatherService()

    def test_fetch_weather_returns_expected_fields(self, weather_service: WeatherService) -> None:
        with patch("mcp_services.weather_service.requests.get", return_value=_mock_response(VALID_API_RESPONSE)):
            result = weather_service.fetch_weather("Tel Aviv")

        assert result["city"] == "Tel Aviv", f"Unexpected city: {result['city']}"
        assert result["temperature"] == 24.3, f"Unexpected temperature: {result['temperature']}"
        assert result["description"] == "clear sky", f"Unexpected description: {result['description']}"
        assert result["humidity"] == 58, f"Unexpected humidity: {result['humidity']}"
        assert result["wind_speed"] == 4.1, f"Unexpected wind_speed: {result['wind_speed']}"

    def test_fetch_weather_passes_timeout(self, weather_service: WeatherService) -> None:
        with patch(
            "mcp_services.weather_service.requests.get", return_value=_mock_response(VALID_API_RESPONSE)
        ) as mock_get:
            weather_service.fetch_weather("Tel Aviv")
        _, kwargs = mock_get.call_args
        assert "timeout" in kwargs, "requests.get must be called with a timeout"

    def test_fetch_weather_http_error_propagates(self, weather_service: WeatherService) -> None:
        mock = _mock_response({}, status_code=404)
        mock.raise_for_status.side_effect = HTTPError("404 Not Found")
        with patch("mcp_services.weather_service.requests.get", return_value=mock):
            with pytest.raises(HTTPError):
                weather_service.fetch_weather("UnknownCity")

    def test_fetch_weather_connection_error_propagates(self, weather_service: WeatherService) -> None:
        with patch(
            "mcp_services.weather_service.requests.get",
            side_effect=requests.exceptions.ConnectionError("Network unreachable"),
        ):
            with pytest.raises(requests.exceptions.ConnectionError):
                weather_service.fetch_weather("Tel Aviv")
