import pytest

from daykit import (
    good_morning,
    good_afternoon,
    good_evening,
    get_greeting,
)


def test_good_morning():
    assert good_morning("Ishara") == "Good morning, Ishara!"


def test_good_afternoon():
    assert good_afternoon("Ishara") == "Good afternoon, Ishara!"


def test_good_evening():
    assert good_evening("Ishara") == "Good evening, Ishara!"


@pytest.mark.parametrize(
    ("hour", "expected"),
    [
        (8, "Good morning, Ishara!"),
        (12, "Good afternoon, Ishara!"),
        (17, "Good afternoon, Ishara!"),
        (18, "Good evening, Ishara!"),
    ],
)
def test_get_greeting(hour, expected):
    assert get_greeting("Ishara", hour) == expected


def test_empty_name():
    with pytest.raises(ValueError):
        good_morning("")


def test_invalid_hour():
    with pytest.raises(ValueError):
        get_greeting("Ishara", 24)
