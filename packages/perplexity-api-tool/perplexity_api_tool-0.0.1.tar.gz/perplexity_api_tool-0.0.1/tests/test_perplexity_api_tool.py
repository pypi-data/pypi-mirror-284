import pytest
import unittest

from promptflow.connections import CustomConnection
from perplexity.tools.perplexity_api_tool import get_perplexity_result


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
    def test_get_perplexity_result(self):
        result = get_perplexity_result(
            url="test",
            api_key="test",
            model="test",
            chat_input="test",
        )
        assert result


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
