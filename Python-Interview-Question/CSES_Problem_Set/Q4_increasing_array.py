"""
You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.

On each turn, you may increase the value of any element by one. What is the minimum number of turns required?

Input

The first input line contains an integer n: the size of the array.

Then, the second line contains n integers x1,x2,…,xn: the contents of the array.

Output

Print the minimum number of turns.

Constraints
1 ≤ n ≤ 2*10^5
1 ≤ xi ≤ 10^9
Example

Input:
5
3 2 5 1 7

Output:
5

"""

import argparse 
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def increasing_array(args):
    assert len(args.number_array) == args.number, "The size of array is incorrectly specified"

    int_array, ans = args.number_array, 0

    for index in range(len(int_array) - 1):
        while int_array[index] > int_array[index+1]:
            int_array[index+1] += 1
            ans += 1

    logger.info(f"The minimum number of turns required is {ans}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tools to find length of the longest repetition")
    parser.add_argument('-n', dest="number", type=int, help="Size of the integer array", required=True)
    parser.add_argument('-array', type=int, dest="number_array", nargs='+')
    args = parser.parse_args()

    increasing_array(args)