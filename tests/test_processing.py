from src.processing import filter_by_state, sort_by_date


def test_filter_executed(list_for_test, list_with_executed):
    assert filter_by_state(list_for_test) == list_with_executed


def test_filter_canceled(list_for_test, list_with_canceled):
    assert filter_by_state(list_for_test, 'CANCELED') == list_with_canceled


def test_sort_by_date(list_for_test, sort_list):
    assert sort_by_date(list_for_test) == sort_list


def test_sort_by_date_reverse(list_for_test, sort_list_reverse):
    assert sort_by_date(list_for_test, False) == sort_list_reverse
