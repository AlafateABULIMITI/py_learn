"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/test_xfail.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:
If we know in advance that the test function will fail to execute, but don't want to skip it directly, but instead of the hint displayed.Pytest uses pytest.mark.xfail to implement predictive error functionality
--------------
Last Modified: Sunday May 10th 2020 09:32:22 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 09:36:51			Alafate			add test_api and @mark.xfail
"""

import pytest


@pytest.mark.xfail(gen.__version__ < "0.2.0", reason="not supported until v0.2.0")
def test_api():
    id_1 = gen.unique_id()
    id_2 = gen.unique_id()
    assert id_1 != id_2
