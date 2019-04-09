from flask import Flask

# MongoEngine
from mongoengine import connect
from flask_mongoengine import MongoEngine
from flask_ckeditor import CKEditor
import os

app = Flask(__name__)

app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.abspath(__file__))+'/uploads'


# Connect with the mongodb database
connect(
    'cs2godeployment',
    username='cs2gouser',
    password='cs2gopassword',
    host='mongodb://cs2gouser:cs2gopassword@ds131296.mlab.com:31296/cs2godeployment'
)

db = MongoEngine(app)
ckeditor = CKEditor(app)

# Grab the blueprints
from cs2go.students.views import students_blueprint
from cs2go.teachers.views import teachers_blueprint
from cs2go.files.views import files_blueprint
from cs2go.forums.views import forums_blueprint
from cs2go.schools.views import schools_blueprint
from cs2go.bebras.views import bebras_blueprint
from cs2go.assignments.views import assignments_blueprint


app.register_blueprint(students_blueprint, url_prefix="/students")
app.register_blueprint(teachers_blueprint, url_prefix="/teachers")
app.register_blueprint(files_blueprint, url_prefix="/files")
app.register_blueprint(forums_blueprint, url_prefix='/forums')
app.register_blueprint(schools_blueprint, url_prefix='/schools')
app.register_blueprint(bebras_blueprint, url_prefix="/bebras")
app.register_blueprint(assignments_blueprint, url_prefix='/assignments')
