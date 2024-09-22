# Multiplication Quiz for Terminal

Randomly generates small multiplication quizzes. Intended for use on my phone terminal emulator.

## Usage

- seed is in [`seed.txt`](seed.txt), if it exists (default: 0)
- number of digits is in [`n_digits.txt`](n_digits.txt), if it exists (default: 5)

On execution, a file [`current_task_number.txt`](current_task_number.txt) is created, which contains the number of the current task. In the default case (without arguments) this task number is read (without solution).

Specify with `--solution` increment the current task number. Feel free to set manually and explore.
