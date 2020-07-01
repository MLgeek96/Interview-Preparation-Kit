"""
A number spiral is an infinite grid whose upper-left square has number 1. 
Here are the first five layers of the spiral:

|  1 |  2 |  9 | 10 | 25 |
|  4 |  8 |  8 | 11 | 24 |
|  5 |  6 |  7 | 12 | 23 |
| 16 | 15 | 14 | 13 | 22 | 
| 17 | 18 | 19 | 20 | 21 |

Your task is to find out the number in row y and column x.

Input

The first input line contains an integer t: the number of tests.

After this, there are t lines, each containing integers y and x.

Output

For each test, print the number in row y and column x.

Constraints
1 ≤ t ≤ 10^5
1 ≤ y,x ≤ 10^9

Example

Input:
3
2 3
1 1
4 2

Output:
8
1
15

"""

import argparse 
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def number_spiral(args):
    coordinates = {}
    for pair in args.number_array:
        x_coordinate, y_coordinate = pair.split(':')
        coordinates[int(x_coordinate)] = int(y_coordinate)

    for x, y in coordinates.items():
        z = max(x, y)
        z2 = (z-1) ** 2
        if z % 2 == 0:
            if y == z:
                ans = z2 + x
            else:
                ans = z2 + 2 * z - y
        else:
            if x == z:
                ans = z2 + y
            else:
                ans = z2 + 2 * z - x

        logging.info(f"{ans}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find the number in the spiral")
    parser.add_argument('-n', dest="number", type=int, help="the number of tests", required=True)
    parser.add_argument('-array', dest="number_array", nargs='*')
    args = parser.parse_args()

    number_spiral(args)