from rasa_core_sdk import Action
from .utils import are_vital_signs_normal


class HeadacheRisk(Action):
    """Sets pacient risk according to headache symptoms"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "action_headache_risk"

    @staticmethod
    def other_symptoms_db():
        # type: () -> List[Text]
        return [
            "nausea",
            "naúsea",
            "enjoo",
            "ânsia",
            "ansia",
            "dor no pescoço",
            "estou enjoado",
            "estou com tontura",
            "estou enjoada",
            "dor na nuca",
        ]

    def run(self, dispatcher, tracker, domain):
        """
        Uses slot values to set user risk
        """
        pain_scale = tracker.get_slot("pain_scale")
        migrain = tracker.get_slot("migrain")
        pain_persistance = tracker.get_slot("pain_persistance")
        other_symptoms = tracker.get_slot("other_symptoms")
        has_other_symptoms = other_symptoms in self.other_symptoms_db()
        is_pain_scale_high = int(pain_scale) > 7

        pressure = tracker.get_slot("blood_pressure")
        oxygen_level = tracker.get_slot("blood_oxygen_level")
        temperature = tracker.get_slot("body_temperature")
        vitals = are_vital_signs_normal(pressure, oxygen_level, temperature)

        if (is_pain_scale_high and not migrain and has_other_symptoms) or (
            (is_pain_scale_high and (pain_persistance is "constant")) or not vitals
        ):
            dispatcher.utter_template("utter_risco_amarelo", tracker)
        else:
            dispatcher.utter_template("utter_risco_verde", tracker)
        return []


class ChestPainRisk(Action):
    """Sets pacient risk according to chestpain symptoms"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "action_chestpain_risk"

    def run(self, dispatcher, tracker, domain):
        """
        Uses slot values to set user risk
        """
        infarction = tracker.get_slot("infarction")
        diabetes = tracker.get_slot("diabetes")
        pain_scale = tracker.get_slot("pain_scale")
        pain_persistance = tracker.get_slot("pain_persistance")
        age = int(tracker.get_slot("age")) > 60
        is_pain_scale_high = int(pain_scale) > 7

        pressure = tracker.get_slot("blood_pressure")
        oxygen_level = tracker.get_slot("blood_oxygen_level")
        temperature = tracker.get_slot("body_temperature")
        vitals = are_vital_signs_normal(pressure, oxygen_level, temperature)

        if (is_pain_scale_high and (infarction or diabetes or age)) or (
            (is_pain_scale_high and (pain_persistance is "constant")) or not vitals
        ):
            dispatcher.utter_template("utter_risco_vermelho", tracker)
        else:
            dispatcher.utter_template("utter_risco_amarelo", tracker)
        return []


class AbdominalPainRisk(Action):
    """Sets pacient risk according to abdominal pain symptoms"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "action_abdominal_pain_risk"

    @staticmethod
    def other_symptoms_db():
        # type: () -> List[Text]
        return [
            "nausea",
            "naúsea",
            "enjoo",
            "ânsia",
            "ansia",
            "dor no pescoço",
            "estou enjoado",
            "estou com tontura",
            "estou enjoada",
            "dor na nuca",
            "suor",
            "diarréia",
            "diarreia",
            "vômito",
            "vomitando",
            "inchaço",
            "inchado",
            "irradiação",
        ]

    @staticmethod
    def prostacao_db():
        # type: () -> List[Text]
        return ["cansaço", "prostração", "prostrado", "prostrada", "cansado", "cansada"]

    def run(self, dispatcher, tracker, domain):
        """
        Uses slot values to set user risk
        """
        pain_scale = tracker.get_slot("pain_scale")
        pain_persistance = tracker.get_slot("pain_persistance")
        other_symptoms = tracker.get_slot("other_symptoms")
        age = tracker.get_slot("age")
        pregnancy = tracker.get_slot("pregnancy")

        has_other_symptoms = other_symptoms in self.other_symptoms_db()
        is_pain_scale_high = int(pain_scale) > 7
        pressure = tracker.get_slot("blood_pressure")
        oxygen_level = tracker.get_slot("blood_oxygen_level")
        temperature = tracker.get_slot("body_temperature")
        vitals = are_vital_signs_normal(pressure, oxygen_level, temperature)

        if (is_pain_scale_high and has_other_symptoms) or (
            (is_pain_scale_high and (pain_persistance is "constant"))
            or not vitals
            or pregnancy
        ):
            dispatcher.utter_template("utter_risco_vermelho", tracker)
        elif (vitals and age > 60) or (
            (other_symptoms in self.prostacao_db()) and int(pain_scale) > 3
        ):
            dispatcher.utter_template("utter_risco_amarelo", tracker)
        else:
            dispatcher.utter_template("utter_risco_verde", tracker)
        return []


class FluLikeRisk(Action):
    """Sets pacient risk according to abdominal pain symptoms"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "action_flu_like_risk"

    def run(self, dispatcher, tracker, domain):
        """
        Uses slot values to set user risk
        """
        age = tracker.get_slot("age")

        pressure = tracker.get_slot("blood_pressure")
        oxygen_level = tracker.get_slot("blood_oxygen_level")
        temperature = tracker.get_slot("body_temperature")
        vitals = are_vital_signs_normal(pressure, oxygen_level, temperature)

        if not vitals or int(age) >= 60:
            dispatcher.utter_template("utter_risco_verde", tracker)
        else:
            dispatcher.utter_template("utter_risco_azul", tracker)
        return []


class TraumaRisk(Action):
    """Sets pacient risk according to headache symptoms"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "action_trauma_risk"

    @staticmethod
    def body_part_db():
        # type: () -> List[Text]
        return ["cabeça", "estômago", "barriga"]

    def run(self, dispatcher, tracker, domain):
        """
        Uses slot values to set user risk
        """
        pain_scale = tracker.get_slot("pain_scale")
        body_part = tracker.get_slot("body_part")
        cause = tracker.get_slot("cause")
        bleeding = tracker.get_slot("bleeding")
        is_pain_scale_high = int(pain_scale) > 7

        pressure = tracker.get_slot("blood_pressure")
        oxygen_level = tracker.get_slot("blood_oxygen_level")
        temperature = tracker.get_slot("body_temperature")
        vitals = are_vital_signs_normal(pressure, oxygen_level, temperature)

        if (
            is_pain_scale_high
            or (body_part in self.body_part_db())
            or bleeding
            or not vitals
        ):
            dispatcher.utter_template("utter_risco_amarelo", tracker)
        elif int(pain_scale) > 3:
            dispatcher.utter_template("utter_risco_verde", tracker)
        else:
            dispatcher.utter_template("utter_risco_azul", tracker)
        return []
