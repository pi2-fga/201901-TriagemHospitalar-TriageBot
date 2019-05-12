# -*- coding: utf-8 -*-
import ast
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk import Action


class TriageForm(Action):
    """Triage custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "action_complete_triage_form"

    def run(self, dispatcher, tracker, domain):
        """
        Gets user entry and registers slots there are in it
        """
        message = tracker.latest_message.text
        message = message.split("estes são meus dados: ", 1)[1]
        slot_keys_values = ast.literal_eval(message)
        slots = None
        print(message)
        for key in slot_keys_values.keys():
            slot = SlotSet(key, slot_keys_values[key])
            slots.append(slot)
            print(slot)
        return slots
