"""
Extended field definitions
"""

from __future__ import annotations

from marshmallow import fields


class BaseField(fields.Field):
    """
    BaseField Field
    """

    def __init__(self, inner, *args, **kwargs):
        self.inner = inner
        super().__init__(*args, **kwargs)

    def _bind_to_schema(self, field_name, parent):
        super()._bind_to_schema(field_name, parent)
        self.inner._bind_to_schema(field_name, parent)

    def _deserialize(self, value, *args, **kwargs):
        return self.inner._deserialize(value, *args, **kwargs)

    def _serialize(self, *args, **kwargs):
        return self.inner._serialize(*args, **kwargs)


class LowerCase(BaseField):
    """
    The field value will be lower-cased with this field.
    """

    def _deserialize(self, value, *args, **kwargs):
        if hasattr(value, "lower"):  # pragma: no branch
            value = value.lower()
        return super()._deserialize(value, *args, **kwargs)


class UpperCase(BaseField):
    """
    The field value will be upper-cased with this field.
    """

    def _deserialize(self, value, *args, **kwargs):
        if hasattr(value, "upper"):  # pragma: no branch
            value = value.upper()
        return super()._deserialize(value, *args, **kwargs)
