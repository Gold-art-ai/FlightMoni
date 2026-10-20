from datetime import datetime, timedelta

import pytest

from daykit import attendant_load, movement_signal


def test_departure_without_checkin_is_urgent():
    signal = movement_signal("departure", datetime.now() + timedelta(minutes=20), checked_in=False)

    assert signal.label == "Crew check-in needed"
    assert signal.css_class == "danger"


def test_attendant_load_labels():
    assert attendant_load(0) == "Light roster"
    assert attendant_load(2) == "Active roster"
    assert attendant_load(4) == "Full roster"


def test_invalid_direction():
    with pytest.raises(ValueError):
        movement_signal("sideways", datetime.now(), checked_in=True)
