import pytest

from mcp_services.ping_service import PingService


@pytest.fixture
def ping_service() -> PingService:
    return PingService()


class TestPingService:
    def test_ping_returns_pong(self, ping_service: PingService) -> None:
        result = ping_service.ping()
        assert result == "pong", f"Expected 'pong', got '{result}'"

    def test_ping_returns_string(self, ping_service: PingService) -> None:
        result = ping_service.ping()
        assert isinstance(result, str), f"Expected str, got {type(result)}"
