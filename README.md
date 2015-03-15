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
    nosetests -v

## How it works...

The main program will try to import a module dynamically from `euler.solutions`
package based on the problem number passed in via the command line. From that
module it will load a class called `Euler`. If the user request verbose output,
the program calls the `problem` property of the loaded `Euler` class and then
calls the `answer` property.

All `Euler` classes are implemented using the abstract base class strategy to
define a common interface for all classes. This is the key contruct that allows
modules to be loaded dynamically. Look at the files `baseeuler.py` and
`program.py` for the gorry details.
