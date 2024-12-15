# 🎲 Dice Roller and Analyzer

## Overview
This Python program simulates rolling dice, analyzes the results statistically, and visualizes the roll distribution using a histogram. It's an interactive and educational tool that combines randomness, statistics, and data visualization, perfect for Python learners, gamers, or anyone curious about dice probabilities.

---

## Features

- **Simulate Dice Rolls**: Roll any number of dice with customizable sides.
- **Statistical Analysis**: Calculates the mean, median, and mode of the rolled results.
- **Data Visualization**: Displays a histogram of the roll distribution using Matplotlib.
- **Interactive Experience**: Provides an easy-to-use interface for repeated use.

---

## Requirements

- Python 3.x
- Libraries:
  - `random`: For generating random dice rolls.
  - `statistics`: For statistical calculations (mean, median, mode).
  - `matplotlib`: For visualizing roll distributions.

---

## How to Run the Program

1. Clone or download the repository.
2. Ensure you have Python installed on your system.
3. Install required libraries using pip if needed:
   ```bash
   pip install matplotlib
   ```
4. Run the program:
   ```bash
   python dice_roller.py
   ```

---

## Usage

1. Enter the number of dice you want to roll.
2. Specify the number of sides on each die (e.g., 6 for standard dice).
3. View the rolled results and their statistical analysis (mean, median, mode).
4. See a visual histogram of the roll distribution.
5. Decide whether to roll again or exit the program.

---

## Example Output

### Input:
```
How many dice would you like to roll? 5
How many sides do your dice have? 6
```

### Output:
```
You rolled: [3, 5, 2, 6, 4]

Statistics:
 - Mean: 4.00
 - Median: 4.00
 - Mode: 3

Generating a visual representation...
```

(A histogram of the rolls will be displayed.)

---

## Error Handling

- **Invalid Input**: Handles non-integer inputs gracefully and prompts the user to try again.
- **Unexpected Errors**: Catches and displays unexpected errors for debugging.

---

## Contribution
Feel free to fork this repository, make improvements, and submit a pull request. Suggestions and feedback are always welcome!

---

## License
This project is open-source and available under the MIT License.

---

## Author
Developed by Geco97.

---

Happy rolling! 🎲
