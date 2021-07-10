import pytest
from unittest.mock import Mock

from items_api.services.request_legacy_api import RequestLegacyAPI
from items_api.services.result_processor import ResultProcessor

@pytest.fixture
def result_processor():
    return Mock(spec=ResultProcessor)

def test_result_processor_is_called(result_processor):
    page = 2
    per_page = 5
    legacy = RequestLegacyAPI(page, per_page)
    legacy.request = Mock(return_value="text")
    legacy.run(result_processor)

    result_processor.assert_called()
