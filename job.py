#Домашнее задание к лекции «Объекты и классы. Инкапсуляция, наследование и полиморфизм»

#Задание № 1. Наследование

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Reviewer(Mentor):
    def check_hw(self, student, course):
        print(f'Проверка домашнего задания {student.name} {student.surname} по курсу {course}')

# Создаем объекты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Another', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# Лектор выставляет оценки
cool_lecturer.rate_hw(best_student, 'Python', 10)
cool_lecturer.rate_hw(best_student, 'Python', 10)
cool_lecturer.rate_hw(best_student, 'Python', 10)

# Проверяющий проверяет домашнюю работу
cool_reviewer.check_hw(best_student, 'Python')

# Выводим оценки студента
print(best_student.grades)




#Задание № 2. Атрибуты и взаимодействие классов.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecture_grades = {}  # Словарь для хранения оценок за лекции

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        """Метод для выставления оценки лектору"""
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
        self.grades = {}  # Словарь для хранения оценок за лекции


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Метод для выставления оценки за домашнее задание"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создаем объекты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Another', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# Оцениваем лекцию
best_student.rate_lecture(cool_lecturer, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 8)

# Рецензент выставляет оценки за домашнее задание
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Выводим оценки студента и лектора
print("Оценки студента:", best_student.grades)
print("Оценки лектора:", cool_lecturer.grades)



#Задание № 3. Полиморфизм и магические методы

#Перегрузите магический метод __str__ у всех классов.

class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer:
    def __init__(self, name, surname, average_grade=0.0):
        self.name = name
        self.surname = surname
        self.average_grade = average_grade

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average_grade:.1f}"
        )

class Student:
    def __init__(
        self,
        name,
        surname,
        average_hw_grade=0.0,
        courses_in_progress=[],
        finished_courses=[],
    ):
        self.name = name
        self.surname = surname
        self.average_hw_grade = average_hw_grade
        self.courses_in_progress = courses_in_progress
        self.finished_courses = finished_courses

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average_hw_grade:.1f}\n"
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

# Создаем объекты
reviewer = Reviewer("Some", "Buddy")
lecturer = Lecturer("Some", "Buddy", 9.9)
student = Student(
    "Ruoy", "Eman", 9.9, ["Python", "Git"], ["Introduction to Programming"]
)

# Выводим информацию об объектах
print(reviewer)
print()
print(lecturer)
print()
print(student)



#Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

class Lecturer:
    def __init__(self, name, surname, average_grade=0.0):
        self.name = name
        self.surname = surname
        self.average_grade = average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(
                f"'<' not supported between instances of 'Lecturer' and '{type(other).__name__}'"
            )
        return self.average_grade < other.average_grade

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(
                f"'<=' not supported between instances of 'Lecturer' and '{type(other).__name__}'"
            )
        return self.average_grade <= other.average_grade

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(
                f"'==' not supported between instances of 'Lecturer' and '{type(other).__name__}'"
            )
        return self.average_grade == other.average_grade

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(
                f"'>=' not supported between instances of 'Lecturer' and '{type(other).__name__}'"
            )
        return self.average_grade >= other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(
                f"'>' not supported between instances of 'Lecturer' and '{type(other).__name__}'"
            )
        return self.average_grade > other.average_grade

class Student:
    def __init__(
        self,
        name,
        surname,
        average_hw_grade=0.0,
        courses_in_progress=[],
        finished_courses=[],
    ):
        self.name = name
        self.surname = surname
        self.average_hw_grade = average_hw_grade
        self.courses_in_progress = courses_in_progress
        self.finished_courses = finished_courses

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError(
                f"'<' not supported between instances of 'Student' and '{type(other).__name__}'"
            )
        return self.average_hw_grade < other.average_hw_grade

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError(
                f"'<=' not supported between instances of 'Student' and '{type(other).__name__}'"
            )
        return self.average_hw_grade <= other.average_hw_grade

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError(
                f"'==' not supported between instances of 'Student' and '{type(other).__name__}'"
            )
        return self.average_hw_grade == other.average_hw_grade

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError(
                f"'>=' not supported between instances of 'Student' and '{type(other).__name__}'"
            )
        return self.average_hw_grade >= other.average_hw_grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError(
                f"'>' not supported between instances of 'Student' and '{type(other).__name__}'"
            )
        return self.average_hw_grade > other.average_hw_grade

# Сравним двух лекторов
lecturer1 = Lecturer("Иван", "Иванов", 8.7)
lecturer2 = Lecturer("Петр", "Петров", 9.4)

if lecturer1 < lecturer2:
    print("Иван Иванов имеет меньшую среднюю оценку за лекции, чем Петр Петров.")
else:
    print(
        "Иван Иванов имеет большую или равную среднюю оценку за лекции, чем Петр Петров."
    )

# Сравним двух студентов
student1 = Student("Анна", "Сидорова", 8.6, ["Python", "Git"], [])
student2 = Student("Елена", "Васильева", 9.2, ["JavaScript", "SQL"], [])

if student1 < student2:
    print("Анна Сидорова имеет меньшую среднюю оценку за домашние задания, чем Елена Васильева."  )
else:
    print ("Анна Сидорова имеет большую или равную среднюю оценку за домашние задания, чем Елена Васильева.")



#Задание № 4. Полевые испытания

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, course_name, grade):
        if course_name not in self.grades:
            self.grades[course_name] = []
        self.grades[course_name].append(grade)

    def get_grades_for_course(self, course_name):
        return self.grades.get(course_name, [])

class Lecturer:
    def __init__(self, name):
        self.name = name
        self.ratings = {}

    def add_rating(self, course_name, rating):
        if course_name not in self.ratings:
            self.ratings[course_name] = []
        self.ratings[course_name].append(rating)

    def get_ratings_for_course(self, course_name):
        return self.ratings.get(course_name, [])

# Создаем двух студентов
student1 = Student("Иван Иванов")
student2 = Student("Петр Петров")

# Добавляем оценки для студентов
student1.add_grade("Python", 4)
student1.add_grade("Python", 5)
student1.add_grade("Java", 3)

student2.add_grade("Python", 5)
student2.add_grade("Java", 4)

# Создаем двух лекторов
lecturer1 = Lecturer("Сергей Сергеев")
lecturer2 = Lecturer("Анна Андреева")

# Добавляем рейтинги для лекторов
lecturer1.add_rating("Python", 9)
lecturer1.add_rating("Python", 8)
lecturer1.add_rating("Java", 7)

lecturer2.add_rating("Python", 10)
lecturer2.add_rating("Java", 6)

def average_student_grade(students, course_name):
    grades_sum = 0
    grades_count = 0

    for student in students:
        grades = student.get_grades_for_course(course_name)
        grades_sum += sum(grades)
        grades_count += len(grades)

    if grades_count == 0:
        return None

    return grades_sum / grades_count

def average_lecturer_rating(lectors, course_name):
    ratings_sum = 0
    ratings_count = 0

    for lecturer in lectors:
        ratings = lecturer.get_ratings_for_course(course_name)
        ratings_sum += sum(ratings)
        ratings_count += len(ratings)

    if ratings_count == 0:
        return None

    return ratings_sum / ratings_count

students = [student1, student2]
lectors = [lecturer1, lecturer2]

print(
    f"Средняя оценка студентов по курсу 'Python': {average_student_grade(students, 'Python')}"
)
print(
    f"Средний рейтинг лекторов по курсу 'Python': {average_lecturer_rating(lectors, 'Python')}"
)
