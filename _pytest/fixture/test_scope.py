"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture/test_scope.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:
The role of fixture is to abstract out duplicate work and facilitate reuse, and for more granular control of fixture (e.g., fixture that only wants to use automatic connection closure for database access test scripts), Pytest uses scopes to specify the scope of fixture use.

When defining fixture, the scope is declared via the scope parameter, with the following options.

`function`: function level, where each test function executes fixture once.
`class`: class level, executed once per test class, all methods are available.
`module`: module level, executed once per module, with functions and methods available within the module.
`session`: session level, one test is executed only once, all found functions and methods are available.
--------------
Last Modified: Sunday May 10th 2020 10:08:08 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 10:13:40			Alafate			add different scopes funcs
"""


@pytest.fixture(scope="function")
def func_scope():
    pass


@pytest.fixture(scope="module")
def mod_scope():
    pass


@pytest.fixture(scope="session")
def sess_scope():
    pass


def test_multi_scope(sess_scope, mod_scope, func_scope):
    pass


@pytest.mark.usefixtures("class_scope")
class TestClassScope:
    def test_1(self):
        pass

    def test_2(self):
        pass


# The role of the fixture is to extract duplicate work and facilitate reuse, and in order to use the scope for classes, `pytest.mark.usefixtures` is used (also for functions and methods)
@pytest.fixture(scope="class")
def class_scope():
    pass
