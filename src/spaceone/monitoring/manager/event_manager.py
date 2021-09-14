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
    def _change_eval_dict_to_str(eval_matches_dict):
        try:
            eval_matches_str = json.dumps(eval_matches_dict)
            return eval_matches_str

        except Exception as e:
            raise ERROR_CONVERT_DATA_TYPE(field=e)
