from flask import Flask, flash, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

from helpers import apology, login_required

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


class Final(db.Model):
    __tablename__ = 'final'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, comments):
        self.customer = customer
        self.dealer = dealer
        self.comments = comments


@ app.route('/')
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
        return render_template('frontpage.html')
    else:
        return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # TODO
    # Forget any user_id

    if request.method == 'POST':
        # Ensuring of user input is given by field setup
        email = request.form.get('email')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        # Ensure password confirmation
        if password != confirmation:
            return apology("password confirmation doesn't match", 400)
        return render_template('frontpage.html')
    else:
        return render_template('signup.html')


if __name__ == '__main__':
    app.run()
