import sys
# sys.path.append(sys.path[0] + "/...")
import os

sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from test_Login import test_Login

import testtools as testtools

if __name__ == "__main__":
    test_loader = TestLoader()

    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(test_Login)
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
