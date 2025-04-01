"""Tests for forest model."""

import unittest
from models.forest import Forest
from config.settings import TREE, EMPTY


class TestForest(unittest.TestCase):
    """Test cases for Forest class."""

    def setUp(self):
        """Initialize test forest."""
        self.forest = Forest(10, 10)  # Smaller size for testing

    def test_initialization(self):
        """Test forest initialization."""
        self.assertEqual(self.forest.width, 10)
        self.assertEqual(self.forest.height, 10)
        self.assertEqual(len(self.forest.grid), 100)

    def test_create_new_forest(self):
        """Test forest creation."""
        grid = self.forest.create_new_forest()
        self.assertTrue(all(cell in (TREE, EMPTY) for cell in grid.values()))

    def test_update_forest(self):
        """Test forest update logic."""
        # Manually set some cells for testing
        self.forest.grid[(0, 0)] = TREE
        self.forest.grid[(1, 0)] = TREE
        self.forest.grid[(0, 1)] = EMPTY

        # Test fire spread
        self.forest.grid[(0, 0)] = 'W'
        self.forest.update_forest()

        # Check if fire spread to adjacent tree
        self.assertEqual(self.forest.grid.get((1, 0)), 'W')


if __name__ == '__main__':
    unittest.main()
