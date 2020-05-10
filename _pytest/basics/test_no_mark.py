"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/test_no_mark.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:
test no mark example
--------------
Last Modified: Sunday May 10th 2020 09:06:04 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 09:10:17			Alafate			add mark for finished and unfinished funcs

10-05-2020 09:10:10			Alafate			add 2 test funcs
"""
import pytest

# pytest will test all funcs begin with `test`
@pytest.mark.finished
def test_func1():
    assert 1 == 1


@pytest.mark.unfinished  # will not test this function
def test_func2():
    assert 1 != 1
