import unittest
from typing import Type

from asserts import assert_equal

from dectest import TestCase


class TestCaseTestBase(TestCase):
    def run_test_class(self, class_: Type[TestCase]) -> None:
        tests = unittest.TestLoader().loadTestsFromTestCase(class_)
        self.result = unittest.TestResult()
        tests.run(self.result)

    def run_test_suite(self, suite: unittest.TestSuite) -> None:
        self.result = unittest.TestResult()
        suite.run(self.result)

    def assert_test_result(self, success: int = 0, failure: int = 0,
                           error: int = 0) -> None:
        failure_count = len(self.result.failures)
        error_count = len(self.result.errors)
        success_count = self.result.testsRun - failure_count - error_count
        assert_equal((success, failure, error),
                     (success_count, failure_count, error_count))
