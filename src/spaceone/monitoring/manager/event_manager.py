import logging
from spaceone.core import utils
from datetime import datetime
from spaceone.core.manager import BaseManager
from spaceone.monitoring.model.event_response_model import EventModel
from spaceone.monitoring.error.event import *
_LOGGER = logging.getLogger(__name__)


class EventManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse(self, raw_data):

        results = []

        if len(raw_data.get('alerts', [])) > 0:
            for alert in raw_data.get('alerts', []):
                if alert.get('fingerprint') == '':
                    _LOGGER.error(ERROR_CHECK_FINGERPRINT())

                event_key = alert['fingerprint']
                event_type = self._get_event_type(alert.get('status'))
                severity = self._get_severity(alert.get('labels', {}).get('severity', ''))
                title = alert.get('annotations', {}).get('summary', 'no title')
                description = alert.get('annotations', {}).get('description', 'no description')
                occured_at = alert.get('startsAt', datetime.now())
                rule = alert.get('labels', {}).get('rule_group')
                resource = self._get_resource_info(self, alert.get('labels'))
                additional_info = self._get_additional_info(alert)

                event_dict = {
                    'event_key': event_key,
                    'event_type': event_type,
                    'severity': severity,
                    'title': title,
                    'rule': rule,
                    'resource': resource,
                    'description': description,
                    'occurred_at': occured_at,
                    'additional_info': additional_info
                }

                event_vo = self._validate_parsed_event(event_dict)
                results.append(event_vo)
                _LOGGER.debug(f'[EventManager: parse] : {event_dict}')

        return results

    @staticmethod
    def _validate_parsed_event(event_dict):
        try:
            event_result_model = EventModel(event_dict, strict=False)
            event_result_model.validate()
            event_result_model_primitive = event_result_model.to_native()
            return event_result_model_primitive

        except Exception as e:
            raise ERROR_CHECK_VALIDITY(field=e)

    @staticmethod
    def _get_event_type(status):
        return 'RECOVERY' if status == 'resolved' else 'ALERT'

    @staticmethod
    def _get_severity(severity):
        """
        critical : CRITICAL
        error : ERROR
        warning : WARNING
        info: INFO

        CRITICAL | ERROR | WARNING | INFO | NOT_AVAILABLE | NONE(default)
        (critical : CRITICAL / error : ERROR / warning: WARNING / info: INFO)

        ------
        """
        severity_flag = 'NONE'
        if severity == 'critical':
            severity_flag = 'CRITICAL'
        elif severity == 'error':
            severity_flag = 'ERROR'
        elif severity == 'warning':
            severity_flag = 'WARNING'
        elif severity == 'info':
            severity_flag = 'INFO'

        return severity_flag

    @staticmethod
    def _get_additional_info(alert):
        additional_info = {}
        if 'runbook_url' in alert.get('annotations'):
            additional_info.update({'runbook_url': alert['annotations']['runbook_url']})

        if 'generatorURL' in alert:
            additional_info.update({'generator_url': alert['generatorURL']})

        if 'endsAt' in alert:
            additional_info.update({'ends_at': str(alert['endsAt'])})

        if 'labels' in alert:
            for label in alert['labels']:
                additional_info.update({
                    label: alert['labels'][label]
                })

        return additional_info

    @staticmethod
    def _get_resource_info(self, labels):
        resource_info = {}
        resource_type, name = self._get_representative_resource(labels)

        resource_info.update({
            'resource_type': resource_type,
            'name': name
        })

        return resource_info

    @staticmethod
    def _get_representative_resource(labels):
        # Since labels selectively have information about resources, parse resource info from the label keys if 'monitoring_target_resources' has.

        resource_type = ''
        resource_name = ''
        monitoring_target_resources = ['prometheus', 'job', 'grpc_method', 'job_name', 'horizontalpodautoscaler',
                                       'phase', 'device', 'controller', 'persistentvolume', 'persistentvolumeclaim',
                                       'resource', 'daemonset', 'statefulset', 'instance', 'service', 'namespace',
                                       'deployment', 'container', 'node', 'pod']

        max_index = 0
        for label in labels:
            if label in monitoring_target_resources:
                label_index = monitoring_target_resources.index(label)

                if label_index > max_index:
                    max_index = label_index
                    resource_type = label
                    resource_name = labels[label]

        return resource_type, resource_name

