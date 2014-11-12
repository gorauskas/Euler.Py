# -*- coding: utf-8 -*-

import argparse


def parse_options(args):
    parser = argparse.ArgumentParser(
        description='Solutions to Project Euler problems written in Python 3',
        epilog='written by Jonas Gorauskas')

    parser.add_argument('-V', '--version',
                        action='version',
                        version='%(prog)s 0.1.0 - written by Jonas Gorauskas')

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Prints the problem statement and the solution')

    parser.add_argument('-p', '--problem',
                        help='The problem/solution number you want to run')

    return parser.parse_args()
