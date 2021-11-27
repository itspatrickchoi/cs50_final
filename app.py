from flask import Flask, flash, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

from helpers import apology, login_required
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    # see SQLAlchemy documentation
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/cs50_final'
else:
    # production database (Heroku?)
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#conn = db.connect()


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    hash = db.Column(db.String(200), unique=True)
    score = db.Column(db.Integer, default=1000)

    def __init__(self, username, email, hash, score):
        self.username = username
        self.email = email
        self.hash = hash
        self.score = score


@ app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/frontpage')
def curvaceous():
    return render_template('frontpage.html')


@ app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        comments = request.form['comments']
        print(customer, dealer, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Final).filter(Final.customer == customer).count() == 0:
            data = Final(customer, dealer, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted before')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # TODO
        return redirect('/')
    else:
        return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # TODO
    # Forget any user_id
    # session.clear()

    if request.method == 'POST':
        # Ensuring of user input is given by field setup
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        # Ensure password confirmation
        if password != confirmation:
            return apology("password confirmation doesn't match", 400)
        hash = generate_password_hash(
            password, method='pbkdf2:sha256', salt_length=8)
        score = 1000

        if db.session.query(Users).filter(Users.username == username).count() != 0:
            return apology('this username already exists', 400)
        elif db.session.query(Users).filter(Users.email == email).count() != 0:
            return apology('this email was already used', 400)
        else:
            data = Users(username, email, hash, score)
            db.session.add(data)
            db.session.commit()
            send_mail(username, email, score)
            return render_template('success.html')

        return redirect('/')
    else:
        return render_template('signup.html')


if __name__ == '__main__':
    app.run()
