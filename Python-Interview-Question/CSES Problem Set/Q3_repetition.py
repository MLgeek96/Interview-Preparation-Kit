"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1 ≤ n ≤ 10^6
Example

Input:
ATTCGGGA

Output:
3

"""

import argparse 
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def repetition(args):
    char, count, ans = 'A', 1, 1

    for character in args.dna_sequence:
        if character == char:
            count += 1
            ans = max(count, ans)
        else:
            char = character 
            count = 1
            
    logger.info(f"the length of the longest repetition is {ans}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tools to find missing number")
    parser.add_argument('-dna', dest="dna_sequence", type=str, help="DNA sequence", required=True)
    args = parser.parse_args()

    repetition(args)