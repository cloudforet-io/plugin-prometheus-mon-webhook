import logging
import hashlib
import json
from spaceone.core import utils
from datetime import datetime
from spaceone.core.manager import BaseManager
from spaceone.monitoring.model.event_response_model import EventModel
from spaceone.monitoring.error.event import *
_LOGGER = logging.getLogger(__name__)
_EXCEPTION_TO_PASS = ["Test notification"]


class EventManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse(self, raw_data):

        results = []

        if len(raw_data.get('alerts')) > 0:
            for alert in raw_data['alerts']:
                if alert.get('fingerprint') == '':
                    _LOGGER.error(ERROR_CHECK_FINGERPRINT())

                event_key = self._generate_event_key(alert.get('fingerprint'))
                event_type = self._get_event_type(alert.get('status'))
                severity = self._get_severity(alert.get('labels', {}).get('severity', ''))
                title = alert.get('annotations', {}).get('summary', '')
                description = alert.get('annotations', {}).get('description', '')
                occured_at = alert.get('startsAt', datetime.now())
                rule = alert.get('labels', {}).get('rule_group')
                resource = alert.get('labels')
                additional_info = self._get_additional_info(self, alert)

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

                event_vo = self._check_validity(event_dict)
                results.append(event_vo)
                _LOGGER.debug(f'[EventManager] parse Event : {event_dict}')

        return results

    @staticmethod
    def _check_validity(event_dict):
        try:
            event_result_model = EventModel(event_dict, strict=False)
            event_result_model.validate()
            event_result_model_primitive = event_result_model.to_native()
            return event_result_model_primitive

        except Exception as e:
            raise ERROR_CHECK_VALIDITY(field=e)

    @staticmethod
    def _generate_event_key(fingerprint):
        # Event key generation
        hash_object = hashlib.md5(fingerprint.encode())
        hashed_event_key = hash_object.hexdigest()

        return hashed_event_key

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
    def _get_additional_info(self, alert):
        additional_info = {}
        if 'runbook_url' in alert.get('annotations'):
            additional_info.update({'runbook_url': alert['annotations']['runbook_url']})

        if 'generatorURL' in alert:
            additional_info.update({'generator_url': alert['generatorURL']})

        if 'endsAt' in alert:
            additional_info.update({'ends_at': str(alert['endsAt'])})

        return additional_info
