"""
File: /Users/alafateabulimiti/Documents/projects/py_learn/unittest/calculator.py
Project: /Users/alafateabulimiti/Documents/projects/py_learn/unittest
Created Date: Saturday May 9th 2020
Author: Alafate ABULIMITI
Description:
Python unittest example
--------------
Last Modified: Saturday May 9th 2020 06:01:18 pm
Modified By: the developer formerly known as Alafate ABULIMITI at alafate.abulimiti@gmail.com
--------------
HISTORY:
Date						By				Comments
----------------			-----			-----------------------------------------------------------------

9-05-2020 06:05:26			Alafate			add the Count class
"""


class Count:
    def __init__(self, a, b):
        super().__init__()
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b
