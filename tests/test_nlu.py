from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
import pytest

TRAINING_DATA_DIR = "bot/data/intents/nlu_data.md"
NLU_CONFIG_DIR = "bot/nlu_config.yml"
MODELS_DIR = "./tests/models"


@pytest.fixture()
def trainer():
    trainer = Trainer(config.load(NLU_CONFIG_DIR))
    yield trainer


@pytest.fixture()
def interpreter(trainer):
    training_data = load_data(TRAINING_DATA_DIR)
    interpreter = trainer.train(training_data)
    yield interpreter


def test_nlu_interpreter_dor_de_cabeça(interpreter):
    parsing = interpreter.parse("dor de cabeça")
    assert parsing["intent"]["name"] == "dor_de_cabeca"


def test_nlu_interpreter_intoxicacao(interpreter):
    parsing = interpreter.parse("tomei uma caixa de remedio")
    assert parsing["intent"]["name"] == "intoxicacao"


def test_interpreter_dir(trainer):
    interpreter_dir = trainer.persist()
    assert interpreter_dir
