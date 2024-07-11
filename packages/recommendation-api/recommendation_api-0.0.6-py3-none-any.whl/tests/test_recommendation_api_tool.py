import pytest
import unittest

from promptflow.connections import CustomConnection

# from hello_world.tools.hello_world_tool import get_greeting_messagename
from recommendation.tools.recommendation_api_tool import get_recommendation_api


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
    def test_get_greeting_messagename(self):
        result = get_recommendation_api(
            http_method="POST",
            api_url="test",
            content_type="test",
            requestId="test",
            country="test",
            num="test",
            pageType="test",
            guid="test",
        )
        assert result


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
