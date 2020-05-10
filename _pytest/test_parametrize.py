"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest/test_parametrize.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_pytest
Created Date: Sunday May 10th 2020
Author: Alafate ABULIMITI
Description:
When a test function is tested, multiple sets of parameters are usually passed to the function. For example, to test an account login, we need to simulate a variety of strange account passwords.

Of course, we can write these parameters to iterate inside the test function. But although the parameters are numerous, it is still a test, and when a set of parameters causes an assertion to fail, the test is terminated.

With exception capture, we can ensure that all program parameters are fully executed, but analyzing the test results requires a lot of extra work.

In Pytest, we have a better solution in the form of parametric testing, where each set of parameters performs a test independently. The tool used is `pytest.mark.parametrize(argnames, argvalues)`

--------------
Last Modified: Sunday May 10th 2020 09:37:15 am
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

10-05-2020 09:44:26			Alafate			add test funcs and @mark.parametrize
"""
import pytest
import hashlib


@pytest.mark.parametrize(
    "passwd", ["dsdsadasdasd", "dsda2324", "d7543vytrw2c", "dssdsdsadsad"]
)
def test_passwd_length(passwd):
    assert len(passwd) <= 8


@pytest.mark.parametrize("user, passwd", [("jack", "abcdefgh"), ("tom", "a123456a")])
def test_passwd_md5(user, passwd):
    db = {
        "jack": "e8dc4081b13434b45189a720b77b6818",
        "tom": "1702a132e769a623c1adb78353fc9503",
    }
    assert hashlib.md5(passwd.encode()).hexdigest() == db[user]
