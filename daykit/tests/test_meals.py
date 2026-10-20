import pytest

from daykit import meal_time


def test_lunch():
    assert "Lunch time" in meal_time(12)


def test_invalid_hour():
    with pytest.raises(ValueError):
        meal_time(25)
