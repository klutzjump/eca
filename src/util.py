import argparse
import random


def check_initial_state(initial_state, cols):
    if len(initial_state) != cols:
        raise Exception(f"initial state is not of length {cols}")

    for char in initial_state:
        if char != "1" and char != "0":
            raise Exception("initial state may only contain 1s and 0s")


def check_symbol(symbol):
    if len(symbol) != 1:
        raise Exception(f"output symbol must be single char, not str")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("rule", help="rule in Wolfram notation", type=int)
    parser.add_argument("cols", help="width in columns", type=int)
    parser.add_argument("steps", help="number of steps/iterations", type=int)
    parser.add_argument("-o", "--out", help="output char", type=str)
    parser.add_argument("-i", "--initial", help="initial state", type=str)
    return parser.parse_args()


def print_universe(universe, symbol):
    for line in universe:
        for cell in line:
            if cell == "1":
                print(symbol, end="")
            else:
                print(" ", end="")

        print("\n", end="")


def random_initial_state(width):
    return [random.choice(["1", "0"]) for _ in range(0, width)]
