import importlib
import types
import sys

import pytest

# Import functions from qwen3_demo without requiring gradio

module_name = "qwen3_demo"

spec = importlib.util.spec_from_file_location(module_name, "qwen3_demo.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reasoning_mode_switch = module.reasoning_mode_switch
multilingual_translation = module.multilingual_translation


def test_reasoning_simple():
    result = reasoning_mode_switch("Hola", "simple")
    assert result == "Salida de razonamiento simple para: Hola"


def test_reasoning_advanced():
    result = reasoning_mode_switch("Hola", "advanced")
    assert result == "Salida de razonamiento avanzado para: Hola"


def test_reasoning_invalid_mode():
    result = reasoning_mode_switch("Hola", "otro")
    assert result == "Modo no válido seleccionado."


def test_reasoning_no_input():
    result = reasoning_mode_switch("", "simple")
    assert result == "Por favor ingresa un texto de entrada."


def test_translation_spanish():
    result = multilingual_translation("Hello", "es")
    assert result == "Traducción al español de 'Hello'"


def test_translation_french():
    result = multilingual_translation("Hello", "fr")
    assert result == "Traducción al francés de 'Hello'"


def test_translation_german():
    result = multilingual_translation("Hello", "de")
    assert result == "Traducción al alemán de 'Hello'"


def test_translation_unsupported():
    result = multilingual_translation("Hello", "it")
    assert result == "Idioma no soportado."


def test_translation_no_text():
    result = multilingual_translation("", "es")
    assert result == "Por favor ingresa un texto para traducir."
