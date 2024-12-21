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

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_student_grade(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grade / count if count > 0 else 0

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecturer_grade(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grade / count if count > 0 else 0

# Пример использования
# Создаем студентов
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Anna', 'Smith', 'female')
student2.courses_in_progress += ['Python', 'Data Science']
student2.finished_courses += ['Математика']

# Создаем лекторов
lecturer1 = Lecturer('John', 'Doe')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Alice', 'Johnson')
lecturer2.courses_attached += ['Data Science']

# Создаем проверяющих
reviewer1 = Reviewer('Jane', 'Smith')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Mark', 'Brown')
reviewer2.courses_attached += ['Data Science']

# Оценка домашнего задания
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student1, 'Data Science', 9)
reviewer2.rate_hw(student2, 'Data Science', 10)

# Студенты выставляют оценки лекторам
student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer2, 'Data Science', 9)

student2.rate_lecture(lecturer1, 'Python', 7)
student2.rate_lecture(lecturer2, 'Data Science', 10)

# Вывод информации
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Подсчет средней оценки за домашние задания по курсу 'Python'
average_student_python = average_student_grade([student1, student2], 'Python')
print(f"Средняя оценка за домашние задания по курсу 'Python': {average_student_python:.1f}")

# Подсчет средней оценки за лекции по курсу 'Data Science'
average_lecturer_data_science = average_lecturer_grade([lecturer1, lecturer2], 'Data Science')
print(f"Средняя оценка за лекции по курсу 'Data Science': {average_lecturer_data_science:.1f}")


#Создание экземпляров: Созданы два экземпляра для каждого класса (Student, Lecturer, Reviewer).
#Функции для подсчета средней оценки:
#average_student_grade: Подсчитывает среднюю оценку за домашние задания по всем студентам для указанного курса.
#average_lecturer_grade: Подсчитывает среднюю оценку за лекции всех лекторов для указанного курса.
#Пример использования: Вызваны все методы, и выведена информация о студентах, лекторах и проверяющих, а также рассчитаны средние оценки.
