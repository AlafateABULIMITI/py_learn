"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/test1.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:
pytest framework success example
--------------
Last Modified: Sunday May 10th 2020 08:56:08 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 08:57:13			Alafate			add test_passing func
"""


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


# use shell command:  pytest _pytest/test1.py
# PYTEST uses `.` marking test success (PASSED).
