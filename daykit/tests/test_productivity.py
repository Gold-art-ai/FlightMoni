import pytest

from daykit import percentage, pomodoro_sessions


def test_percentage():
    assert percentage(45, 60) == 75


def test_percentage_zero():
    with pytest.raises(ValueError):
        percentage(1, 0)


def test_pomodoro_sessions():
    assert pomodoro_sessions(100) == 4


def test_custom_session_length():
    assert pomodoro_sessions(90, 30) == 3
