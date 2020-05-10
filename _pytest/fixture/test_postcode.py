"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture/test_postcode.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:

Fixtures are functions that pytest loads to run before (or after) executing the test function.

We can do anything with firmware, probably the most common of which is the initial connection to the database and the final closure operation.

Pytest uses `pytest.fixture()` to define the firmware
--------------
Last Modified: Sunday May 10th 2020 09:54:05 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 10:02:1			Alafate			add @pytest.fixture
"""

import pytest


@pytest.fixture()
def postcode():
    return "75000"


def test_postcode(postcode):
    assert postcode == "75000"
