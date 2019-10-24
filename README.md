# Improved TestCase Class


[![License](https://img.shields.io/pypi/l/dectest.svg)](https://pypi.python.org/pypi/dectest/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dectest)](https://pypi.python.org/pypi/dectest/)
[![Github](https://img.shields.io/github/release/srittau/python-dectest/all.svg)](https://github.com/srittau/python-dectest/releases/)
[![pypi](https://img.shields.io/pypi/v/dectest.svg)](https://pypi.python.org/pypi/dectest/)
[![Travis CI](https://travis-ci.org/srittau/python-dectest.svg?branch=master)](https://travis-ci.org/srittau/python-dectest)

`dectest.TestCase` is a drop-in replacement for `unittest.TestCase` with
a few added features.

## Tests, Setup, and Teardown with Decorators

Tests can optionally be marked using the `@test` decorator, instead of
prefixing the method name with `test`. The following test case class
contains two tests:

```python
from dectest import TestCase, test

class MyTest(TestCase):
    def test_foo(self):
        pass

    @test
    def bar(self):
        pass
```

Setup and teardown methods can be marked using the `@before` and `@after`
decorators, respectively. A class can have multiple setup and teardown
methods:

```python
from dectest import TestCase, before, after

class MyTest(TestCase):
    @before
    def setup_stuff(self):
        pass
    
    @before
    def setup_more_stuff(self):
        pass
        
    @after
    def teardown_all_stuff(self):
        pass
```

While the order of execution inside a class is undefined and should not be
relied upon, it is guaranteed that setup methods in super-classes are
executed before methods in sub-classes, and teardown methods in sub-classes
are executed before teardown method in super-classes:

```python
from dectest import TestCase, before, after

class MySuperTest(TestCase):
    @before
    def super_setup(self):
        print("setup first")
    
    @after
    def super_teardown(self):
        print("teardown second")

class MySubTest(MySuperTest):
    @before
    def sub_setup(self):
        print("setup second")

    @after
    def sub_teardown(self):
        print("teardown first")
```

## Patch Support

`dectest.TestCase` has a `patch()` method to install a mock using
`unittest.mock.patch()`. This patch is removed during test
teardown:

```python
from dectest import TestCase, test

class MyPatchTest(TestCase):
    @test
    def foo(self):
        exit = self.patch("sys.exit")  # will be stopped during teardown
        # call implementation
        exit.assert_called_with(1)
```
