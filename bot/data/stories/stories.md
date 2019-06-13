## story usando formulário de dados básicos
  * dados
  - action_complete_triage_form
  - utter_slots_values


## story dor de cabeça, categorização de risco de usuário de cadeira de rodas
* dor_de_cabeca
  - initial_form
  - form{"name": "initial_form"}
  - form{"name": null}
  - headache_form
  - form{"name": "headache_form"}
  - form{"name": null}
  - utter_cadeira_de_rodas
  * sim
  - utter_medicao_pressao
  * dados
  - action_complete_triage_form
  - utter_medicao_temperatura_oximetro
  * dados
  - action_complete_triage_form
  - utter_slots_values
  * dados_recebidos
  - action_headache_risk
  - action_restart <!-- -action_restart restarts bot, cleaning slots -->


## story dor de cabeça, categorização de risco de não usuário de cadeira de rodas
  * dor_de_cabeca
    - initial_form
    - form{"name": "initial_form"}
    - form{"name": null}
    - headache_form
    - form{"name": "headache_form"}
    - form{"name": null}
    - utter_cadeira_de_rodas
    * negativo
    - utter_medicao_temperatura_oximetro
    * dados
    - action_complete_triage_form
    - utter_medicao_pressao
    * dados
    - action_complete_triage_form
    - utter_medicao_peso_altura
    * dados
    - action_complete_triage_form
    - utter_slots_values
    * dados_recebidos
    - action_headache_risk
    - action_restart <!-- -action_restart restarts bot, cleaning slots -->


## story intoxicação exógena ou tentativa de suicídio
  * intoxicacao
    - utter_risco_vermelho
    - action_restart <!-- -action_restart restarts bot, cleaning slots -->
