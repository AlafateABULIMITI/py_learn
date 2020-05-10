"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture/test_autouse.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:

So far, all fixture use has been specified manually, either as a parameter, or using `usefixtures`.

If we want the fixture to execute automatically, we can specify the `autouse` parameter at the time of definition.

Here are two auto-timing fixture, one for each function's run time (`function` scope) and one for calculating total test time (`session` scope)

--------------
Last Modified: Sunday May 10th 2020 10:58:18 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 11:04:50			Alafate			add autouse fixture
"""
import pytest
import time

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


@pytest.fixture(scope="session", autouse=True)
def timer_session_scope():
    start = time.time()
    print("\nstart: {}".format(time.strftime(DATE_FORMAT, time.localtime(start))))

    yield

    finished = time.time()
    print("finished: {}".format(time.strftime(DATE_FORMAT, time.localtime(finished))))
    print("Total time cost: {:.3f}s".format(finished - start))


@pytest.fixture(autouse=True)
def timer_function_scope():
    start = time.time()
    yield
    print(" Time cost: {:.3f}s".format(time.time() - start))


def test_1():
    time.sleep(1)


def test_2():
    time.sleep(2)


"""
pytest -s test_autouse.py                                                2914  11:03:18 
======================================= test session starts ========================================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture
collected 2 items

test_autouse.py
start: 2020-05-10 11:03:34
. Time cost: 1.003s
. Time cost: 2.004s
finished: 2020-05-10 11:03:37
Total time cost: 3.008s


======================================== 2 passed in 3.02s =========================================
"""
