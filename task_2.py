# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print('Task_2')
print()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    lec_grades = {}
    

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def lect_rate(self, lecturer, course, lec_grade):
        if isinstance (lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [lec_grade]
            else:
                lecturer.lec_grades[course] = [lec_grade]
        else:
            return print('Ошибка')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка')
    
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
new_student = Student('Richard', 'o`Neil', 'male')
new_studentess = Student('Lisa', 'Doherty', 'female')
new_student.courses_in_progress += ['Python']
new_studentess.courses_in_progress += ['Python']
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
check_person = Reviewer('Bill', 'Johnes')
check_person.courses_attached = ['Python']
another_lecturer = Lecturer('Barry', 'Wyler')
another_lecturer.courses_attached += ['Python']
new_teacher = Lecturer('Ivan', 'Popov')
new_teacher.courses_attached += ['C++']
new_student.lect_rate(another_lecturer, 'Python', 10)
new_studentess.lect_rate(another_lecturer, 'Python', 10)
best_student.lect_rate(another_lecturer, 'Python', 10)
check_person.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(new_studentess, 'Python', 8)
check_person.rate_hw(new_student, 'Python', 10)
check_person.rate_hw(new_student, 'Python', 9)
check_person.rate_hw(new_student, 'Python', 10)
check_person.rate_hw(new_studentess, 'Python', 10)
check_person.rate_hw(new_studentess, 'Python', 10)

print(f'Рейтинг оценок {best_student.name} {best_student.surname}: {best_student.grades}')
print(f'Рейтинг оценок {new_student.name} {new_student.surname}: {new_student.grades}')
print(f'Рейтинг оценок {new_studentess.name} {new_studentess.surname}: {new_studentess.grades}')

print(f'Личный рейтинг преподавателя {another_lecturer.name} {another_lecturer.surname} {another_lecturer.lec_grades}')

print(f'Преподаватель {new_teacher.name} {new_teacher.surname} ведёт курс по программированию на {", ".join(new_teacher.courses_attached)}')
new_studentess.lect_rate(new_teacher, 'C++', 17) # для проверки
check_person.rate_hw(new_studentess, 'C++', 12) # для проверки

