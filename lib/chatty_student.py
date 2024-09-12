# chatty_student.py

from student import Student

class ChattyStudent(Student):
    def hello(self):
        '''Prints out the parent class greeting and adds more chatty content.'''
        super().hello()  # Call the hello method from Student
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    def raise_hand(self):
        '''Calls the parent class raise_hand method ten times.'''
        for _ in range(10):
            super().raise_hand()  # Call the raise_hand method from Student
