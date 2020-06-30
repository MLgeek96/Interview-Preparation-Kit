"""
Consider an algorithm that takes as input a positive integer n. 
If n is even, the algorithm divides it by two, 
and if n is odd, the algorithm multiplies it by three and adds one. 

The algorithm repeats this, until n is one. 

For example, the sequence for n=3 is as follows:
3→10→5→16→8→4→2→1

Your task is to simulate the execution of the algorithm for a given value of n.

Input

The only input line contains an integer n.

Output

Print a line that contains all values of n during the algorithm.

Constraints
1 ≤ n ≤ 10^6

Example
Input:
3

Output:
3 10 5 16 8 4 2 1
"""

import argparse 
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def weird_algorithm(args):
    """
    This method will simulate the execution of the algorithm for a given value of n.
    """
    
    assert 1 <= args.number <= 10**6, "Please input another integer within the range [1, 1000000]"

    num = args.number
    seq = f"{num}"
    
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3*num + 1
        seq += f" {num}"
    
    logger.info(seq)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tools to estimate pi")
    parser.add_argument('-n', dest="number", type=int, help="Integer input", required=True)
    args = parser.parse_args()

    weird_algorithm(args)