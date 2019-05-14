# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Optional

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction


class HeadacheForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "headache_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["migrain", "pain_persistence", "other_symptoms", "pain_scale"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
                "pain_scale": [self.from_entity(entity="pain_scale",
                                                intent="escala_de_dor"),
                               self.from_entity(entity="number")],
                "migrain": [self.from_intent(intent='sim', value=True),
                            self.from_intent(intent='negativo', value=False)],
                "pain_persistance": [(self
                                      .from_entity(entity="pain_persistance",
                                                   intent="persistencia_dor"))
                                     ],
                "other_symptoms": [self.from_intent(intent='outros_sintomas'),
                                   self.from_intent(intent='negativo',
                                                    value=False),
                                   self.from_text()]}

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_pain_scale(self,
                            value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate pain_scale value."""

        if self.is_int(value) and int(value) > 0:
            return value
        else:
            dispatcher.utter_template('utter_erro_escala_de_dor', tracker)
            # validation failed, set slot to None
            return None

    @staticmethod
    def pain_persistance_db():
        # type: () -> List[Text]
        """Database of supported pain persistance"""
        return ["not_constant", "constant"]

    def validate_pain_persistance(self,
                                  value: Text,
                                  dispatcher: CollectingDispatcher,
                                  tracker: Tracker,
                                  domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate pain_persistance value."""

        if value.lower() in self.cuisine_db():
            # validation succeeded
            return value
        else:
            dispatcher.utter_template('utter_erro_persistencia_dor', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return None

    @staticmethod
    def other_symptoms_db():
        # type: () -> List[Text]
        """Database of supported pain persistance"""
        return ["not_constant", "constant"]

    def validate_other_symptoms(self,
                                value: Text,
                                dispatcher: CollectingDispatcher,
                                tracker: Tracker,
                                domain: Dict[Text, Any]) -> Any:
        """Validate other_symptoms value."""

        if isinstance(value, str):
            return value
        else:
            dispatcher.utter_template('utter_erro_outros_sintomas',
                                      tracker)
            # validation failed, set slot to None
            return None

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []
