from io import BytesIO

import pytest
import responses

from nessus.nessus import Nessus


@responses.activate
def test_session_authentication():
    """
    Test to raise the exception unauthorized session is created
    """
    test_file = BytesIO(b"""{key:"getApiToken",value:function(){return"00000000-0000-0000-0000-000000000000"}""")
    responses.add(responses.POST, "https://localhost:8834/session", json={"token": "EXAMPLE TOKEN"})
    responses.add(responses.GET, "https://localhost:8834/nessus6.js", body=test_file.read())
    test_file.seek(0)

    Nessus(url="https://localhost:8834", username="username", password="password")


def test_invalid_url():
    with pytest.raises(TypeError):
        Nessus(url="://localhost:8834", username="username", password="password")
