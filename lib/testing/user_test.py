#!/usr/bin/env python3

from user import User

class TestUser:
    '''Class "User" in user.py'''

    def test_is_class(self):
        '''is a class.'''
        assert(object in User.__bases__)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_user = User("My", "User")
        assert((my_user.first_name, my_user.last_name) == ("My", "User"))
        