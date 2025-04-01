"""Forest Fire Sim, by Al Sweigart al@inventwithpython.com
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/"""

import sys
from models.forest import Forest
from utils.display import ForestDisplay


def main():
    """Run the forest fire simulation."""
    try:
        forest = Forest()
        display = ForestDisplay()
        display.clear_screen()

        while True:
            display.display_forest(forest)
            forest.update_forest()
            display.pause()

    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
