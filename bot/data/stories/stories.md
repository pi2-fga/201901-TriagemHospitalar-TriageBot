## story usando formulário de dados básicos
  * dados
  - action_complete_triage_form
  - utter_slots_values


## story dor de cabeça, categorização de risco
  * dor_de_cabeca
    - initial_form
    - form{"name": "initial_form"}
    - form{"name": null}
    - headache_form
    - form{"name": "headache_form"}
    - form{"name": null}
    - utter_medicao
    * dados
    - action_complete_triage_form
    - utter_slots_values
    * dados_recebidos
    - action_headache_risk
    - action_restart <!-- -action_restart restarts bot, cleaning slots -->

## story dor abdominal, categorização de risco
  * dor_abdomen
    - initial_form
    - form{"name": "initial_form"}
    - form{"name": null}
    - abdominalpain_form
    - form{"name": "abdominalpain_form"}
    - form{"name": null}
    - utter_medicao
    * dados
    - action_complete_triage_form
    - utter_slots_values
    * dados_recebidos
    - action_abdominal_pain_risk
    - action_restart <!-- -action_restart restarts bot, cleaning slots -->

## story dor no torax
  * dor_torax
    - initial_form
    - form{"name": "initial_form"}
    - form{"name": null}
    - chestpain_form
    - form{"name": "chestpain_form"}
    - form{"name": null}
    - utter_slots_values
    * dados_recebidos
    - utter_medicao
    * dados
    - action_complete_triage_form
    - action_eletrocardiogram_check
    * dados_recebidos
    - action_chestpain_risk
    - action_restart <!-- -action_restart restarts bot, cleaning slots -->

## story sintomas gripais, categorização de risco
  * sintomas_gripais
    - initial_form
    - form{"name": "initial_form"}
    - form{"name": null}
    - flulike_form
    - form{"name": "flulike_form"}
    - form{"name": null}
    - utter_medicao
    * dados
    - action_complete_triage_form
    - utter_slots_values
    * dados_recebidos
    - action_flu_like_risk
    - action_restart <!-- -action_restart restarts bot, cleaning slots -->

## story trauma, categorização de risco
  * trauma
    - initial_form
    - form{"name": "initial_form"}
    - form{"name": null}
    - trauma_form
    - form{"name": "trauma_form"}
    - form{"name": null}
    - utter_medicao
    * dados
    - action_complete_triage_form
    - utter_slots_values
    * dados_recebidos
    - action_trauma_risk
    - action_restart <!-- -action_restart restarts bot, cleaning slots -->

## story intoxicação exógena ou tentativa de suicídio
  * intoxicacao
    - utter_risco_vermelho
    - action_restart <!-- -action_restart restarts bot, cleaning slots -->
