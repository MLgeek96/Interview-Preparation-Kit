"""
Question:

Given a uniform distribution on (0,1), estimate the value of pi

Variant:

Given a uniform distribution on (a, b), estimate the value of pi
"""

import argparse
import random 
    
def estimate_pi(args):
    """
    This method is used to estimate the value of pi.

    Given X ~ U(0,1), estimate value of pi.

    """
    num_points_within_circle = 0

    for _ in range(args.number_of_iterations):
        x = random.random()
        y = random.random()

        if (x ** 2) + (y ** 2) <= 1:
            num_points_within_circle += 1

    print(f"The estimated value of pi is {4 * num_points_within_circle / args.number_of_iterations}")

    return 

def estimate_pi_variant(args):
    """
    This method is an extension of the problem above.

    Given X ~ U(a,b), estimate value of pi.

    """
    num_points_within_circle = 0

    assert args.lower_bound < args.upper_bound, "lower_bound is larger than upper bound"

    for _ in range(args.number_of_iterations):
        x = random.uniform(args.lower_bound, args.upper_bound)
        y = random.uniform(args.lower_bound, args.upper_bound)

        if ((x-args.lower_bound) ** 2 + (y-args.lower_bound) **2) <= (args.upper_bound-args.lower_bound) **2:
            num_points_within_circle += 1

    print(f"The estimated value of pi is {4 * num_points_within_circle / args.number_of_iterations}")

    return 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tools to estimate pi")
    subparsers = parser.add_subparsers(help="Desired action to perform")

    base_parser = argparse.ArgumentParser(add_help=False)
    base_parser.add_argument('--number-of-iterations', '-n', default=100000, type=int, help="Number of iterations to estimate pi", required=False)
    
    usual = subparsers.add_parser("usual", parents=[base_parser], help="Estimate pi with given number of iterations")
    usual.set_defaults(func=estimate_pi)

    uniform_params_parser = argparse.ArgumentParser(add_help=False)
    uniform_params_parser.add_argument('--lower-bound', '-lower', type=int, help="lower bound of interval", required=True)
    uniform_params_parser.add_argument('--upper-bound', '-upper',  type=int, help="Upper bound of interval", required=True)
    
    uniform_params = subparsers.add_parser("uniform-params", parents=[base_parser, uniform_params_parser], help="Parameters required for any given uniform distribution other than standard uniform distribution")
    uniform_params.set_defaults(func=estimate_pi_variant)

    args = parser.parse_args()
    args.func(args)


