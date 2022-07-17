from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from utils import is_empty_string, sample_no_replace


class TestUtils(TestCase):
    @parameterized.expand([' ', '\t'])
    def test_any_white_spaces_is_empty(self, white_spaces: str):
        actual = is_empty_string(white_spaces)

        self.assertTrue(actual)

    @parameterized.expand(['billy', 'hughie'])
    def test_any_letters_is_not_empty(self, letters: str):
        actual = is_empty_string(letters)

        self.assertFalse(actual)

    @parameterized.expand([
        ['homelander', 'starlight'],
        ['maeve', 'a-train']
    ])
    def test_random_choice_is_removed_from_seq(self, expected, unexpected):
        def choice_expected(seq):
            return expected

        with patch('utils.choice', choice_expected):
            given = [expected, unexpected]

            sample_no_replace(given)
            actual = given

            self.assertListEqual(actual, [unexpected])

    @parameterized.expand(['mm', 'deep'])
    def test_random_choice_is_returned(self, expected):
        def choice_expected(seq):
            return expected

        with patch('utils.choice', choice_expected):
            actual = sample_no_replace([expected])

            self.assertIs(actual, expected)
