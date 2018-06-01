from asserts import fail, assert_true

from dectest import TestCase, test, before

from dectest_test.common import TestCaseTestBase


class DecoratorTest(TestCaseTestBase):
    @test
    def two_before_decorators(self) -> None:
        class MyTestCase(TestCase):
            @before
            def before1(self) -> None:
                self._my_before1 = True

            @before
            def before2(self) -> None:
                self._my_before2 = True

            @test
            def my_test(self) -> None:
                assert_true(hasattr(self, "_my_before1"), "before1 not called")
                assert_true(hasattr(self, "_my_before2"), "before2 not called")

        self.run_test_class(MyTestCase)
        self.assert_test_result(success=1)

    @test
    def decorator__success(self) -> None:
        class MyTestCase(TestCase):
            @test
            def foo(self) -> None:
                pass

        self.run_test_class(MyTestCase)
        self.assert_test_result(success=1)

    @test
    def decorator__error(self) -> None:
        class MyTestCase(TestCase):
            @test
            def foo(self) -> None:
                raise ValueError()

        self.run_test_class(MyTestCase)
        self.assert_test_result(error=1)

    @test
    def decorator__fail(self) -> None:
        class MyTestCase(TestCase):
            @test
            def foo(self) -> None:
                fail("failing test")

        self.run_test_class(MyTestCase)
        self.assert_test_result(failure=1)
