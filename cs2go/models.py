from cs2go import db
from datetime import datetime

class School(db.Document):
    name = db.StringField(required=True, max_length=100)
    module1 = db.ReferenceField('Module1')
    module2 = db.ReferenceField('Module2')
    module3 = db.ReferenceField('Module3')
    # A school will have a list of assignments
    assignments = db.ListField(db.ReferenceField('Assignment'))
    meta = {
        'collection': 'schools'
    }


class Assignment(db.Document):
    title = db.StringField(required=True, max_length=200)
    description = db.StringField()
    # who created the assignment.
    created_by = db.ReferenceField('User')
    # what school.
    school = db.ReferenceField('School')
    # submission date
    submission_date = db.DateTimeField(required=True)
    # status open or close. true means open false means close
    status = db.BooleanField(required=True, default=True)
    # submitted documents
    documents = db.ListField(db.ReferenceField('Document'))
    meta = {
        'collection': 'assignments'
    }


class Document(db.Document):
    # name of the file
    filename = db.StringField()
    # which assignment this document belongs to
    assignment = db.ReferenceField('Assignment')
    # who is submitted the document
    submitted_by = db.ReferenceField('User')
    # when was the document submitted
    submitted_date = db.DateTimeField(required=True, default=datetime.utcnow)
    meta = {
        'collection': 'documents'
    }


class Module1(db.Document):
    files = db.ListField(db.ReferenceField('File'))
    chats = db.ListField(db.ReferenceField('Chat'))
    meta = {
        'collection': 'module1'
    }


class Module2(db.Document):
    files = db.ListField(db.ReferenceField('File'))
    chats = db.ListField(db.ReferenceField('Chat'))
    meta = {
        'collection': 'module2'
    }


class Module3(db.Document):
    files = db.ListField(db.ReferenceField('File'))
    chats = db.ListField(db.ReferenceField('Chat'))
    meta = {
        'collection': 'module3'
    }


class Chat(db.Document): #Note: Chat refers to "Module Post Board", It was first called "Module Chat" but changed the name
    description = db.StringField(required=True)
    # A user reference to who added this chat
    user = db.ReferenceField('User')
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)
    meta = {
        'collection': 'chats'
    }


class PersonalQuestions(db.Document):
    # All the fields for PersonalQuestions
    gender = db.StringField(required=True)
    age = db.StringField(required=True)
    year = db.StringField(required=True)
    englishspeaker = db.StringField(required=True)
    mornornight = db.StringField(required=True)
    personalsmartphone = db.StringField(required=True)
    phoneaccess = db.StringField(required=True)
    phonehours = db.StringField(required=True)
    phoneactivity = db.StringField
    personalcomputer = db.StringField(required=True)
    computeraccess = db.StringField
    phonehours = db.StringField(required=True)
    phoneactivity = db.ListField
    nocomputer = db.StringField(required=True)
    computerhours = db.StringField(required=True)
    computeractivity = db.ListField
    personaltablet = db.StringField(required=True)
    tablethours = db.StringField(required=True)
    tabletactivity = db.ListField
    programmingexperience = db.StringField(required=True)
    programmingexperiencetime = db.StringField(required=True)
    programminglanguages = db.ListField
    programoften = db.StringField(required=True)
    programminglevel = db.StringField(required=True)
    weborappdev = db.StringField(required=True)
    technologies = db.ListField
    programmingsite = db.ListField
    jclevel = db.StringField(required=True)
    parentoccupation = db.StringField(required=True)

    meta = {
        'collection': 'PersonalQs'
    }

class CSQs(db.Document):
    #All the fields for CS Questions
    userid = db.StringField(required=True)
    studycs = db.StringField(required=True)
    thinkcs = db.StringField(required=True)
    csinteresting = db.StringField(required=True)
    csinterestingwhy = db.StringField
    cschallenging = db.StringField(required=True)
    cschallengingwhy = db.StringField
    internetcentral = db.StringField(required=True)
    wordexcelcentral = db.StringField(required=True)
    installingcentral = db.StringField(required=True)
    programmingcentral = db.StringField(required=True)
    solvingproblemscentral = db.StringField(required=True)
    relatedtomaths = db.StringField(required=True)
    workwithothers = db.StringField(required=True)
    menmorelikely = db.StringField(required=True)
    donenocomputer = db.StringField(required=True)
    heardcompthinking = db.StringField(required=True)
    compthinkingmeaning = db.StringField


    meta = {
        'collection': 'ComputerScienceQs'
    }



class BebrasQuiz1(db.Document):
    #Bebras1
    email = db.StringField(required=True)
    braclet = db.StringField(required=True)
    animation = db.StringField(required=True)
    animalcompetition = db.StringField(required=True)
    stackcomputer = db.StringField(required=True)
    crosscountry = db.StringField(required=True)
    dicethrow = db.StringField(required=True)
    drawingstars = db.StringField(required=True)
    beaverlunch = db.StringField(required=True)
    wontfind = db.StringField(required=True)
    bowlfactory = db.StringField(required=True)
    fireworks = db.StringField(required=True)
    kangaroo = db.StringField(required=True)
    spies = db.StringField(required=True)
    score = db.IntField(required=True)

    meta = {
        'collection': 'BebrasQuiz1'
    }


class BebrasQuiz2(db.Document):
    #bebras2
    email = db.StringField(required=True)
    bebraspainting = db.StringField(required=True)
    bottles = db.StringField(required=True)
    partyguests = db.StringField(required=True)
    tubesystem = db.StringField(required=True)
    magicpotions = db.StringField(required=True)
    concurrentdirections = db.StringField(required=True)
    secretmessages = db.StringField(required=True)
    triangles = db.StringField(required=True)
    scannercode = db.StringField(required=True)
    thegame = db.StringField(required=True)
    benigma = db.StringField(required=True)
    theatre = db.StringField(required=True)
    piratehunters = db.StringField(required=True)
    score = db.IntField(required=True)


    meta = {
        'collection': 'BebrasQuiz2'
    }



class User(db.DynamicDocument):
    # student table we should keep some additional field dl_docs_array and login_counter and login_array
    # All this field will be set dynamically
    dl_docs_array = db.ListField(db.ReferenceField('File'))
    login_counter = db.IntField()
    login_array = db.ListField(db.DateField())
    title = db.StringField()
    approved = db.BooleanField()

    name = db.StringField(required=True, max_length=50)
    surname = db.StringField(required=True)
    email = db.EmailField(required=True)
    password = db.BinaryField(required=True)
    user_type = db.StringField(required=True)
    school = db.ReferenceField(School)  # Here will store id of the school
    # Here will be list of post collection
    posts = db.ListField(db.ReferenceField('Post'))

    meta = {
        'collection': 'users'
    }


class File(db.Document):
    user = db.ReferenceField('User')
    filename = db.StringField()
    tags = db.ListField(db.StringField(), default=list)
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)
    meta = {
        'collection': 'files'
    }


class Post(db.Document):
    subject = db.StringField()
    author = db.StringField(required=True, max_length=50)
    description = db.StringField()
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)
    comments = db.ListField(db.ReferenceField('Comment'))
    # Post will have a list of comments
    meta = {
        'collection': 'posts'
    }


# keep a post field in the comment which will make to find or delete the comment very easily
class Comment(db.DynamicDocument):
    description = db.StringField()
    post = db.ReferenceField('Post')
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)
    user_id = db.ReferenceField(User)  # here will store id of the user
    author = db.StringField(required=True, max_length=50)
    meta = {
        'collection': 'comments'
    }
