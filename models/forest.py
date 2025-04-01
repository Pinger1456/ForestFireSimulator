"""Forest model and operations."""

import random
from config.settings import (WIDTH, HEIGHT, TREE, FIRE, EMPTY,
                             INITIAL_TREE_DENSITY, GROW_CHANCE, FIRE_CHANCE)


class Forest:
    """Represents a forest grid and its operations."""

    def __init__(self, width=WIDTH, height=HEIGHT):
        """Initialize forest with given dimensions."""
        self.width = width
        self.height = height
        self.grid = self.create_new_forest()

    def create_new_forest(self):
        """Create a new forest grid with initial trees."""
        grid = {}
        for x in range(self.width):
            for y in range(self.height):
                if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                    grid[(x, y)] = TREE
                else:
                    grid[(x, y)] = EMPTY
        return grid

    def update_forest(self):
        """Update forest state for one simulation step."""
        new_grid = {}

        for x in range(self.width):
            for y in range(self.height):
                if (x, y) in new_grid:
                    continue

                current_cell = self.grid.get((x, y), EMPTY)

                if current_cell == EMPTY and random.random() <= GROW_CHANCE:
                    new_grid[(x, y)] = TREE
                elif current_cell == TREE and random.random() <= FIRE_CHANCE:
                    new_grid[(x, y)] = FIRE
                elif current_cell == FIRE:
                    # Spread fire to neighbors
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            neighbor = (x + dx, y + dy)
                            if self.grid.get(neighbor) == TREE:
                                new_grid[neighbor] = FIRE
                    new_grid[(x, y)] = EMPTY
                else:
                    new_grid[(x, y)] = current_cell

        self.grid = new_grid
        return self.grid
