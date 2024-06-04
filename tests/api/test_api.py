import pytest
import requests


@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""
@pytest.mark.check
def test_name(user):
    assert 7 * 7 == 49

@pytest.mark.check
def test_check_math78(user):
    assert 7 * 8 == 56
    assert user.name == "Sergii"


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Butenko"