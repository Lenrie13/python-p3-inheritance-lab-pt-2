# test_student.py

import pytest
from student import Student
import io
import sys

class TestStudent:
    def test_hello(self):
        '''Tests the hello method in Student class.'''
        captured_output = io.StringIO()
        sys.stdout = captured_output
        student = Student()
        student.hello()
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue().strip() == "Hey there! I'm so excited to learn stuff."
    
    def test_raise_hand(self):
        '''Tests the raise_hand method in Student class.'''
        captured_output = io.StringIO()
        sys.stdout = captured_output
        student = Student()
        student.raise_hand()
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue().strip() == "Pick me!"
