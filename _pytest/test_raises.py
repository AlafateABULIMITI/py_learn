"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/test_raises.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:
test raise example
--------------
Last Modified: Sunday May 10th 2020 09:02:36 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 09:06:28			Alafate			add test raise example
"""
import pytest


def test_raises():
    with pytest.raises(TypeError) as e:
        connect("localhost", "6379")
    exec_msg = e.value.args[0]
    assert exec_msg == "port type must be int"
