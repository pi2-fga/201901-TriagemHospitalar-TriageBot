# Triage bot

Um bot api utilizado para categorizar o risco de um paciente de emergência de acordo
com o Protocolo de Manchester.

## Pré requisitos

Para rodar esse projeto os programas docker e docker-compose devem estar previamente instalados.

## Setup e Instalação

Para instalação das dependências do projeto deve-se executar o script build-base.sh, caso precise de permissão root para utilizar o 'docker-compose' deve rodar utilizando sudo:

```
$ sudo ./build-base.sh
```

Depois, basta subir o container do bot para que ele funcione usando:
```
$ sudo docker-compose up bot
```

Em outro terminal, pode ser enviada uma requisição para api do bot:
```sh
curl --request POST \
  --url http://localhost:5005/webhooks/rest/webhook \
  --header 'content-type: application/json' \
  --data '{
    "message": "mensagem"
  }'
```

## Como contribuir

O bot foi implementado usando o Rasa Stack (Rasa Core + Rasa NLU)

### Arquivos para Rasa NLU model

- **data/intents/*.md** arquivos que definem as intents, isto é, o que se espera que o usuário dirá

- **nlu_config.yml** arquivo contém a configuração do pipeline do NLU:
```yaml
language: "pt"

pipeline: spacy_sklearn
```

### Arquivos para Rasa Core model

- **data/stories/*.md** arquivos que tem as histórias para serem treinadas, que são as conversas entre usuário e o bot.
- **domain.yml** arquivo descreve o domínio do bot, que inclue intentes, entities, slots, templates e actions que o bot deve ter consciência.
- **actions.py** onde são declaradas ações realizadas pelo bot que vão além de responder o usuário com texto
- **endpoints.yml** arquivo que contém a configuração do webhook para uma ação personalizada
- **policies.yml** arquivo que contém as políticas de treinamento da model do Rasa core.

## Comandos make
1. You can train the Rasa NLU model by running:
```make train-nlu```
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:
```make train-core```
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. In a new terminal start the server for the custom action by running:
```make action-server```
This will start the server for emulating the custom action.

4. Test the assistant by running:
```make cmdline```
This will load the assistant in your terminal for you to chat.
