from datetime import datetime

import pytest

from daykit import format_duration, is_weekend


def test_format_duration():
    assert format_duration(125) == "2 minutes 5 seconds"


def test_format_hours():
    assert format_duration(3660) == "1 hour 1 minute"


def test_weekend():
    saturday = datetime(2026, 10, 10)
    assert is_weekend(saturday) is True


def test_weekday():
    monday = datetime(2026, 10, 5)
    assert is_weekend(monday) is False


def test_negative_duration():
    with pytest.raises(ValueError):
        format_duration(-1)
