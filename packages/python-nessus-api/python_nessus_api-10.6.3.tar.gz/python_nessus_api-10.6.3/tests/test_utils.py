from nessus.utils import url_validator


def test_url_validator_failed():
    url = "google.com"
    assert url_validator(url) is False
