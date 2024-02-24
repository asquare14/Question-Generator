import json
import unittest

from app import app
from constants import (ERROR_CONTEXT_EMPTY,
                       ERROR_CONTEXT_ONLY_INVALID_CHARACTERS,
                       ERROR_CONTEXT_TOO_LONG, INVALID_INPUT)

VALID_INPUT = "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles gain kinetic energy and take up more space."
EXTRA_LONG_INPUT = (
    "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles gain kinetic energy and take up more space."
    * 6
)


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def post_question(self, context, expected_status_code):
        response = self.app.post("/generate-question", data={"context": context})
        self.assertEqual(response.status_code, expected_status_code)
        return json.loads(response.data)

    def test_generate_question_api_valid_input(self):
        """Test that the API generates a question for valid input."""
        data = self.post_question(VALID_INPUT, 200)
        self.assertIn("question", data)

    def test_generate_question_api_input_with_extra_spaces(self):
        """Test that the API handles input with extra spaces."""
        data = self.post_question("  " + VALID_INPUT, 200)
        self.assertIn("question", data)

    def test_generate_question_api_numeric_input(self):
        """Test that the API handles numeric input."""
        data = self.post_question("12345", 400)
        self.assertEqual(data["error"], ERROR_CONTEXT_ONLY_INVALID_CHARACTERS)

    def test_generate_question_api_special_characters(self):
        """Test that the API handles input with only special characters."""
        data = self.post_question("!@#$%^&*()", 400)
        self.assertEqual(data["error"], ERROR_CONTEXT_ONLY_INVALID_CHARACTERS)

    def test_generate_question_api_non_english_characters(self):
        """Test that the API handles non-English characters."""
        data = self.post_question("こんにちは世界", 400)
        self.assertEqual(data["error"], INVALID_INPUT)

    def test_generate_question_api_empty_input(self):
        """Test that the API returns an error for empty input."""
        data = self.post_question("", 400)
        self.assertIn("error", data)
        self.assertEqual(data["error"], ERROR_CONTEXT_EMPTY)

    def test_generate_question_api_extra_long_input(self):
        """Test that the API returns an error for input that is too long."""
        data = self.post_question(EXTRA_LONG_INPUT, 400)
        self.assertIn("error", data)
        self.assertEqual(data["error"], ERROR_CONTEXT_TOO_LONG)

    def test_generate_question_api_no_entities_generated(self):
        """Test that the API returns an error when no entities can be generated."""
        data = self.post_question("what what what what what", 400)
        self.assertIn("error", data)
        self.assertEqual(data["error"], INVALID_INPUT)


if __name__ == "__main__":
    unittest.main()
