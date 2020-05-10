"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/test_skip.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:
test skip func
--------------
Last Modified: Sunday May 10th 2020 09:11:00 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 09:14:33			Alafate			add mark skip and mark skipif funcs
"""

import pytest


@pytest.mark.skip(reason="out-of-date api")
def test_connect():
    pass


@pytest.mark.skipif(conn.__version__ < "0.2.2", reason="not supported until v0.2.2")
def test_api():
    pass
