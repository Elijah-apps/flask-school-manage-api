from flask_restful import Api
from school.endpoints import StudentAPI, StudentListAPI, TeacherAPI, TeacherListAPI

def initialize_routes(app):
    api = Api(app)
    api.add_resource(StudentAPI, '/students/<string:student_id>')
    api.add_resource(StudentListAPI, '/students')
    api.add_resource(TeacherAPI, '/teachers/<string:teacher_id>')
    api.add_resource(TeacherListAPI, '/teachers')
