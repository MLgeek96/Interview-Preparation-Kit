"""
You are given all numbers between 1,2,…,n except one. 
Your task is to find the missing number.

Input

The first input line contains an integer n.

The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output

Print the missing number.

Constraints
2 ≤ n ≤ 2*10**5
Example

Input:
5
2 3 1 5

Output:
4

"""

import argparse 
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def missing_number(args):
    number = args.number
    int_array = args.number_array

    target_sum = int(number * (number+1) / 2)
    current_sum = sum(int_array)

    missing_num = target_sum - current_sum
    
    logger.info(f"Missing number in the given array is {missing_num}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tools to find missing number")
    parser.add_argument('-n', dest="number", type=int, help="Integer n", required=True)
    parser.add_argument('-array', type=int, dest="number_array", nargs='+')
    args = parser.parse_args()

    missing_number(args)

