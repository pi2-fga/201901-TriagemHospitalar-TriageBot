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
        return ["nausea",
                "naúsea",
                "enjoo",
                "ânsia",
                "ansia",
                "dor no pescoço",
                "estou enjoado",
                "estou com tontura",
                "estou enjoada"]

    def run(self, dispatcher, tracker, domain):
        """
        Gets user entry and registers slots there are in it
        """
        pain_scale = tracker.get_slot('pain_scale')
        migrain = tracker.get_slot('migrain')
        if int(pain_scale) > 7 and not migrain:
            dispatcher.utter_template('utter_risco_amarelo', tracker)
        else:
            dispatcher.utter_template('utter_risco_verde', tracker)
        return []
