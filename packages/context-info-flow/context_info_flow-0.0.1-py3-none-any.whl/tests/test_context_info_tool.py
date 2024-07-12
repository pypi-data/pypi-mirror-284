import pytest
import unittest

from promptflow.connections import CustomConnection
from context_info.tools.context_info_tool import get_context_info


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
    def test_get_context_info(self):
        result = get_context_info(
            azure_search_endpoint="test",
            azure_search_key="test",
            azure_search_api_version="test",
            index_name="test",
            top="5",
            user_query="test",
        )
        assert result


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
