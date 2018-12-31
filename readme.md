# Flapjack Solver

A python solver for the Flapjack Fwop puzzle at [https://cassidoo.github.io/flapjack-fwop](https://cassidoo.github.io/flapjack-fwop/)

The solver is a single python file that takes input as the buttered/unbuttered state of each pancake, starting with the top-left pancake.  It returns a list of pancakes to click in order.

*notes: This was a quick for-fun solver and does not include input validation.  It will keep searching until all possibly reachable states of pancakes based on the starting state have been found, so if the puzzle is unsolvable, it will take a long time to find out that it is unsolvable using this program.*
