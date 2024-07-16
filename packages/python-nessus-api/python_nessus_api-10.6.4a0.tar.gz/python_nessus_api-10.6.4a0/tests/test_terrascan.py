import responses

TERRASCAN_INFO = {
    "installed": True,
    "path": "/path/file",
    "status": "string",
    "terrascan_desired": True,
    "version": "string",
}


@responses.activate
def test_terrascan_get_info(nessus):
    responses.add(responses.GET, "https://localhost:8834/tools/terrascan", json=TERRASCAN_INFO)
    resp = nessus.terrascan.get_info()
    assert resp == TERRASCAN_INFO


@responses.activate
def test_terrascan_set_desired(nessus):
    responses.add(responses.POST, "https://localhost:8834/tools/terrascan")
    resp = nessus.terrascan.set_desired(terrascan=True)
    assert resp is None


@responses.activate
def test_terrascan_download(nessus):
    responses.add(responses.POST, "https://localhost:8834/tools/terrascan/download")
    resp = nessus.terrascan.download()
    assert resp is None


@responses.activate
def test_terrascan_get_config(nessus):
    responses.add(responses.GET, "https://localhost:8834/tools/terrascan/configs/1", json=TERRASCAN_INFO)
    resp = nessus.terrascan.get_config(1)
    assert resp == TERRASCAN_INFO


@responses.activate
def test_terrascan_save_config(nessus):
    responses.add(responses.POST, "https://localhost:8834/tools/terrascan/configs")
    resp = nessus.terrascan.save_config({}, "name", 12)
    assert resp is None


@responses.activate
def test_terrascan_delete_config(nessus):
    responses.add(responses.DELETE, "https://localhost:8834/tools/terrascan/configs/1")
    resp = nessus.terrascan.delete_config(1)
    assert resp is None


@responses.activate
def test_terrascan_edit_config(nessus):
    responses.add(responses.PUT, "https://localhost:8834/tools/terrascan/configs/1")
    resp = nessus.terrascan.edit_config(1)
    assert resp is None


@responses.activate
def test_terrascan_get_configs(nessus):
    responses.add(responses.GET, "https://localhost:8834/tools/terrascan/configs")
    resp = nessus.terrascan.get_configs()
    assert resp is None


@responses.activate
def test_terrascan_delete_configs(nessus):
    responses.add(responses.DELETE, "https://localhost:8834/tools/terrascan/configs/1")
    resp = nessus.terrascan.delete_configs(1)
    assert resp is None


@responses.activate
def test_terrascan_get_default_config(nessus):
    responses.add(responses.GET, "https://localhost:8834/tools/terrascan/configs/default", json=TERRASCAN_INFO)
    resp = nessus.terrascan.get_default_config()
    assert resp == TERRASCAN_INFO


@responses.activate
def test_terrascan_get_scans(nessus):
    responses.add(responses.GET, "https://localhost:8834/tools/terrascan/scans/1")
    resp = nessus.terrascan.get_scans(1)
    assert resp is None


@responses.activate
def test_terrascan_launch_scan(nessus):
    responses.add(responses.POST, "https://localhost:8834/tools/terrascan/scans/1")
    resp = nessus.terrascan.launch_scan(1)
    assert resp is None


@responses.activate
def test_terrascan_delete_scan(nessus):
    responses.add(responses.DELETE, "https://localhost:8834/tools/terrascan/scan?scan_ids=1&scan_ids=2")
    resp = nessus.terrascan.delete_scan([1, 2])
    assert resp is None


@responses.activate
def test_terrascan_download_scan_result(nessus):
    responses.add(responses.GET, "https://localhost:8834/tools/terrascan/scan/results/1/1/pdf")
    resp = nessus.terrascan.download_scan_result(1, 1, "pdf")
    assert resp is None


@responses.activate
def test_terrascan_dowload_scan_result_command_output(nessus):
    responses.add(responses.GET, "https://localhost:8834/tools/terrascan/scan/command_output/1/1")
    resp = nessus.terrascan.dowload_scan_result_command_output(1, 1)
    assert resp is None
