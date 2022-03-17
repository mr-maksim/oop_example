class People:
    def __init__(self, name, sure_name):
        self.name = name
        self.sure_name = sure_name


class Mentor(People):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.fixed_courses = []

class Reviewer(Mentor):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.fixed_courses = []


class Lecturer(Mentor):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.fixed_courses = []
        self.assessment = []


class Student(People):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.finished_courses = []
        self.assessment = []
