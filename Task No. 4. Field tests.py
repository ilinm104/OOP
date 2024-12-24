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
