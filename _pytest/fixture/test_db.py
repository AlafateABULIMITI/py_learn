"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture/test_db.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/fixture
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:

there is a need for preprocessing (e.g. new database connection) before testing and cleaning up (closing database connection) when testing is complete.

When there is a lot of duplication of such operations, best practice is to use firmware to automate all pre-processing and post-processing.

Pytest uses the `yield` keyword to divide the firmware into two parts, the code before `yield` is pre-processing and will be executed before the test, and the code after `yield` is post-processing and will be executed after the test is completed.

--------------
Last Modified: Sunday May 10th 2020 10:02:46 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 10:08:20			Alafate			add db funcs and `yield` keyword
"""

import pytest


@pytest.fixture()
def db():
    print("Connection successful")
    yield
    print("Connection closed")


def search_user(user_id):
    d = {"001": "aa"}
    return d[user_id]


def test_search_user(db):
    assert search_user("001") == "aa"
