from flask import Flask, flash, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

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


@app.route('/curvaceous')
def curvaceous():
    return render_template('curvaceous.html')


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
