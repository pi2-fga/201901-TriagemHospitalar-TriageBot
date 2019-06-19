# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Optional

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction


class AbdominalPainForm(FormAction):
    """
    Form used to ask necessary questions to categorize patient with a headache.

    Required slots are: migrain, pain_scale, pain_persistance, others symptoms

    """

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "abdominalpain_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["pregnancy", "pain_scale", "pain_persistance", "other_symptoms"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "pain_scale": self.from_entity(entity="pain_scale", intent="escala_de_dor"),
            "pregnancy": [
                self.from_intent(intent="sim", value=True),
                self.from_intent(intent="negativo", value=False),
            ],
            "other_symptoms": [
                self.from_entity(entity="other_symptoms", intent="outros_sintomas"),
                self.from_intent(intent="negativo", value=False),
                self.from_text(),
            ],
            "pain_persistance": self.from_entity(
                entity="pain_persistance", intent="persistencia_dor"
            ),
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

    @staticmethod
    def pain_persistance_db():
        # type: () -> List[Text]
        """Database of supported pain persistance"""
        return ["not_constant", "constant"]

    def validate_pain_persistance(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Any:
        """Validate other_symptoms value."""
        if value in self.pain_persistance_db():
            return value
        else:
            dispatcher.utter_template("utter_erro_persistencia_dor", tracker)
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
