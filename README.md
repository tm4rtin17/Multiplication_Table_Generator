# Multiplication Table Generator

## Overview
This Python program generates a multiplication table for a user-specified base number up to a user-defined number of rows. The program leverages input validation for robust handling of user inputs and provides a clean, formatted output of the multiplication table.

## Features
- Allows the user to specify both positive and negative base numbers.
- Ensures the user specifies at least one row for the multiplication table.
- Uses a `while` loop to iterate through each row and calculate the multiplication results dynamically.
- Cleanly formatted output for easy readability.

## How It Works
1. **Input Validation:**
   - The program uses `pyinputplus` to validate inputs for the base number and the maximum number of rows.
   - The `max_row_number` input has a minimum constraint of 1 to ensure the table has at least one row.
2. **Calculation and Output:**
   - A `while` loop iterates from 1 to the specified `max_row_number`.
   - For each iteration, the program calculates the result by multiplying the base number by the current row number and prints the result in the format: `base_number X row_counter = result`.

## Requirements
- Python 3.13.1
- `pyinputplus` library

## Installation
1. Clone this repository or download the program file.
2. Ensure you have Python 3.x installed on your system.
3. Install `pyinputplus` by running:
   ```bash
   pip install pyinputplus
   ```

## Usage
1. Run the program using the command:
   ```bash
   python Multiplication_Table_Generator.py
   ```
2. Enter the base number (positive or negative) when prompted.
3. Enter the maximum number of rows for the table (minimum value: 1).
4. View the generated multiplication table in the terminal.

## Example Output
```
What is the base number you would like to generate a multiplication table for? 3
What is the maximum amount of rows you would like to generate? 5
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
```

## Future Enhancements
- Add an option to save the table to a text file.
- Allow users to generate multiple tables in a single session.
- Add an option to customize the range (e.g., start and end numbers) for the table.

## License
This project is licensed under the MIT License.

