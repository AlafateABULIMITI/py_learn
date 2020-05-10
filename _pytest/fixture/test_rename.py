"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture/test_rename.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:

The fixture name defaults to the function name at the time of definition, if you do not want to use the default, you can specify the name via the `name` option.

--------------
Last Modified: Sunday May 10th 2020 11:05:39 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 11:07:58			Alafate			add `rename` function to fixture.
"""

import pytest


@pytest.fixture(name="age")
def calculate_average_age():
    return 20


def test_age(age):
    assert age == 20
