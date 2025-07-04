import os
import sys
import types


class DummyBlocks:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        pass


dummy_gradio = types.ModuleType("gradio")
dummy_gradio.Blocks = DummyBlocks
dummy_gradio.Markdown = lambda *args, **kwargs: None
dummy_gradio.Textbox = lambda *args, **kwargs: None
dummy_gradio.Radio = lambda *args, **kwargs: None
dummy_gradio.Button = lambda *args, **kwargs: None
sys.modules["gradio"] = dummy_gradio
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import importlib

qwen3_demo = importlib.import_module("qwen3_demo")


def test_reasoning_mode_switch_simple():
    result = qwen3_demo.reasoning_mode_switch("hola", "simple")
    assert result == "Salida de razonamiento simple para: hola"


def test_reasoning_mode_switch_advanced():
    result = qwen3_demo.reasoning_mode_switch("hola", "advanced")
    assert result == "Salida de razonamiento avanzado para: hola"


def test_reasoning_mode_switch_invalid():
    result = qwen3_demo.reasoning_mode_switch("hola", "foo")
    assert result == "Modo no válido seleccionado."


def test_reasoning_mode_switch_empty():
    result = qwen3_demo.reasoning_mode_switch("", "simple")
    assert result == "Por favor ingresa un texto de entrada."


def test_multilingual_translation_es():
    result = qwen3_demo.multilingual_translation("hola", "es")
    assert result == "Traducción al español de 'hola'"


def test_multilingual_translation_fr():
    result = qwen3_demo.multilingual_translation("bonjour", "fr")
    assert result == "Traducción al francés de 'bonjour'"


def test_multilingual_translation_de():
    result = qwen3_demo.multilingual_translation("hallo", "de")
    assert result == "Traducción al alemán de 'hallo'"


def test_multilingual_translation_invalid_language():
    result = qwen3_demo.multilingual_translation("ciao", "it")
    assert result == "Idioma no soportado."


def test_multilingual_translation_empty_text():
    result = qwen3_demo.multilingual_translation("", "es")
    assert result == "Por favor ingresa un texto para traducir."
