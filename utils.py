import logging

from constants import (ERROR_CONTEXT_EMPTY,
                       ERROR_CONTEXT_ONLY_INVALID_CHARACTERS,
                       ERROR_CONTEXT_TOO_LONG, INVALID_INPUT,
                       MAX_TEXT_LENGTH_FOR_MODEL)


class Utils:
    def __init__(self):
        pass

    def cleanup_context(self, context):
        return context.strip()

    def validate_context(self, context):
        if len(context) <= 0:
            raise ValueError(ERROR_CONTEXT_EMPTY)
        elif len(context) > MAX_TEXT_LENGTH_FOR_MODEL:
            logging.warning(
                "The number of characters in the string exceeds the maximum limit taken by the model."
            )
            raise ValueError(ERROR_CONTEXT_TOO_LONG)
        elif not any(char.isalpha() for char in context):
            logging.warning("The input contains only invalid characters like $%#!.")
            raise ValueError(ERROR_CONTEXT_ONLY_INVALID_CHARACTERS)
        return context

    def validate_entities(self, extracted_entities):
        if not extracted_entities:
            logging.warning("No entities found in the input text.")
            raise ValueError(INVALID_INPUT)
        return True
