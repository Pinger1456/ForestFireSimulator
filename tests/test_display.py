"""Tests for display utilities."""

import unittest
from unittest.mock import patch
from models.forest import Forest
from utils.display import ForestDisplay


class TestDisplay(unittest.TestCase):
    """Test cases for ForestDisplay class."""

    def setUp(self):
        """Initialize test objects."""
        self.forest = Forest(5, 5)
        self.display = ForestDisplay()

    @patch('bext.clear')
    def test_clear_screen(self, mock_clear):
        """Test screen clearing."""
        self.display.clear_screen()
        mock_clear.assert_called_once()

    @patch('bext.goto')
    @patch('bext.fg')
    @patch('builtins.print')
    def test_display_forest(self, mock_print, mock_fg, mock_goto):
        """Test forest display."""
        self.display.display_forest(self.forest)
        self.assertTrue(mock_goto.called)
        self.assertTrue(mock_fg.called)
        self.assertTrue(mock_print.called)


if __name__ == '__main__':
    unittest.main()
