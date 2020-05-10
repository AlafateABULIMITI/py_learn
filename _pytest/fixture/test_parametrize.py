"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture/test_parametrize.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:
Since the fixture is also a function, we can also parameterize the fixture.
--------------
Last Modified: Sunday May 10th 2020 11:09:05 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 11:17:36			Alafate			add parametrize fixture funcs
"""

import pytest

"""
Fixture parameterization requires the use of pytest built-in fixture `request`, with parameters obtained through `request.param`.
"""


@pytest.fixture(params=[("redis", "6379"), ("elasticsearch", "9200")])
def param(request):
    return request.param


@pytest.fixture(autouse=True)
def db(param):
    print("\nSucceed to connect %s:%s" % param)

    yield

    print("\nSucceed to close %s:%s" % param)


def test_api():
    assert 1 == 1
