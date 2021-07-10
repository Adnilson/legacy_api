import pytest
from items_api.services.result_processor import ResultProcessor

@pytest.fixture
def result(page):
    return {
        'data': list(range(100)),
        'metadata': {'page': page}
    }


@pytest.mark.parametrize(('length', 'page', 'per_page'), (
    (100, 1, None),
    (2, 5, 2)
))
def test_result_processor(result, length, page, per_page):
    items = ResultProcessor().run(result, per_page)

    assert len(items['data']) == length
    assert items['metadata']['page'] == page
    assert items['metadata']['perPage'] == length
