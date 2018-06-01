import os
import sys
from asserts import assert_equal

from dectest import TestCase, test

from dectest_test.common import TestCaseTestBase


class PatchTest(TestCaseTestBase):
    @test
    def patched(self) -> None:
        class MyTestCase(TestCase):
            @test
            def my_test(self) -> None:
                getcwd = self.patch("os.getcwd")
                getcwd.return_value = "/foo/bar"
                assert_equal("/foo/bar", os.getcwd())

        self.run_test_class(MyTestCase)
        self.assert_test_result(success=1)

    @test
    def cleanup_in_teardown(self) -> None:
        class MyTestCase(TestCase):
            @test
            def my_test(self) -> None:
                self.patch("sys.copyright", "Fake Copyright")

        original_copyright = sys.copyright
        self.run_test_class(MyTestCase)
        assert_equal(original_copyright, sys.copyright)
