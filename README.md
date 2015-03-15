# Euler

Solutions to the Project Euler problems implemented in Python 3.

Clone this repo and then run the following from the command line:

    ./euler.py -p <problem number>

## Usage

    usage: euler.py [-h] [-V] [-v] [-p PROBLEM]

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -v, --verbose         Prints the problem statement and the solution
      -p PROBLEM, --problem PROBLEM
                            The problem/solution number you want to run

## Tests

Alternatively, there is a full set of unit tests that can be run by invoking
nose at the root of the package, like so:

    cd Euler.Py
    nosetests
