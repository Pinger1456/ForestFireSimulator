# Forest Fire Simulator 🌲🔥

A Python simulation of wildfires spreading in a forest, inspired by Nicky Case's Emoji Sim. This project demonstrates cellular automata and environmental modeling.

![Forest Fire Simulation Demo](demo.gif) *(placeholder for actual gif)*

## Features

- Realistic forest fire propagation model
- Adjustable simulation parameters
- Colorful terminal visualization
- Modular architecture for easy extension

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/forest-fire-sim.git
cd forest-fire-sim
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the simulation:
```bash
python main.py
```

**Controls:**
- `Ctrl+C` - Exit the simulation

**Adjustable parameters:**
Modify `config/settings.py` to change:
- Forest dimensions
- Tree growth probability
- Lightning strike chance
- Simulation speed

## Project Structure

```
forest_fire_sim/
├── config/            # Simulation configuration
├── models/            # Core data structures
├── utils/             # Display and helper functions
├── tests/             # Unit tests
├── main.py           # Entry point
└── requirements.txt   # Dependencies
```

## Configuration

Edit these values in `config/settings.py`:

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `WIDTH`, `HEIGHT` | Forest dimensions | 79, 22 |
| `INITIAL_TREE_DENSITY` | Starting tree coverage | 0.2 |
| `GROW_CHANCE` | Probability of new tree growth | 0.01 |
| `FIRE_CHANCE` | Probability of lightning strike | 0.01 |
| `PAUSE_LENGTH` | Simulation speed (seconds per step) | 0.5 |

## Running Tests

```bash
python -m unittest discover tests
```

## Requirements

- Python 3.3+
- bext library (for terminal colors)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Original concept by Al Sweigart
- Inspired by [Nicky Case's Emoji Sim](http://ncase.me/simulating/model/)
