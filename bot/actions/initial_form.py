# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Optional

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction


class InitialForm(FormAction):
    """
    Form used to ask necessary initial questions, no matter what pacient
    is feeling.

    Required slots are: age, continuous_medication and alergies.
    """

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "initial_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["age", "continuous_medication", "alergies"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "age": self.from_entity(entity="age", intent="idade"),
            "continuous_medication": [
                self.from_intent(intent="negativo", value=False),
                self.from_entity(entity="continuous_medication", intent="medicacao"),
            ],
            "alergies": [
                self.from_intent(intent="negativo", value=False),
                self.from_entity(entity="alergies", intent="alergias"),
            ],
        }

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_age(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate pain_scale value."""

        if self.is_int(value) and int(value) >= 0:
            return value
        else:
            dispatcher.utter_template("utter_erro_idade", tracker)
            return None

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        age = tracker.get_slot("age")
        continuous_medication = tracker.get_slot("continuous_medication")
        alergies = tracker.get_slot("alergies")
        elements = f"data {'age': {age}, 'continuos_medication': {continuous_medication}, 'alergies': {alergies}}"
        dispatcher.utter_custom_message(elements, tracker)
        return []
