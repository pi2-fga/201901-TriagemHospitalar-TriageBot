# -*- coding: utf-8 -*-
import ast
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk import Action
from .headache_form import HeadacheForm
from .risk_actions import HeadacheRisk, ChestPainRisk
from .initial_form import InitialForm
from .chestpain_form import ChestPainForm
from .utils import are_vital_signs_normal


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
        message = tracker.latest_message["text"]
        message = message.split("estes são meus sinais vitais ", 1)[1]
        slot_keys_values = ast.literal_eval(message)
        slots = []

        for key in slot_keys_values.keys():
            slot = SlotSet(key, slot_keys_values[key])
            slots.append(slot)
        return slots


class EletrocardiogramNeed(Action):
    """
    This action checks if patient needs to perfom an eletrocardiogram

    """

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "action_eletrocardiogram_check"

    def run(self, dispatcher, tracker, domain):
        """
        Gets user entry and registers slots there are in it
        """
        age = tracker.get_slot("age")
        pressure = tracker.get_slot("blood_pressure")
        oxygen_level = tracker.get_slot("blood_oxygen_level")
        temperature = tracker.get_slot("body_temperature")
        vitals = are_vital_signs_normal(pressure, oxygen_level, temperature)
        if int(age) >= 60 and vitals:
            dispatcher.utter_template("utter_eletrocardiograma", tracker)
        else:
            dispatcher.utter_template("utter_sinal", tracker)
        return []
