class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Атрибут для хранения оценок от студентов

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Пример использования
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# Создаем экземпляры Lecturer и Reviewer
cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Jane', 'Smith')
cool_reviewer.courses_attached += ['Python']

# Оценка домашнего задания
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)

# Студент выставляет оценку лектору
best_student.rate_lecture(cool_lecturer, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'Python', 9)

print(best_student.grades)  # Оценки студента
print(cool_lecturer.grades)  # Оценки лектора

#Метод rate_lecture в классе Student: Позволяет студенту выставлять оценки лекторам за лекции, если лектор закреплен за курсом, на который записан студент.
#Метод rate_hw в классе Reviewer: Оставлен для выставления оценок студентам за домашние задания
#Метод rate_lecture в классе Student: Позволяет студенту выставлять оценки лекторам за лекции, если лектор закреплен за курсом, на который записан студент.
#Метод rate_hw в классе Reviewer: Оставлен для выставления оценок студентам за домашние задания