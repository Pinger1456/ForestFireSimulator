"""Simulation settings and constants."""

# Dimensions
WIDTH = 79
HEIGHT = 22

# Symbols
TREE = 'A'
FIRE = 'W'
EMPTY = ' '

# Probabilities
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# Display
PAUSE_LENGTH = 0.5
