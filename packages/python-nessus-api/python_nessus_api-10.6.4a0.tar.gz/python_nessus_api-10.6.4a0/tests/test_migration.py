import responses

MIGRATION_SETTING = {
    "status": "not started",
    "port": "443",
    "linkingKey": "dc5c8817266e0bcfcf93501c45baa1832c2cb50a32bb10d02998f850f066bfd5",
    "domain": "tenable.com",
    "host": "cloud.tenable.com",
    "name": "test migration",
}

MIGRATION_STATUS = {
    "transient": 0,
    "critical": 0,
    "current": "Migrating local scanner",
    "error": "",
    "progress": 90,
    "status": "started",
}

MIGRATION_SCAN_HISTORY = {
    "totalCount": 5,
    "totalBytes": 54493184,
    "uploadedCount": 1,
    "uploadedBytes": 216064,
    "skippedCount": 1,
    "skippedBytes": 215040,
    "uploadCount": 3,
    "uploadBytes": 54062080,
    "uploadingStopped": False,
    "items": [
        {
            "upload_status": "",
            "bytes": 215040,
            "last_modification_date": 1542402549,
            "name": "test host discovery",
            "uuid": "f4a44006-c5e8-45cf-2188-64f79d44c2c5ea86524cdfcdb528",
            "message": "",
            "status": "skipped",
            "id": 8,
        },
        {
            "upload_status": "",
            "bytes": 216064,
            "last_modification_date": 1542307330,
            "name": "test host discovery",
            "uuid": "5b7b023a-7d1d-9d2d-e639-a85de5b8683f3629dc7afbcb64af",
            "message": "",
            "status": "finished",
            "id": 9,
        },
        {
            "upload_status": "",
            "bytes": 17881088,
            "last_modification_date": 1542137211,
            "owner": "admin",
            "name": "test advanced scan",
            "uuid": "cea9e002-dc9b-6247-67e6-e092c92c72f94f75a5c95e8d6674",
            "message": "",
            "status": "not started",
            "id": 10,
        },
    ],
}

MIGRATION_SCAN_HISTORY_SETTING = {
    "days_of_history": 10,
    "concurrent_uploads": 1,
    "seconds_to_sleep_between_each_upload": 5,
}


@responses.activate
def test_migration_get_settings(nessus):
    responses.add(responses.GET, "https://localhost:8834/migration/config", json=MIGRATION_SETTING)
    resp = nessus.migration.get_settings()
    assert resp == MIGRATION_SETTING


@responses.activate
def test_migration_update_settings(nessus):
    responses.add(responses.PUT, "https://localhost:8834/migration/config")
    resp = nessus.migration.update_settings(key="", secret="", domain="")
    assert resp is None


@responses.activate
def test_migration_status(nessus):
    responses.add(responses.GET, "https://localhost:8834/migration", json=MIGRATION_STATUS)
    resp = nessus.migration.status()
    assert resp == MIGRATION_STATUS


@responses.activate
def test_migration_start(nessus):
    responses.add(responses.POST, "https://localhost:8834/migration")
    resp = nessus.migration.start()
    assert resp is None


@responses.activate
def test_migration_stop(nessus):
    responses.add(responses.DELETE, "https://localhost:8834/migration")
    resp = nessus.migration.stop(finish=True)
    assert resp is None


@responses.activate
def test_migration_scan_history(nessus):
    responses.add(responses.GET, "https://localhost:8834/migration/scan-history", json=MIGRATION_SCAN_HISTORY)
    resp = nessus.migration.scan_history(updated_after=1201840128)
    assert resp == MIGRATION_SCAN_HISTORY


@responses.activate
def test_migration_scan_history_settings(nessus):
    responses.add(
        responses.GET,
        "https://localhost:8834/migration/scan-history/upload-settings",
        json=MIGRATION_SCAN_HISTORY_SETTING,
    )
    resp = nessus.migration.scan_history_settings()
    assert resp == MIGRATION_SCAN_HISTORY_SETTING


@responses.activate
def test_migration_update_scan_history_settings(nessus):
    responses.add(responses.POST, "https://localhost:8834/migration/scan-history/upload-settings")
    resp = nessus.migration.update_scan_history_settings(
        days_of_history=10, seconds_to_sleep_between_each_upload=0, concurrent_uploads=1
    )
    assert resp is None


@responses.activate
def test_migration_start_scan_history_migration(nessus):
    responses.add(responses.POST, "https://localhost:8834/migration/scan-history/start-upload")
    resp = nessus.migration.start_scan_history_migration()
    assert resp is None


@responses.activate
def test_migration_stop_scan_history_migration(nessus):
    responses.add(responses.POST, "https://localhost:8834/migration/scan-history/stop-upload")
    resp = nessus.migration.stop_scan_history_migration()
    assert resp is None


@responses.activate
def test_migration_skip_scan_history(nessus):
    responses.add(responses.POST, "https://localhost:8834/migration/scan-history/1/skip-upload")
    resp = nessus.migration.skip_scan_history("1")
    assert resp is None


@responses.activate
def test_migration_skip_scan_history_bulk(nessus):
    responses.add(responses.POST, "https://localhost:8834/migration/scan-history/skip-upload?ids=1&ids=2")
    resp = nessus.migration.skip_scan_history_bulk(["1", "2"])
    assert resp is None


@responses.activate
def test_migration_reset_scan_history(nessus):
    responses.add(responses.POST, "https://localhost:8834/migration/scan-history/1/start-upload")
    resp = nessus.migration.reset_scan_history("1")
    assert resp is None


@responses.activate
def test_migration_reset_scan_history_bulk(nessus):
    responses.add(responses.POST, "https://localhost:8834/migration/scan-history/start-upload?ids=1&ids=2")
    resp = nessus.migration.reset_scan_history_bulk(["1", "2"])
    assert resp is None
