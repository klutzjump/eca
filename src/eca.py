#!/usr/bin/env python
import calc
import util


"""
eca runs elementary cellular automata in the terminal

use:
    syntax:
        pyeca [rule] [cols] [steps]

    args:
        rule: rule specified using Wolfram notation (1-256)
        cols: character width of automaton
        steps: number of steps/iterations to compute

    optional flags:
        --initial or -i: initial state specified with 1s and 0s
        --out or -o: character (1s) used as output to terminal

"""


if __name__ == "__main__":
    args = util.parse_args()

    if args.initial:
        util.check_initial_state(args.initial, args.cols)
        initial_state = args.initial
    else:
        initial_state = util.random_initial_state(args.cols)

    if args.out:
        util.check_symbol(args.out)
        symbol = args.out
    else:
        symbol = "\u2588"

    universe = calc.run(initial_state, args.rule, args.steps)
    util.print_universe(universe, symbol)
