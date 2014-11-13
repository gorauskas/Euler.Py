# -*- coding: utf-8 -*-

import importlib

from euler import util


EULER_SOLUTION = 'euler.solutions.euler'
EULER_CLSNAME = 'Euler'


def run(args):
    opts = util.parse_options(args)

    try:

        mod = importlib.import_module(EULER_SOLUTION + opts.problem)
        cls = getattr(mod, EULER_CLSNAME)
        e = cls()

        if opts.verbose:
            print(e.problem)

        e.solve()

    except (ImportError, TypeError):

        if not opts.problem:
            print('Please provide a Project Euler problem number...')
            print('Invoke ./euler.py -h for usage information')
        else:
            print('Unable to execute solution to Project Euler problem %s'
                  % opts.problem)


# def run(args):
#     opts = util.parse_options(args)

#     mod = importlib.import_module(EULER_SOLUTION + opts.problem)
#     cls = getattr(mod, EULER_CLSNAME)
#     e = cls()

#     if opts.verbose:
#         print(e.problem)

#     e.solve()
