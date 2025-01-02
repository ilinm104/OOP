# Задание № 3.2. Атрибуты и взаимодействие классов

class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_rating(self):
        rating = []
        for values in self.grades.values():
            for value in values:
                rating.append(value)
                self.average = sum(rating) / len(rating)
        return self.average

    def __str__(self):
        a = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        b = f'Средняя оценка за домашние задания: {self.average} \n'
        c = f'Курсы в процессе изучения: {self.courses_in_progress[0]}, {self.courses_in_progress[1]}\n'
        d = f'Завершенные курсы: {self.finished_courses[0]}'
        return a + b + c + d
        
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_to_lecturer = {}

    def rate_hw(self, student):
        if isinstance(student, Student):
            self.grades_to_lecturer = student.grades.copy()
        else:
            return 'Ошибка'

    def average_rating(self):
        rating = []
        for values in self.grades_to_lecturer.values():
            for value in values:
                rating.append(value)
                self.average = sum(rating) / len(rating)
        return self.average
    
    def __str__(self):
        a = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        b = f'Средняя оценка за лекции: {self.average}'
        return a + b


class Reviewer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

# Данные первого студента
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

# Данные второго студента
best_student_2 = Student('Sara', 'Conor', 'female')
best_student_2.courses_in_progress += ['Python', 'Git', 'Java']
best_student_2.finished_courses = ['Введение в программирование']

# Данные первого проверяющего
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']

# Данные второго проверяющего
cool_mentor_2 = Reviewer('Kate', 'Rose')
cool_mentor_2.courses_attached += ['Python', 'Git', 'Java']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Git', 10)

cool_mentor_2.rate_hw(best_student_2, 'Python', 10)
cool_mentor_2.rate_hw(best_student_2, 'Git', 10)
cool_mentor_2.rate_hw(best_student_2, 'Python', 9)
cool_mentor_2.rate_hw(best_student_2, 'Git', 10)
cool_mentor_2.rate_hw(best_student_2, 'Java', 9)
cool_mentor_2.rate_hw(best_student_2, 'Java', 10)

# Данные первого лектора
lecturer = Lecturer('Some', 'Buddy')
lecturer.rate_hw(best_student)

# Данные второго лектора
lecturer_2 = Lecturer('Kate', 'Rose')
lecturer_2.rate_hw(best_student_2)

some_reviewer = cool_mentor.__str__()
av_lec = lecturer.average_rating()

lecturer_2.average_rating()

some_lecturer = lecturer.__str__()
best_student.average_rating()
some_student = best_student.__str__()

best_student_2.average_rating()

# Функция для сравнения средних оценок за лекции между лекторами
def average_lec(lecturer, lecturer_2):
    if lecturer.average > lecturer_2.average:
        print(f'Средняя оценка за лекции {lecturer.name} {lecturer.surname} больше,')
        print(f'чем средняя оценка {lecturer_2.name} {lecturer_2.surname}')
    elif lecturer.average == lecturer_2.average:
        print(f'Средняя оценка за лекции {lecturer.name} {lecturer.surname} и {lecturer_2.name} {lecturer_2.surname} равны')
    else:
        print(f'Средняя оценка за лекции {lecturer_2.name} {lecturer_2.surname} больше,')
        print(f'чем средняя оценка {lecturer.name} {lecturer.surname}')

average_lec(lecturer, lecturer_2)

# Функция для сравнения средних оценок за домашние задания между студентами
def average_stud(best_student, best_student_2):
    if best_student.average > best_student_2.average:
        print(f'Средняя оценка за домашние задания {best_student.name} {best_student.surname} больше,')
        print(f'чем средняя оценка {best_student_2.name} {best_student_2.surname}')
    elif best_student.average == best_student_2.average:
        print(f'Средние оценки за домашние задания {best_student.name} {best_student.surname} и {best_student_2.name} {best_student_2.surname} равны')
    else:
        print(f'Средняя оценка за домашние задания {best_student_2.name} {best_student_2.surname} больше,')
        print(f'чем средняя оценка {best_student.name} {best_student.surname}')

average_stud(best_student, best_student_2)

# Функция для сравнения средних оценок за между студентом и лектором
def average_stud_lec(best_student, lecturer):
    if best_student.average > lecturer.average:
        print(f'Средняя оценка студента {best_student.name} {best_student.surname} больше,')
        print(f'чем средняя оценка лектора {lecturer.name} {lecturer.surname}')
    elif best_student.average == lecturer.average:
        print(f'Средние оценки студента {best_student.name} {best_student.surname} и лектора {lecturer.name} {lecturer.surname} равны')
    else:
        print(f'Средняя оценка лектора {lecturer.name} {lecturer.surname} больше,')
        print(f'чем средняя оценка студента {best_student.name} {best_student.surname}')

average_stud_lec(best_student, lecturer)





        
