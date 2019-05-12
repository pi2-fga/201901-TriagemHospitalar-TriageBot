## story_dor_de_cabeca <!--- The name of the story. It is not mandatory, but useful for debugging. -->
  * dor_de_cabeca <!--- User input expressed as intent. In this case it represents users message 'Hello'. -->
   - utter_dor_de_cabeca <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' -->
  * sim
  - utter_outros_sintomas
  * dor_de_cabeça_outros_sintomas

## story_dor_de_cabeca_2 <!--- The name of the story. It is not mandatory, but useful for debugging. -->
  * dor_de_cabeca <!--- User input expressed as intent. In this case it represents users message 'Hello'. -->
   - utter_dor_de_cabeca <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' -->
  * nao
  - utter_outros_sintomas
  * dor_de_cabeça_outros_sintomas
  - utter_escala_de_dor


## usando formulário
  * dados
  - action_complete_triage_form
  - utter_slots_values

<!-- -action_restart restarts bot -->
