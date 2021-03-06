# Triage bot

Um bot api utilizado para categorizar o risco de um paciente de emergência de acordo
com o Protocolo de Manchester.

## Pré requisitos

Para rodar esse projeto os programas docker e docker-compose devem estar previamente instalados.

## Setup e Instalação

Para instalação das dependências do projeto deve-se executar o script build-base.sh,
caso precise de permissão root para utilizar o 'docker-compose' deve rodar utilizando sudo:

```
$ sudo ./build-base.sh
```

Além disso, rode o comando train e up do trainer para treinar o bot:

```
$ sudo make train
$ sudo docker-compose up trainer
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
1. Você pode treinar uma model do Rasa NLU rodando:
```make train-nlu```
Isso vai treinar as models e armazenar `/models/current/nlu` dentro da pasta bot.

2. Você pode treinar as models do Core rodando:
```make train-core```

3. Começa o servidor de actions em um terminal diferente:
```make action-server```


4. Disponibiliza o bot na API (localhost:5005):
```make run-api```
