# test_chatty_student.py

import pytest
from chatty_student import ChattyStudent
import io
import sys

class TestChattyStudent:
    def test_hello(self):
        '''Tests the hello method in ChattyStudent class.'''
        captured_output = io.StringIO()
        sys.stdout = captured_output
        chatty_student = ChattyStudent()
        chatty_student.hello()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip().split("\n")
        assert output[0] == "Hey there! I'm so excited to learn stuff."
        assert output[1] == "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
    
    def test_raise_hand(self):
        '''Tests the raise_hand method in ChattyStudent class.'''
        captured_output = io.StringIO()
        sys.stdout = captured_output
        chatty_student = ChattyStudent()
        chatty_student.raise_hand()
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue().strip().split("\n").count("Pick me!") == 10
