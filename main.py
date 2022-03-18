class People:
    def __init__(self, name, sure_name):
        self.name = name
        self.sure_name = sure_name

    def __str__(self) -> str:
        message = f'Имя: {self.name}\nФамилия: {self.sure_name}'
        return message


class Mentor(People):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        # self.fixed_courses = ['py']

    def add_course(self, student, course_name):
        student.courses[course_name] = []

    def close_course(self, student, course_name):
        if course_name in student.courses:
            del student.courses[course_name]


class Reviewer(Mentor):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.fixed_courses = []

    def put_assessment(self, course_name, student):
        pass


class Lecturer(Mentor):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.fixed_courses = {}

    def __str__(self) -> str:
        try:
            score = sum(self.assessment)/len(self.assessment)
        except:
            score = "Лектор не получал оценки!"
        return super().__str__() + f'\nСредняя оценка за лекции: {score}'


class Student(People):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.courses = {}

    def __str__(self) -> str:
        try:
            score = sum(self.assessment)/len(self.assessment)
        except:
            score = "Ученик не заработал ни одной оценки!"
        return super().__str__() + f'\nСредняя оценка за домашние задания: {score} {self.courses}'


