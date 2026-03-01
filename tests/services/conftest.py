import pytest

from mcp_services.ping_service import PingService
from mcp_services.weather_service import WeatherService


@pytest.fixture
def ping_service() -> PingService:
    return PingService()


@pytest.fixture
def weather_service(monkeypatch: pytest.MonkeyPatch) -> WeatherService:
    monkeypatch.setenv("WEATHER_API_KEY", "test-api-key")
    return WeatherService()
