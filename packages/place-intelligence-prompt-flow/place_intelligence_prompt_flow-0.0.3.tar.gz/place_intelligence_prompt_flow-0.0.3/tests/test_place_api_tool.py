import pytest
import unittest

from promptflow.connections import CustomConnection
from place.tools.place_api_tool import get_place_intelligence_flow_api


@pytest.fixture
def my_custom_connection() -> CustomConnection:
    my_custom_connection = CustomConnection(
        {
            "api-key": "my-api-key",
            "api-secret": "my-api-secret",
            "api-url": "my-api-url",
        }
    )
    return my_custom_connection


class TestTool:
    def test_get_place_intelligence_flow_api(self):
        result = get_place_intelligence_flow_api(
            allowed=True,
            chat_input={"message": "test", "image": ""},
            end_point="test",
            api_key="test",
            deployment_name="test",
        )
        assert result


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
