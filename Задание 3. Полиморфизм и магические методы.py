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

    def average_grade(self):
        if self.grades:
            return sum([sum(grades) for grades in self.grades.values()]) / sum([len(grades) for grades in self.grades.values()])
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Атрибут для хранения оценок от студентов

    def average_grade(self):
        if self.grades:
            return sum([sum(grades) for grades in self.grades.values()]) / sum([len(grades) for grades in self.grades.values()])
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# Пример использования
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

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

# Вывод информации
print(best_student)
print(cool_lecturer)
print(cool_reviewer)

# Сравнение студентов и лекторов
print(best_student < Student('Another', 'Student', 'your_gender'))  # Пример сравнения студентов
print(cool_lecturer < Lecturer('Another', 'Lecturer'))  # Пример сравнения лекторов

#Метод __str__: Перегружен для всех классов, чтобы выводить информацию в требуемом формате.
#Метод average_grade: Добавлен в классы Student и Lecturer для вычисления средней оценки.
#Методы сравнения __lt__: Реализованы для классов Student и Lecturer, чтобы сравнивать их по средней оценке.

