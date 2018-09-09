from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config.update(
    SECRET_KEY='admin',
    SQLALCHEMY_DATABASE_URI='postgres://postgres:admin@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


# connection for flask and database
db = SQLAlchemy(app)


class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer,primary_key=False)
    ssn = db.Column(db.String(10),primary_key=False)
    image = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(10), primary_key=False)
    dob= db.Column(db.DateTime, default=datetime.utcnow())

    ins_id = db.Column(db.Integer, db.ForeignKey('insurance.id'))

    def __init__(self, id,name,age,ssn,phone_number,image,ins_id):
        self.id = id
        self.name = name
        self.age=age
        self.ssn=ssn
        self.phone_number=phone_number
        self.image=image
        self.ins_id=ins_id

    def __repr__(self):
        return 'This id is {},Name is {}'.format(self.id, self.name)


class Insurance(db.Model):
    __tablename__ = 'insurance'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, id,name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'This id is {},Name is {}'.format(self.id, self.name)



@app.before_request
def some_function():
    g.string = '<br> This code ran before any request'


# BASIC ROUTE
@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask! <br>' + g.string


# QUERY STRINGS
@app.route('/new/')
def query_strings(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is : {0} </h1>'.format(query_val) + g.string


# REMOVE QUERY STRINGS
@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there ! {} </h1>'.format(name)


# STRINGS
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> here is a string: ' + name + '</h1>'


# NUMBERS
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: ' + str(num) + '</h1>'


# MORE NUMBERS
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1>the sum is : {}'.format(num1 + num2) + '</h1>'


# FLOATS
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is: {}'.format(num1 * num2) + '</h1>'


# USING TEMPLATES
@app.route('/temp')
def using_templates():
    return render_template('hello.html')


# JINJA TEMPLATES
@app.route('/watch')
def movies_2017():
    movie_list = ['autopsy of jane doe',
                  'neon demon',
                  'ghost in a shell',
                  'kong: skull island',
                  'john wick 2',
                  'spiderman - homecoming']

    return render_template('movies.html',
                           movies=movie_list,
                           name='Harry')


@app.route('/tables')
def movies_plus():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('table_data.html',
                           movies=movies_dict,
                           name='Sally')


@app.route('/filters')
def filter_data():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('filter_data.html',
                           movies=movies_dict,
                           name=None,
                           film='a christmas carol')


@app.route('/macros')
def jinja_macros():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('using_macros.html',
                           movies=movies_dict)


@app.route('/session')
def session_data():
    if 'name' not in session:
        session['name'] = 'harry'
    return render_template('session.html', name=session['name'], session=session)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=False)
