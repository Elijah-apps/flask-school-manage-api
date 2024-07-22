from flask_restful import Resource, reqparse
from school.models import Student, Teacher

student_parser = reqparse.RequestParser()
student_parser.add_argument('name', type=str, required=True, help="Name cannot be blank!")
student_parser.add_argument('age', type=int, required=True, help="Age cannot be blank!")
student_parser.add_argument('grade', type=str, required=True, help="Grade cannot be blank!")

update_student_parser = reqparse.RequestParser()
update_student_parser.add_argument('name', type=str)
update_student_parser.add_argument('age', type=int)
update_student_parser.add_argument('grade', type=str)

teacher_parser = reqparse.RequestParser()
teacher_parser.add_argument('name', type=str, required=True, help="Name cannot be blank!")
teacher_parser.add_argument('subject', type=str, required=True, help="Subject cannot be blank!")

update_teacher_parser = reqparse.RequestParser()
update_teacher_parser.add_argument('name', type=str)
update_teacher_parser.add_argument('subject', type=str)

class StudentAPI(Resource):
    def get(self, student_id):
        student = Student.get_student(student_id)
        if not student:
            return {'message': 'Student not found'}, 404
        return student, 200

    def post(self, student_id):
        args = student_parser.parse_args()
        name = args['name']
        age = args['age']
        grade = args['grade']
        try:
            Student.create_student(student_id, name, age, grade)
            return {'message': 'Student created'}, 201
        except ValueError as e:
            return {'message': str(e)}, 400

    def put(self, student_id):
        args = update_student_parser.parse_args()
        name = args.get('name')
        age = args.get('age')
        grade = args.get('grade')
        try:
            Student.update_student(student_id, name, age, grade)
            return {'message': 'Student updated'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    def delete(self, student_id):
        try:
            Student.delete_student(student_id)
            return {'message': 'Student deleted'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

class StudentListAPI(Resource):
    def get(self):
        return Student.students, 200

class TeacherAPI(Resource):
    def get(self, teacher_id):
        teacher = Teacher.get_teacher(teacher_id)
        if not teacher:
            return {'message': 'Teacher not found'}, 404
        return teacher, 200

    def post(self, teacher_id):
        args = teacher_parser.parse_args()
        name = args['name']
        subject = args['subject']
        try:
            Teacher.create_teacher(teacher_id, name, subject)
            return {'message': 'Teacher created'}, 201
        except ValueError as e:
            return {'message': str(e)}, 400

    def put(self, teacher_id):
        args = update_teacher_parser.parse_args()
        name = args.get('name')
        subject = args.get('subject')
        try:
            Teacher.update_teacher(teacher_id, name, subject)
            return {'message': 'Teacher updated'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    def delete(self, teacher_id):
        try:
            Teacher.delete_teacher(teacher_id)
            return {'message': 'Teacher deleted'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

class TeacherListAPI(Resource):
    def get(self):
        return Teacher.teachers, 200
