#!/usr/bin/env python

# teacher.py

from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def teach(self, topics):
        """Adds topics to the teacher's knowledge."""
        self.knowledge.extend(topics)


