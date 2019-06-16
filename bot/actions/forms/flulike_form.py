# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Optional

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction


class FluLikeForm(FormAction):
    """
    Form used to ask necessary questions to categorize patient with flu like
    symptomps.

    Required slots are: others symptoms

    """

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "flulike_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["other_symptoms"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "other_symptoms": [
                self.from_entity(entity="other_symptoms", intent="sintomas_gripais"),
                self.from_intent(intent="negativo", value=False),
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return []
