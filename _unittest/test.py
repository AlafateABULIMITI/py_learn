"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/_unittest/test.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/_unittest
Created Date: Saturday May 9th 2020
Author: Alafate ABULIMITI
Description:
Basic test file for example calculator
--------------
Last Modified: Saturday May 9th 2020 06:06:08 pm
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

9-05-2020 06:15:0			Alafate			add TestAdd class for the "calculator" file
"""

from calculator import Count
import unittest


class TestAdd(unittest.TestCase):
    # The method is used to initialize the test case before execution.
    def setup(self):
        print("test start")

    # test method
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5, "wrong calculation")

    #The `tearDown()` method corresponds to `setUp()` and is used to test what happens after the use case.
    def tearDown(self):
        print("test end")


if __name__ == "__main__":
    # construct test suite
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    # run test runner
    runner = unittest.TextTestRunner()
    runner.run(suite)
