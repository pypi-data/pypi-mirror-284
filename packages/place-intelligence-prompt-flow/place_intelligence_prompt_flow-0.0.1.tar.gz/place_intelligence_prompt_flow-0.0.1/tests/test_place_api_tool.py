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
            chat_input={"message": "양양에 있는 매장 알려줘", "image": ""},
            end_point="https://place-intelligence-endpoint.eastus.inference.ml.azure.com/score",
            api_key="WbdH5a1t9ruiR95npZP8F2AzeAYrgVrH",
            deployment_name="place-intelligence-endpoint-7",
        )
        assert result


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
