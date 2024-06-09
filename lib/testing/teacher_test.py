#!/usr/bin/env python3

from teacher import Teacher
from user import User

class TestTeacher:
    '''Class "Teacher" in teacher.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert(User in Teacher.__bases__)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_teacher = Teacher("My", "Teacher")
        assert((my_teacher.first_name, my_teacher.last_name) == ("My", "Teacher"))

    def test_has_attribute_knowledge(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        my_teacher = Teacher("My", "Teacher")
        # Define a list of topics to be taught
        topics_to_teach = ["Math", "Science"]
        # Call the teach method with the topics_to_teach argument
        my_teacher.teach(topics_to_teach)
        # Verify the contents of my_teacher.knowledge
        assert isinstance(my_teacher.knowledge, list), "knowledge is not a list"
        assert len(my_teacher.knowledge) > 0, "knowledge list is empty"
        assert all(topic in my_teacher.knowledge for topic in topics_to_teach), "Not all topics are in knowledge"

# Assuming the rest of the code is correctly implemented elsewhere
