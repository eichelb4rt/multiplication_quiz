import os
import random
from argparse import ArgumentParser

HIGHEST_POSSIBLE_N_DIGITS = 32
MIN_GENERATED_NUMBER = 10 ** (HIGHEST_POSSIBLE_N_DIGITS - 1)
MAX_GENERATED_NUMBER = 10 ** HIGHEST_POSSIBLE_N_DIGITS - 1


def read_int_from_file_with_default(file_name: str, default: int) -> int:
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return int(f.read())
    else:
        return default


def generate_task(seed: int, task_number: int, n_digits: int) -> tuple[int, int]:
    random.seed(seed)
    min_factor = 10 ** (n_digits - 1)
    max_factor = 10 ** n_digits - 1
    for _ in range(task_number + 1):
        # i could do this and cut it off with a modulus to be consistent across numbers of digits, but i don't actually want that. make the necessary changes if you want that.
        # a = random.randint(MIN_GENERATED_NUMBER, MAX_GENERATED_NUMBER)
        # b = random.randint(MIN_GENERATED_NUMBER, MAX_GENERATED_NUMBER)
        a = random.randint(min_factor, max_factor)
        b = random.randint(min_factor, max_factor)
    return a, b


def main():
    parser = ArgumentParser("Randomly generates small multiplication quizzes. Seed is in seed.txt, if it exists (default: 0). Number of digits is in n_digits.txt, if it exists (default: 5). On execution, a file current_task_number.txt is created, which contains the number of the current task. In the default case (without arguments) this task number is read (without solution). Specify with --solution increment the current task number. Feel free to set manually and explore.")
    parser.add_argument("-s", "--solution", help="Shows the solutions to the current quiz", action="store_true")
    parser.add_argument("-n", "--task_number", help="Shows the quiz number `task_number` instead of the next quiz.", required=False, default=None)
    parser.add_argument("-e", "--explain", help="Explains why i use one file per variable instead of just json for 3 variables.", action="store_true")
    args = parser.parse_args()

    if args.explain:
        print("i intend to use this script primarily on my phone on the terminal. this is quite slow to navigate without a proper keyboard so i want to minimize the amount of pressing keys like arrows or backspace. such keys i would have to press more often if i were to navigate a json. it is much easier to just change 1 number in a file.")
        exit(0)

    # read program arguments the way we specified
    seed = read_int_from_file_with_default("seed.txt", 0)
    saved_task_number = read_int_from_file_with_default("current_task_number.txt", 0)
    n_digits = read_int_from_file_with_default("n_digits.txt", 0)

    # maybe use the given task number instead of the saved one
    task_number = saved_task_number
    if args.task_number is not None:
        task_number = int(args.task_number)

    # generate the task and maybe show the solution
    a, b = generate_task(seed, task_number, n_digits)
    if args.solution:
        print(f"{a} * {b} = {a * b}")
        if args.task_number is None:
            with open("current_task_number.txt", "w") as f:
                f.write(str(task_number + 1))
    else:
        print(f"{a} * {b} = ?")


if __name__ == "__main__":
    main()
