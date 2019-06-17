from rasa_core import config
from rasa_core.trackers import DialogueStateTracker
from rasa_core.domain import Domain
from rasa_core.policies import KerasPolicy
from rasa_core.agent import Agent
from rasa_core.dispatcher import Dispatcher
from rasa_core.channels import CollectingOutputChannel
from rasa_core.nlg import TemplatedNaturalLanguageGenerator

from bot.actions import (HeadacheForm, ChestPainForm, FluLikeForm,
                        AbdominalPainForm)
import uuid


def test_agent_and_persist_dor_de_cabeca():
    policies = config.load("./bot/policies.yml")
    policies[0] = KerasPolicy(epochs=2)  # Keep training times low

    agent = Agent("./bot/domain.yml", policies=policies)
    training_data = agent.load_data("./bot/data/stories/stories.md")
    agent.train(training_data, validation_split=0.0)
    agent.persist("./tests/models/dialogue")

    loaded = Agent.load("./tests/models/dialogue")

    assert agent.handle_text("/dor_de_cabeca") is not None
    assert loaded.domain.action_names == agent.domain.action_names
    assert loaded.domain.intents == agent.domain.intents
    assert loaded.domain.entities == agent.domain.entities
    assert loaded.domain.templates == agent.domain.templates


def test_agent_and_persist():
    policies = config.load("./bot/policies.yml")
    policies[0] = KerasPolicy(epochs=2)  # Keep training times low

    agent = Agent("./bot/domain.yml", policies=policies)
    training_data = agent.load_data("./bot/data/stories/stories.md")
    agent.train(training_data, validation_split=0.0)
    agent.persist("./tests/models/dialogue")

    loaded = Agent.load("./tests/models/dialogue")

    assert agent.handle_text("/sintomas_gripais") is not None
    assert loaded.domain.action_names == agent.domain.action_names
    assert loaded.domain.intents == agent.domain.intents
    assert loaded.domain.entities == agent.domain.entities
    assert loaded.domain.templates == agent.domain.templates


def test_headache_form_action():
    domain = Domain.load("./bot/domain.yml")
    nlg = TemplatedNaturalLanguageGenerator(domain.templates)
    dispatcher = Dispatcher("my-sender", CollectingOutputChannel(), nlg)
    uid = str(uuid.uuid1())
    tracker = DialogueStateTracker(uid, domain.slots)

    action = HeadacheForm()
    action.run(dispatcher, tracker, domain)

    assert (
        "yes_or_no Algum médico já o diagnosticou com enxaqueca?"
        == dispatcher.output_channel.latest_output()["text"]
    )


def test_chestpain_form_action():
    domain = Domain.load("./bot/domain.yml")
    nlg = TemplatedNaturalLanguageGenerator(domain.templates)
    dispatcher = Dispatcher("my-sender", CollectingOutputChannel(), nlg)
    uid = str(uuid.uuid1())
    tracker = DialogueStateTracker(uid, domain.slots)

    action = ChestPainForm()
    action.run(dispatcher, tracker, domain)

    assert (
        "yes_or_no Você já sofreu de infarto do miocárdio?"
        == dispatcher.output_channel.latest_output()["text"]
    )


def test_flulike_form_action():
    domain = Domain.load("./bot/domain.yml")
    nlg = TemplatedNaturalLanguageGenerator(domain.templates)
    dispatcher = Dispatcher("my-sender", CollectingOutputChannel(), nlg)
    uid = str(uuid.uuid1())
    tracker = DialogueStateTracker(uid, domain.slots)

    action = FluLikeForm()
    action.run(dispatcher, tracker, domain)

    assert (
        "text O que mais você está sentindo?"
        == dispatcher.output_channel.latest_output()["text"]
    )


def test_abdominalpain_form_action():
    domain = Domain.load("./bot/domain.yml")
    nlg = TemplatedNaturalLanguageGenerator(domain.templates)
    dispatcher = Dispatcher("my-sender", CollectingOutputChannel(), nlg)
    uid = str(uuid.uuid1())
    tracker = DialogueStateTracker(uid, domain.slots)

    action = AbdominalPainForm()
    action.run(dispatcher, tracker, domain)

    assert (
        "yes_or_no Existe possibilidade de gravidez?"
        == dispatcher.output_channel.latest_output()["text"]
    )
