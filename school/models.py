class Student:
    students = {}

    @staticmethod
    def create_student(student_id, name, age, grade):
        if student_id in Student.students:
            raise ValueError("Student already exists.")
        Student.students[student_id] = {'name': name, 'age': age, 'grade': grade}

    @staticmethod
    def get_student(student_id):
        return Student.students.get(student_id)

    @staticmethod
    def update_student(student_id, name=None, age=None, grade=None):
        if student_id not in Student.students:
            raise ValueError("Student does not exist.")
        if name:
            Student.students[student_id]['name'] = name
        if age:
            Student.students[student_id]['age'] = age
        if grade:
            Student.students[student_id]['grade'] = grade

    @staticmethod
    def delete_student(student_id):
        if student_id in Student.students:
            del Student.students[student_id]

class Teacher:
    teachers = {}

    @staticmethod
    def create_teacher(teacher_id, name, subject):
        if teacher_id in Teacher.teachers:
            raise ValueError("Teacher already exists.")
        Teacher.teachers[teacher_id] = {'name': name, 'subject': subject}

    @staticmethod
    def get_teacher(teacher_id):
        return Teacher.teachers.get(teacher_id)

    @staticmethod
    def update_teacher(teacher_id, name=None, subject=None):
        if teacher_id not in Teacher.teachers:
            raise ValueError("Teacher does not exist.")
        if name:
            Teacher.teachers[teacher_id]['name'] = name
        if subject:
            Teacher.teachers[teacher_id]['subject'] = subject

    @staticmethod
    def delete_teacher(teacher_id):
        if teacher_id in Teacher.teachers:
            del Teacher.teachers[teacher_id]
