from schematics.models import Model
from schematics.types import DictType, StringType, ModelType, DateTimeType, ListType, FloatType

__all__ = ['EventModel']


class ResourceModel(Model):
    pod = StringType(serialize_when_none=False)
    alertname = StringType(serialize_when_none=False)
    rule_group = StringType(serialize_when_none=False)
    namespace = StringType(serialize_when_none=False)
    instance = StringType(serialize_when_none=False)
    endpoint = StringType(serialize_when_none=False)
    job = StringType(serialize_when_none=False)
    severity = StringType(serialize_when_none=False)
    prometheus = StringType(serialize_when_none=False)
    service = StringType(serialize_when_none=False)
    container = StringType(serialize_when_none=False)


class EventModel(Model):
    event_key = StringType(required=True)
    event_type = StringType(choices=['RECOVERY', 'ALERT'], default='ALERT')
    title = StringType(required=True)
    description = StringType(default='')
    severity = StringType(choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'NOT_AVAILABLE', 'NONE'], default='NONE')
    resource = ModelType(ResourceModel)
    rule = StringType(default='')
    occurred_at = DateTimeType()
    additional_info = DictType(StringType, default={})
