from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_cors import CORS
from model import predict_model

app = Flask(__name__)
api = Api(app)
CORS(app)

api_args = reqparse.RequestParser()
api_args.add_argument('q1', type=int,
                      help='The semester course content, teaching method and evaluation system were provided at the start.', required=True)
api_args.add_argument('q2', type=int,
                      help='The course aims and objectives were clearly stated at the beginning of the period.', required=True)
api_args.add_argument('q3', type=int,
                      help='The course was worth the amount of credit assigned to it.', required=True)
api_args.add_argument('q4', type=int,
                      help='The course was taught according to the syllabus announced on the first day of class.', required=True)
api_args.add_argument('q5', type=int,
                      help='The class discussions, homework assignments, applications and studies were satisfactory.', required=True)
api_args.add_argument('q6', type=int,
                      help='The textbook and other courses resources were sufficient and up to date.', required=True)
api_args.add_argument('q7', type=int,
                      help='The course allowed field work, applications, laboratory, discussion and other studies.', required=True)
api_args.add_argument('q8', type=int,
                      help='The quizzes, assignments, projects and exams contributed to helping the learning.', required=True)
api_args.add_argument('q9', type=int,
                      help='I greatly enjoyed the class and was eager to actively participate during the lectures.', required=True)
api_args.add_argument('q10', type=int,
                      help='My initial expectations about the course were met at the end of the period or year.', required=True)
api_args.add_argument('q11', type=int,
                      help='The course was relevant and beneficial to my professional development.', required=True)
api_args.add_argument('q12', type=int,
                      help='The course helped me look at life and the world with a new perspective.', required=True)
api_args.add_argument('q13', type=int,
                      help="The Instructor's knowledge was relevant and up to date.", required=True)
api_args.add_argument('q14', type=int,
                      help='The Instructor came prepared for classes.', required=True)
api_args.add_argument('q15', type=int,
                      help='The Instructor taught in accordance with the announced lesson plan.', required=True)
api_args.add_argument('q16', type=int,
                      help='The Instructor was committed to the course and was understandable.', required=True)
api_args.add_argument('q17', type=int,
                      help='The Instructor arrived on time for classes.', required=True)
api_args.add_argument('q18', type=int,
                      help='The Instructor has a smooth and easy to follow delivery/speech.', required=True)
api_args.add_argument('q19', type=int,
                      help='The Instructor made effective use of class hours.', required=True)
api_args.add_argument('q20', type=int,
                      help='The Instructor explained the course and was eager to be helpful to students.', required=True)
api_args.add_argument('q21', type=int,
                      help='The Instructor demonstrated a positive approach to students.', required=True)
api_args.add_argument('q22', type=int,
                      help='The Instructor was open and respectful of the views of students about the course.', required=True)
api_args.add_argument('q23', type=int,
                      help='The Instructor encouraged participation in the course.', required=True)
api_args.add_argument('q24', type=int,
                      help='The Instructor gave relevant homework assignments/projects, and helped/guided students.', required=True)
api_args.add_argument('q25', type=int,
                      help='The Instructor responded to questions about the course inside and outside of the course.', required=True)
api_args.add_argument('q26', type=int,
                      help="The Instructor's evaluation system(midterm and final questions, projects, assignments, etc.) effectively measured the course objectives.", required=True)
api_args.add_argument('q27', type=int,
                      help='The Instructor provided solutions to exams and discussed them with students.', required=True)
api_args.add_argument('q28', type=int,
                      help='The Instructor treated all students in a right and objective manner.', required=True)


class Predict(Resource):
    def post(self):
        args = api_args.parse_args()
        for i in range(1, 29):
            if args[f'q{i}'] > 5 and args[f'q{i}'] < 1:
                abort(404, message='Values must be 1 - 5')
        predict = predict_model(
            args['q1'],
            args['q2'],
            args['q3'],
            args['q4'],
            args['q5'],
            args['q6'],
            args['q7'],
            args['q8'],
            args['q9'],
            args['q10'],
            args['q11'],
            args['q12'],
            args['q13'],
            args['q14'],
            args['q15'],
            args['q16'],
            args['q17'],
            args['q18'],
            args['q19'],
            args['q20'],
            args['q21'],
            args['q22'],
            args['q23'],
            args['q24'],
            args['q25'],
            args['q26'],
            args['q27'],
            args['q28'],

        )
        return {'predict': predict}, 201


api.add_resource(Predict, '/')

if __name__ == '__main__':
    app.run()
