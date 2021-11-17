from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

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


class Final(db.model):
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


@ app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        comments = request.form['comments']
        print(customer, dealer, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')
        return render_template('success.html')


if __name__ == '__main__':
    app.run()
