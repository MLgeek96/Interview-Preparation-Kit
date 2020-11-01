"""
A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.

Given n, construct a beautiful permutation if such a permutation exists.

Input

The only input line contains an integer n.

Output

Print a beautiful permutation of integers 1,2,…,n. 
If there are several solutions, you may print any of them. 
If there are no solutions, print "NO SOLUTION".

Constraints
1 ≤ n ≤ 10^6

Example 1

Input:
5

Output:
4 2 5 3 1

Example 2

Input:
3

Output:
NO SOLUTION

"""

import argparse 
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def permutation(args):
    assert 1 <= args.number <= 10**6, "Please input a integer within this interval [1, 100000]"

    permutation = ""
    if args.number == 1: ## base case
        permutation += "1"
        logger.info(permutation)
    elif args.number == 2 or args.number == 3: ## base case
        logger.info("NO SOLUTION")
    elif args.number % 2 == 0:
        for num in range(2, args.number+1, 2):
            permutation += f" {num} "
        for num in range(1, args.number+1, 2):
            permutation += f" {num} "
        logger.info(permutation)
    else:
        for num in range(args.number-1, 0, -2):
            permutation += f" {num} "
        for num in range(args.number, 0, -2):
            permutation += f" {num} "
        logger.info(permutation)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Print a beautiful permutation of integers")
    parser.add_argument('-n', dest="number", type=int, help="Size of the integer array", required=True)
    args = parser.parse_args()

    permutation(args)