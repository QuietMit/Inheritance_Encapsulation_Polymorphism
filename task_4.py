# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print('Task_4')
print()


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lect_rate(self, lecturer, course, lec_grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [lec_grade]
            else:
                lecturer.grades[course] = [lec_grade]
        else:
            return print('Ошибка')

    def avg_grade(self):
        return Mentor.avg_grade(self)


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\nKурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: Введение в программирование'

    def __gt__(self, other):
        if not isinstance(other, Student):
            return f'{other.name} {other.surname} is not a student!'
        if self.avg_grade() > other.avg_grade():
            return f'{self.name} {self.surname} победил по среднему баллу {other.name} {other.surname}'
        else:
            return f'{self.name} {self.surname} проиграл по среднему баллу {other.name} {other.surname}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def avg_grade(self):
        grade_list = list(self.grades.items())
        for tuple in grade_list:
            grade = 0
            leng = 0
            for key, value in grade_list:
                grade += sum(value)
                leng += len(value)
        return round(grade / leng, 2)


class Lecturer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return f'{other.name} {other.surname} is not a Lecturer!'
        if self.avg_grade() > other.avg_grade():
            return f'{self.name} {self.surname} победил по среднему баллу {other.name} {other.surname}'
        else:
            return f'{self.name} {self.surname} проиграл по среднему баллу {other.name} {other.surname}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


st_list = []


def av_hw_rate_by_the_course(student_list, course):
    avg_mark = 0
    marks_quantity = 0
    for student in student_list:
        avg_mark += sum(student.grades[course])
        marks_quantity += len(student.grades[course])
    return f'''Средняя оценка за домашнюю работу
по всем студентам курса {course}: {round((avg_mark / marks_quantity), 2)}'''


lec_list = []


def lec_rate_by_the_course(lecturer_list, course):
    avg_mark = 0
    marks_quantity = 0
    for lecturer in lecturer_list:
        avg_mark += sum(lecturer.grades[course])
        marks_quantity += len(lecturer.grades[course])
    return f'''Средняя оценка лекторам за лекции
по курсу {course}: {round((avg_mark / marks_quantity), 2)}'''


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
new_student = Student('Richard', 'o`Neil', 'male')
new_studentess = Student('Lisa', 'Doherty', 'female')
new_student.courses_in_progress += ['Python', 'C++']
new_studentess.courses_in_progress += ['Python', 'C++']
st_list = [best_student, new_student, new_studentess]
cpp_list = [new_student, new_studentess]
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
just_mentor = Mentor('Carl', 'Muller')
just_mentor.courses_attached += ['Python', 'Git', 'C++']
check_person = Reviewer('Bill', 'Johnes')
new_reviewer = Reviewer('Darya', 'Alekseeva')
check_person.courses_attached = ['Python']
new_reviewer.courses_attached += ['Git', 'C++']
another_lecturer = Lecturer('Barry', 'Wyler')
another_lecturer.courses_attached += ['Python']
new_teacher = Lecturer('Ivan', 'Popov')
new_teacher.courses_attached += ['Python']
lec_list = [another_lecturer, new_teacher]
new_student.lect_rate(another_lecturer, 'Python', 10)
new_studentess.lect_rate(another_lecturer, 'Python', 10)
best_student.lect_rate(another_lecturer, 'Python', 10)
new_student.lect_rate(new_teacher, 'Python', 10)
new_studentess.lect_rate(new_teacher, 'Python', 10)
best_student.lect_rate(new_teacher, 'Python', 9)
check_person.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(new_studentess, 'Python', 8)
check_person.rate_hw(new_student, 'Python', 10)
check_person.rate_hw(new_student, 'Python', 9)
check_person.rate_hw(new_student, 'Python', 10)
check_person.rate_hw(new_studentess, 'Python', 10)
check_person.rate_hw(new_studentess, 'Python', 10)
new_reviewer.rate_hw(new_student, 'C++', 6)
new_reviewer.rate_hw(new_studentess, 'C++', 9)
new_reviewer.rate_hw(new_student, 'C++', 10)
new_reviewer.rate_hw(new_studentess, 'C++', 10)
new_reviewer.rate_hw(new_student, 'C++', 10)
new_reviewer.rate_hw(new_studentess, 'C++', 10)
new_reviewer.rate_hw(new_student, 'C++', 8)
new_reviewer.rate_hw(new_studentess, 'C++', 8)
new_reviewer.rate_hw(new_student, 'C++', 10)
new_reviewer.rate_hw(new_studentess, 'C++', 9)
new_reviewer.rate_hw(new_student, 'C++', 9)
new_reviewer.rate_hw(new_studentess, 'C++', 10)

print()
print(cool_mentor.name)
print(cool_mentor.surname)
print
print(just_mentor.name)
print(just_mentor.surname)
print()
print(check_person)
print()
print(new_reviewer)
print()
print(another_lecturer)
print()
print(new_teacher)
print()
print(new_student)
print()
print(new_studentess)
print()
print(best_student)
print()
print(best_student > new_student)
print(new_studentess > new_student)
print()
print(another_lecturer > new_teacher)
print(new_teacher > new_reviewer)
print(new_teacher > another_lecturer)
print()
print(best_student.grades)
print(new_student.grades)
print(new_studentess.grades)
print()
print(new_student.avg_grade())
print(new_studentess.avg_grade())
print()
print(av_hw_rate_by_the_course(st_list, 'Python'))
print(av_hw_rate_by_the_course(cpp_list, 'C++'))
print(lec_rate_by_the_course(lec_list, 'Python'))
