from rasa_core_sdk import Action


class HeadacheRisk(Action):
    """Sets pacient risk according to headache symptoms"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "action_headache_risk"

    @staticmethod
    def other_symptoms_db():
        # type: () -> List[Text]
        """Database of supported cuisines"""
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

        if (is_pain_scale_high and not migrain and has_other_symptoms) or (
            is_pain_scale_high and pain_persistance is "constant"
        ):
            dispatcher.utter_template("utter_risco_amarelo", tracker)
        else:
            dispatcher.utter_template("utter_risco_verde", tracker)
        return []
