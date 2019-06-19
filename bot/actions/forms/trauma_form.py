# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Optional

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction


class TraumaForm(FormAction):
    """
    Form used to ask necessary questions to categorize patient with a headache.

    Required slots are: migrain, pain_scale, pain_persistance, others symptoms

    """

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "trauma_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["cause", "pain_scale", "bleeding"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "pain_scale": self.from_entity(entity="pain_scale", intent="escala_de_dor"),
            "bleeding": [
                self.from_intent(intent="sim", value=True),
                self.from_intent(intent="negativo", value=False),
            ],
            "cause": self.from_entity(entity="cause", intent="causa"),
        }

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_pain_scale(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate pain_scale value."""

        if self.is_int(value) and int(value) > 0:
            return value
        else:
            dispatcher.utter_template("utter_erro_escala_de_dor", tracker)
            # validation failed, set slot to None
            return None

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return []
