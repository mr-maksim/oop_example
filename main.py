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

    def add_course(self, student, course_name):
        if course_name in self.fixed_courses:
            student.courses[course_name] = []

    def close_course(self, student, course_name):
        if course_name in self.fixed_courses:
            if course_name in student.courses:
                del student.courses[course_name]


class Reviewer(Mentor):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.fixed_courses = []

    def put_assessment(self, course_name, student, assessment=10):
        if course_name in self.fixed_courses:
            student.courses[course_name].append(assessment)


class Lecturer(Mentor):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.fixed_courses = {}

    def __str__(self) -> str:
        result = 0
        try:
            for course_assessment in self.fixed_courses.values():
                result = result + sum(course_assessment)/len(course_assessment)
            score = result / len(self.fixed_courses.values())
        except:
            score = "Лектор не получал оценки!"
        return super().__str__() + f'\nСредняя оценка за лекции: {score}'

    def __lt__(self, lecturer_2):
        result = 0
        result_2 = 0
        try:
            for course_assessment in self.fixed_courses.values():
                result = result + sum(course_assessment)/len(course_assessment)
            score = result / len(self.fixed_courses.values())
            for course_assessment in lecturer_2.fixed_courses.values():
                result_2 = result_2 + \
                    sum(course_assessment)/len(course_assessment)
            score_2 = result_2 / len(lecturer_2.fixed_courses.values())
        except:
            score = "Ошибка сравнения!"
            return score
        return score < score_2


class Student(People):
    def __init__(self, name, sure_name):
        super().__init__(name, sure_name)
        self.courses = {}
        self.finished_courses = []

    def __str__(self) -> str:
        result = 0
        try:
            for course_assessment in self.courses.values():
                result = result + sum(course_assessment)/len(course_assessment)
            score = result / len(self.courses.values())
        except:
            score = "Ученик не заработал ни одной оценки!"
        return super().__str__() + f'\nСредняя оценка за домашние задания: {score}\nКурсы в процессе изучения: {", ".join(self.courses)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, student_2):
        result = 0
        result_2 = 0
        try:
            for course_assessment in self.courses.values():
                result = result + sum(course_assessment)/len(course_assessment)
            score = result / len(self.courses.values())
            for course_assessment in student_2.courses.values():
                result_2 = result_2 + \
                    sum(course_assessment)/len(course_assessment)
            score_2 = result_2 / len(student_2.courses.values())
        except:
            score = "Ошибка сравнения!"
            return score
        return score < score_2

    def put_assessment(self, course_name, lecturer, assessment=10):
        if course_name in lecturer.fixed_courses and course_name in self.courses:
            lecturer.fixed_courses[course_name].append(assessment)


# Создание проверяющих
some_reviewer_1 = Reviewer("Петр", "Петров")
some_reviewer_2 = Reviewer("Иван", "Иванов")

# Создание Лекторов
some_lecturer_1 = Lecturer("Вова", "Вовочкин")
some_lecturer_2 = Lecturer("Василий", "Васильев")

# Создание Студентов
some_student_1 = Student("Татьяна", "Танечкина")
some_student_2 = Student("Нина", "Ниночкина")

# Закрепление курсов проверяющих
some_reviewer_1.fixed_courses.append('Python')
some_reviewer_1.fixed_courses.append("Git")
some_reviewer_2.fixed_courses.append('Python')
some_reviewer_2.fixed_courses.append("Git")

# Закрепление курсов лекторов
some_lecturer_1.fixed_courses["Python"] = []
some_lecturer_1.fixed_courses["Git"] = []
some_lecturer_2.fixed_courses["Python"] = []
some_lecturer_2.fixed_courses["Git"] = []

# Закрепление курсов студентов
some_student_1.courses["Python"] = []
some_student_1.courses["Git"] = []
some_student_2.courses["Python"] = []
some_student_2.courses["Git"] = []

# Закрепление заверщенных курсов студентов
some_student_1.finished_courses.append("Введение в программирование")
some_student_2.finished_courses.append("Введение в программирование")

# Выставление оценок лекторам
some_student_1.put_assessment("Python", some_lecturer_1, 5)
some_student_1.put_assessment("Python", some_lecturer_1, 7)
some_student_1.put_assessment("Git", some_lecturer_1, 9)
some_student_1.put_assessment("Git", some_lecturer_1, 7)

some_student_1.put_assessment("Python", some_lecturer_2, 5)
some_student_1.put_assessment("Python", some_lecturer_2, 5)
some_student_1.put_assessment("Git", some_lecturer_2, 9)
some_student_1.put_assessment("Git", some_lecturer_2, 7)

# Выставление оценок студентам
some_reviewer_1.put_assessment("Python", some_student_1, 4)
some_reviewer_1.put_assessment("Git", some_student_1, 5)
some_reviewer_2.put_assessment("Python", some_student_2, 9)
some_reviewer_2.put_assessment("Git", some_student_2, 3)

print(f'{"*"*15}__STR__{"*"*15}')
print(f'{some_reviewer_1}\n{"-"*15}\n{some_lecturer_1}\n{"-"*15}\n{some_student_1}\n{"-"*15}\n\n')

print(f'{"*"*15} Сравнение лекторов {"*"*15}')
print(some_lecturer_2 > some_lecturer_1)
print(some_lecturer_2 < some_lecturer_1)
print(f'{"-"*15}\n\n')

print(f'{"*"*15} Сравнение студентов {"*"*15}')
print(some_student_1 > some_student_2)
print(some_student_1 < some_student_2)
print(f'{"-"*15}\n\n')

# Списки для функций расчета средней оценки
lecturer_list = [some_lecturer_1, some_lecturer_2]
student_list = [some_student_1, some_student_2]


def lecturer_score(lecturer_list, course_name):
    result = 0
    count = 0
    for lecturer in lecturer_list:
        for assessment in lecturer.fixed_courses[course_name]:
            result = result + assessment
            count += 1
    score = result / count
    return f'Средняя оценка: {score}'


def student_score(student_list, course_name):
    result = 0
    count = 0
    for student in student_list:
        for assessment in student.courses[course_name]:
            result = result + assessment
            count += 1
    score = result / count
    return f'Средняя оценка: {score}'


print(f'{"*"*15} Расчет средней оценки {"*"*15}')
print(lecturer_score(lecturer_list, 'Python'))
print(student_score(student_list, 'Python'))
