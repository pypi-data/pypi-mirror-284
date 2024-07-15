import responses


@responses.activate
def test_session_get(nessus):
    responses.add(
        responses.GET,
        "https://localhost:8834/session",
        json={
            "id": "abcdef",
            "username": "admin",
            "email": "admin@something.com",
            "name": "Admin User",
        },
    )
    resp = nessus.session.get()
    assert resp["id"] == "abcdef"
    assert resp["name"] == "Admin User"


@responses.activate
def test_session_chpasswd(nessus):
    responses.add(responses.PUT, "https://localhost:8834/session/chpasswd")
    nessus.session.chpasswd("old_pass", "new_pass")


@responses.activate
def test_session_api_keys(nessus):
    responses.add(
        responses.PUT, "https://localhost:8834/session/keys", json={"accessKey": "abcdef", "secretKey": "abcdef"}
    )
    keys = nessus.session.api_keys()
    assert keys["accessKey"] == "abcdef"
    assert keys["secretKey"] == "abcdef"


@responses.activate
def test_session_edit(nessus):
    responses.add(
        responses.PUT,
        "https://localhost:8834/session",
    )
    nessus.session.edit(name="User", email="email@user.com")


@responses.activate
def test_session_destroy(nessus):
    responses.add(
        responses.DELETE,
        "https://localhost:8834/session",
    )
    nessus.session.destroy()
