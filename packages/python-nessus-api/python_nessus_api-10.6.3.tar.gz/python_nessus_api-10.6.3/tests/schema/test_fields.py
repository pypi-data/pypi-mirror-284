from marshmallow import Schema, fields

from nessus.schema.fields import BaseField, LowerCase, UpperCase


def test_base_field():

    class BaseFieldSchema(Schema):
        test_field = BaseField(fields.Str())

    test = {"test_field": "name"}
    schema = BaseFieldSchema()
    assert schema.dump(schema.load(test)) == test


def test_lower_case():

    class LowerCaseSchema(Schema):
        test_field = LowerCase(fields.Str())

    test = {"test_field": "Name"}
    schema = LowerCaseSchema()
    assert schema.dump(schema.load(test)) == {"test_field": "name"}


def test_upper_case():

    class UpperCaseSchema(Schema):
        test_field = UpperCase(fields.Str())

    test = {"test_field": "name"}
    schema = UpperCaseSchema()
    assert schema.dump(schema.load(test)) == {"test_field": "NAME"}
