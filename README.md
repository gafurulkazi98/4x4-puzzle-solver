# 4x4-puzzle-solver
Returns the steps of a given 14-piece 4-by-4 slider puzzle to reach a given solution

Created for NYU Tandon School of Engineering "Artificial Intelligence" Undergraduate Course (CS-UY 4613)

Currently unoptimized

Input text file contains initial state of the board and final state of the board

Output text file contains inital state of the board, final state of the board, number of moves taken to reach final state, number of nodes generated, moves taken to move the two zeroes (blank spaces), and f(n) at each move, where f(n) = Manhattan distances of each non-blank tile to their goal position + number of moves taken so far.

Example input:

1 2 3 4
5 0 6 7
8 9 0 10
11 12 13 14

1 2 4 0
8 5 3 7
11 9 6 10
0 12 13 14

Example output:

1 2 3 4
0 5 6 7
8 9 0 10
11 12 13 14

1 2 3 4
5 6 7 8
9 10 11 12
13 14 0 0

6
40
U2 U2 R2 L1 D1 D1 
6 6 6 6 6 6 6 
