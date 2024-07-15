from nessus.schema.scans import ScanExportSchema


def test_scan_export_schema():
    schema = ScanExportSchema()
    scan_export = schema.load({"format": "db", "password": "abc", "template_id": 1})
    assert schema.dump(scan_export) == {"format": "db", "password": "abc", "template_id": 1}
    assert schema.dump(schema.load({})) == {"format": "nessus"}
