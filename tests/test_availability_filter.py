from availability_filter import AvailabilityFilter
from beer import Beer
from yes_filter import YesFilter


def make_test_beer(available):
    return Beer("Guinness", "pint", "stout", 0, available)


def get_test_filter(quantity_requested):
    return AvailabilityFilter(YesFilter(), quantity_requested)


def test_quantity_filter_request_five_five_available():
    assert get_test_filter(5).is_match(make_test_beer(5)) is True


def test_quantity_filter_request_five_less_available():
    assert get_test_filter(5).is_match(make_test_beer(4)) is False


def test_quantity_filter_request_five_zero_available():
    assert get_test_filter(5).is_match(make_test_beer(0)) is False


def test_quantity_filter_request_five_six_available():
    assert get_test_filter(5).is_match(make_test_beer(6)) is True


def test_quantity_filter_request_five_negative_quantity_available():
    assert get_test_filter(5).is_match(make_test_beer(-5)) is False
