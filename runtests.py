#!/usr/bin/env python

import sys
import tests
import unittest


def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTests(loader.loadTestsFromModule(tests.terminals))
    test_suite.addTests(loader.loadTestsFromModule(tests.themes))
    test_suite.addTests(loader.loadTestsFromModule(tests.widgets))
    return test_suite


def run_tests():
    s = suite()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(s)
    sys.exit({True: 0, False: 3}[result.wasSuccessful()])

if __name__ == '__main__':
    run_tests()
