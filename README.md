# Triage bot

Um bot api utilizado para categorizar o risco de um paciente de emergência de acordo
com o Protocolo de Manchester.



## Bot

### API

```sh
sudo docker-compose up bot
```

Para que a assistente virtual inicie a conversa você deve criar um `trigger`.
Para isso, entre no rocketchat como `admin`, e vá no painel do Livechat na
seção de Triggers, clique em `New Trigger`. Preencha o Trigger da seguinte forma:

```yaml
Enabled: Yes
Name: Start Talk
Description: Start Talk
Condition: Visitor time on site
    Value: 3
Action: Send Message
 Value: Impersonate next agent from queue
 Value: Olá!
```

```sh
curl --request POST \
  --url http://localhost:5005/webhooks/rest/webhook \
  --header 'content-type: application/json' \
  --data '{
    "message": "mensagem"
  }'
```




### Console

```sh
sudo docker-compose run --rm bot make train
sudo docker-compose run --rm bot make run-console
```

### Train Online

```
sudo make train
sudo docker-compose run --rm bot make train-online
```

## Analytics

### Setup

```
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py
sudo docker-compose up -d elasticsearch
```

Lembre-se de setar as seguintes variaveis de ambiente no `docker-compose`.

```
ENVIRONMENT_NAME=localhost
BOT_VERSION=last-commit-hash
```

### Visualização

```
sudo docker-compose up -d kibana
```

Você pode acessar o kibana no `locahost:5601`




## Notebooks - Análise de dados

### Setup

Levante o container `notebooks`

```sh
docker-compose up -d notebooks
```

Acesse o notebook em `localhost:8888`



## Tutorial para levantar toda a stack

```sh
./docker/build-base.sh 
sudo docker-compose up coach
sudo make train
sudo docker-compose up -d kibana
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py

sudo docker-compose up -d bot
```
