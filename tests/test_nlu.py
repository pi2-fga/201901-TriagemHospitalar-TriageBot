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

    parsing = interpreter.parse("Estou com dor de cabeça")
    assert parsing["intent"]["name"] == "dor_de_cabeca"


def test_nlu_interpreter_intoxicacao(interpreter):
    parsing = interpreter.parse("tomei uma caixa de remedio")
    assert parsing["intent"]["name"] == "intoxicacao"

    parsing = interpreter.parse("tomei produto de limpeza")
    assert parsing["intent"]["name"] == "intoxicacao"


def test_nlu_interpreter_dor_torax(interpreter):
    parsing = interpreter.parse("estou com dor no peito")
    assert parsing["intent"]["name"] == "dor_torax"

    parsing = interpreter.parse("dor torácica")
    assert parsing["intent"]["name"] == "dor_torax"


def test_nlu_interpreter_dor_abdomen(interpreter):
    parsing = interpreter.parse("dor na barriga")
    assert parsing["intent"]["name"] == "dor_abdomen"

    parsing = interpreter.parse("dor de lado")
    assert parsing["intent"]["name"] == "dor_abdomen"

    parsing = interpreter.parse("cólica")
    assert parsing["intent"]["name"] == "dor_abdomen"


def test_nlu_interpreter_sintomas_gripais(interpreter):
    parsing = interpreter.parse("tosse")
    assert parsing["intent"]["name"] == "sintomas_gripais"

    parsing = interpreter.parse("Tosse e dor de garganta")
    assert parsing["intent"]["name"] == "sintomas_gripais"

    parsing = interpreter.parse("estou com muita dor de garganta")
    assert parsing["intent"]["name"] == "sintomas_gripais"


def test_nlu_interpreter_outros_sintomas(interpreter):
    parsing = interpreter.parse("cansaço")
    assert parsing["intent"]["name"] == "outros_sintomas"

    parsing = interpreter.parse("diarréia")
    assert parsing["intent"]["name"] == "outros_sintomas"

    parsing = interpreter.parse("inchaço na barriga")
    assert parsing["intent"]["name"] == "outros_sintomas"


def test_nlu_interpreter_sim(interpreter):
    parsing = interpreter.parse("positivo")
    assert parsing["intent"]["name"] == "sim"

    parsing = interpreter.parse("isso")
    assert parsing["intent"]["name"] == "sim"

    parsing = interpreter.parse("sim")
    assert parsing["intent"]["name"] == "sim"


def test_nlu_interpreter_negativo(interpreter):
    parsing = interpreter.parse("não")
    assert parsing["intent"]["name"] == "negativo"

    parsing = interpreter.parse("nada")
    assert parsing["intent"]["name"] == "negativo"

    parsing = interpreter.parse("nenhum")
    assert parsing["intent"]["name"] == "negativo"


def test_interpreter_dir(trainer):
    interpreter_dir = trainer.persist(MODELS_DIR)
    assert interpreter_dir
