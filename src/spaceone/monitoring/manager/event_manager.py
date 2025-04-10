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

        if len(raw_data.get("alerts", [])) > 0:
            for alert in raw_data.get("alerts", []):
                if alert.get("fingerprint") == "":
                    _LOGGER.error(ERROR_CHECK_FINGERPRINT())

                labels = alert.get("labels", {})
                annotations = alert.get("annotations", {})

                event_key = alert["fingerprint"]
                event_type = self._get_event_type(alert.get("status"))
                severity = self._get_severity(labels.get("severity", ""))
                title = self._get_title(labels, annotations)
                description = annotations.get("description", "no description")
                occurred_at = alert.get("startsAt", str(datetime.utcnow()))
                rule = labels.get("rule_group")
                resource = self._get_resource_info(self, labels)
                additional_info = self._get_additional_info(alert)

                event_dict = {
                    "event_key": event_key,
                    "event_type": event_type,
                    "severity": severity,
                    "title": title,
                    "rule": rule,
                    "resource": resource,
                    "description": description,
                    "occurred_at": occurred_at,
                    "additional_info": additional_info,
                }

                event_vo = self._validate_parsed_event(event_dict)
                event_vo["occurred_at"] = utils.iso8601_to_datetime(
                    event_vo["occurred_at"]
                )
                results.append(event_vo)
                _LOGGER.debug(f"[EventManager: parse] : {event_dict}")

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
    def _get_title(labels, annotations):
        return annotations.get("summary") or labels.get("alertname") or "no title"

    @staticmethod
    def _get_event_type(status):
        return "RECOVERY" if status == "resolved" else "ALERT"

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
        if severity == "critical":
            severity_flag = "CRITICAL"
        elif severity == "error":
            severity_flag = "ERROR"
        elif severity == "warning":
            severity_flag = "WARNING"
        else:
            severity_flag = "INFO"

        return severity_flag

    @staticmethod
    def _get_additional_info(alert):
        additional_info = {}
        if "runbook_url" in alert.get("annotations", {}):
            additional_info.update({"runbook_url": alert["annotations"]["runbook_url"]})

        if "generatorURL" in alert:
            additional_info.update({"generator_url": alert["generatorURL"]})

        if "endsAt" in alert:
            additional_info.update({"ends_at": str(alert["endsAt"])})

        if "labels" in alert:
            for label in alert["labels"]:
                additional_info.update({label: alert["labels"][label]})

        return additional_info

    @staticmethod
    def _get_resource_info(self, labels):
        resource_info = {}
        resource_type, name = self._get_representative_resource(labels)

        resource_info.update({"resource_type": resource_type, "name": name})

        return resource_info

    @staticmethod
    def _get_representative_resource(labels):
        # Select the most specific resource type based on the priority order in 'monitoring_target_resources'
        monitoring_target_resources = [
            "resource",
            "grpc_method",
            "instance",
            "pod",
            "container",
            "device",
            "persistentvolumeclaim",
            "persistentvolume",
            "deployment",
            "daemonset",
            "statefulset",
            "horizontalpodautoscaler",
            "service",
            "controller",
            "job",
            "namespace",
            "phase",
            "severity",
            "alertname",
            "prometheus",
        ]

        resource_type = None
        resource_name = None
        min_index = float("inf")  # Lower index means higher priority

        for label, value in labels.items():
            if label in monitoring_target_resources:
                label_index = monitoring_target_resources.index(label)

                if (
                    label_index < min_index
                ):  # Select the resource with the highest priority (lowest index)
                    min_index = label_index
                    resource_type = label
                    resource_name = value

        return resource_type, resource_name
