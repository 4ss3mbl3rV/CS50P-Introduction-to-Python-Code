from working import convert
import pytest

def test_working():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_error():
    with pytest.raises(ValueError):
        convert("9 AM - 10 PM")
    with pytest.raises(ValueError):
        convert("15 AM to 18 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 10:60 PM")
