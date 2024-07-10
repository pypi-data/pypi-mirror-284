import pytest
import unittest

from promptflow.connections import CustomConnection
from recommendation.tools.recommendation_api_tool import (
    get_recommendation_intelligence_flow_api,
)


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
    def test_get_recommendation_intelligence_flow_api(self):
        result = get_recommendation_intelligence_flow_api(
            allowed=True,
            chat_input={"message": "모니터 추천해줘", "image": ""},
            end_point="https://recommendation-api-endpoint.eastus.inference.ml.azure.com/score",
            api_key="GY5T30PdjQ8W1KxRdibJR2Q892PGE2h4",
            deployment_name="recommendation-api-endpoint",
        )
        assert result


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
