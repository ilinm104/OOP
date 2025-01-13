#             № 1


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
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


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
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


# Создаем объекты
best_student = Student("Ruoy", "Eman", "your_gender")
best_student.courses_in_progress += ["Python"]

cool_lecturer = Lecturer("Some", "Buddy")
cool_lecturer.courses_attached += ["Python"]

cool_reviewer = Reviewer("Another", "Buddy")
cool_reviewer.courses_attached += ["Python"]

# Оцениваем лекцию
best_student.rate_lecture(cool_lecturer, "Python", 9)
best_student.rate_lecture(cool_lecturer, "Python", 10)
best_student.rate_lecture(cool_lecturer, "Python", 8)

# Рецензент выставляет оценки за домашнее задание
cool_reviewer.rate_hw(best_student, "Python", 10)
cool_reviewer.rate_hw(best_student, "Python", 10)
cool_reviewer.rate_hw(best_student, "Python", 10)

# Выводим оценки студента и лектора
# print("Оценки студента:", best_student.grades)
print("Оценки лектора:", cool_lecturer.grades)


#                    № 2


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
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course(self, course):
        self.courses_attached.append(course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок за лекции


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Метод для выставления оценки за домашнее задание"""
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


# Создаем объекты
best_student = Student("Руслан", "Еманов", "Мужской")
best_student.courses_in_progress += ["Python"]

cool_lecturer = Lecturer("Иван", "Иванов")
cool_lecturer.add_course("Python")  # добавляем курс для лектора

cool_reviewer = Reviewer("Петр", "Петров")
cool_reviewer.add_course("Python")  # добавляем курс для рецензента

# Оцениваем лекцию
best_student.rate_lecture(cool_lecturer, "Python", 9)
best_student.rate_lecture(cool_lecturer, "Python", 10)
best_student.rate_lecture(cool_lecturer, "Python", 8)

# Рецензент выставляет оценки за домашнее задание
cool_reviewer.rate_hw(best_student, "Python", 10)
cool_reviewer.rate_hw(best_student, "Python", 10)
cool_reviewer.rate_hw(best_student, "Python", 10)

# Выводим оценки студента и лектора
print(f"Оценки студента: {best_student.grades}")
print(f"Оценки лектора: {cool_lecturer.grades}")

#                   №    3.1


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


#                   3.2


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

    # Метод для получения средней оценки студента
    def get_average_grade(self):
        total_grades = 0
        num_courses = 0

        for course, grades in self.grades.items():
            total_grades += sum(grades)
            num_courses += len(grades)

        if num_courses == 0:
            return 0

        return total_grades / num_courses

    # Операторы сравнения
    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()


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

    # Метод для получения среднего рейтинга лектора
    def get_average_rating(self):
        total_ratings = 0
        num_courses = 0

        for course, ratings in self.ratings.items():
            total_ratings += sum(ratings)
            num_courses += len(ratings)

        if num_courses == 0:
            return 0

        return total_ratings / num_courses

    # Операторы сравнения
    def __lt__(self, other):
        return self.get_average_rating() < other.get_average_rating()

    def __le__(self, other):
        return self.get_average_rating() <= other.get_average_rating()

    def __eq__(self, other):
        return self.get_average_rating() == other.get_average_rating()

    def __ge__(self, other):
        return self.get_average_rating() >= other.get_average_rating()

    def __gt__(self, other):
        return self.get_average_rating() > other.get_average_rating()


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

# Проверка операторов сравнения для студентов
if student1 < student2:
    print(f"{student1.name} имеет меньшую среднюю оценку, чем {student2.name}")
elif student1 > student2:
    print(f"{student1.name} имеет большую среднюю оценку, чем {student2.name}")
else:
    print(f"{student1.name} и {student2.name} имеют одинаковую среднюю оценку")

# Проверка операторов сравнения для лекторов
if lecturer1 < lecturer2:
    print(f"{lecturer1.name} имеет меньший средний рейтинг, чем {lecturer2.name}")
elif lecturer1 > lecturer2:
    print(f"{lecturer1.name} имеет больший средний рейтинг, чем {lecturer2.name}")
else:
    print(f"{lecturer1.name} и {lecturer2.name} имеют одинаковый средний рейтинг")


#                        №  4


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
