"""
Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.

Input

The only input line contains an integer n.

Output

Print n integers: the results.

Constraints
1 ≤ n ≤ 10000

Example

Input:
8

Output:
0
6
28
96
252
550
1056
1848

"""

import argparse 
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def two_knights(args):
    
    for num in range(args.number):
        board_size = (num + 1) ** 2
        solution = board_size * (board_size - 1) / 2
        if num > 2:
            solution -= 4 * num * (num - 1)
        logging.info(int(solution))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find the number in the spiral")
    parser.add_argument('-n', dest="number", type=int, help="board size", required=True)
    args = parser.parse_args()

    two_knights(args)