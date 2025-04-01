"""Display utilities for forest simulation."""

import time
import bext
from config.settings import (TREE, FIRE, EMPTY, GROW_CHANCE,
                             FIRE_CHANCE, PAUSE_LENGTH)


class ForestDisplay:
    """Handles display of the forest simulation."""

    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        bext.clear()

    @staticmethod
    def display_forest(forest):
        """Display the forest grid on screen."""
        bext.goto(0, 0)
        for y in range(forest.height):
            for x in range(forest.width):
                cell = forest.grid.get((x, y), EMPTY)
                if cell == TREE:
                    bext.fg('green')
                    print(TREE, end='')
                elif cell == FIRE:
                    bext.fg('red')
                    print(FIRE, end='')
                else:
                    print(EMPTY, end='')
            print()

        bext.fg('reset')
        print(f'Grow chance: {GROW_CHANCE * 100}%  ', end='')
        print(f'Lightning chance: {FIRE_CHANCE * 100}%  ', end='')
        print('Press Ctrl-C to quit.')

    @staticmethod
    def pause():
        """Pause simulation according to settings."""
        time.sleep(PAUSE_LENGTH)
