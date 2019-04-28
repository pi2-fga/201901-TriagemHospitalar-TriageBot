run-console:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current \
  --debug --endpoints endpoints.yml

run-api:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current \
  --endpoints endpoints.yml --debug --enable_api

evaluate:
	python3 -m rasa_core.evaluate -d models/dialogue -s data/core/

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions
