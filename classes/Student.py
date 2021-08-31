class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_dumb(self):
        return 'Yes' if self.name == 'Geverton' else 'No'
