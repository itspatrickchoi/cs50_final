from flask import Flask, flash, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

from helpers import apology, login_required, success
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

from datetime import datetime

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

# set secret key for working with sessions
app.secret_key = "sdfjawoi39439435wief"

db = SQLAlchemy(app)
#conn = db.connect()


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    hash = db.Column(db.String(200), unique=True)
    score = db.Column(db.Integer, default=1000)
    # https: // blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
    monthly_plans = db.relationship(
        'MonthlyPlan', backref='author', lazy='dynamic')

    def __init__(self, username, email, hash, score):
        self.username = username
        self.email = email
        self.hash = hash
        self.score = score


class MonthlyPlan(db.Model):
    __tablename__ = 'monthly_plan'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    plan_item = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, index=True)
    # https: // blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

    # make sure that in pgadmin4 id is set to "Type: IDENTITY; BY DEFAULT, Increment: 1",..
    # so that when adding a new row to the db, the id is autoincremented/autofilled
    def __init__(self, user_id, plan_item, date_created):
        self.user_id = user_id
        self.plan_item = plan_item
        self.date_created = date_created


@ app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        print("TEEEESTTT!!!")
        print(request.form['add-task-in-1'])
        print(request.form['add-task-in-2'])
        if request.form['add-task-in-1']:
            print("first box input!")
            input1 = request.form['add-task-in-1']
            data = MonthlyPlan(
                session["user_id"], input1, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            db.session.add(data)
            db.session.commit()
            print("DONE!")
        elif request.form['add-task-in-2']:
            print("second box input!")
        else:
            print("No input!")

        return redirect("/")
    else:
        # datetime object containing current date and time
        now = datetime.now()
        print("now =", now)
        dt_month = now.strftime('%B')
        print("dt_month = ", dt_month)
        dt_day = now.strftime('%d')
        print("dt_day = ", dt_day)
        dt_year = now.strftime('%Y')
        print("dt_year = ", dt_year)

        monthly_plan = db.session.query(MonthlyPlan).filter(
            MonthlyPlan.user_id == session["user_id"]).all()
        print(monthly_plan)
        return render_template('index.html', month=dt_month.upper(), day=dt_day, year=dt_year, monthly_plan=monthly_plan)


@app.route('/delete/<int:id>')
@login_required
def delete(id):
    task_to_delete = db.session.query(
        MonthlyPlan).filter(MonthlyPlan.id == id).one()
    print("Hey, delete here!!")
    print(task_to_delete)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect("/")


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
            # DON'T FORGET, before commit() gets error as not-null violation of id column. Config in pgadmin4 to "Type: IDENTITY" and config Increment
            send_mail(customer, dealer, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted before')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    # Forget any user_id
    session.clear()

    if request.method == 'POST':
        # only lowercase the input when comparing emails in if-statements
        username_email = request.form.get('username-or-email-address')
        password = request.form.get('password')
        # if invalid username
        if db.session.query(Users).filter(Users.username == username_email).count() == 0:
            # if invalid email, return apology
            if db.session.query(Users).filter(Users.email == username_email.lower()).count() == 0:
                return apology("Invalid username or email address", 403)
            # if correct email, check password
            else:
                user = db.session.query(Users).filter(
                    Users.email == username_email.lower()).first()
                if check_password_hash(user.hash, password):
                    # Remember which user has logged in
                    session["user_id"] = user.id
                    print("User logged in: " + str(session["user_id"]))
                    return redirect('/')
                else:
                    return apology("Invalid password", 403)
        # if correct username, check password
        else:
            user = db.session.query(Users).filter(
                Users.username == username_email).first()
            if check_password_hash(user.hash, password):
                # Remember which user has logged in
                session["user_id"] = user.id
                print("User logged in: " + str(session["user_id"]))
                return redirect('/')
            else:
                return apology("Invalid password", 403)
    else:
        return render_template('signin.html')


@app.route('/signout')
def signout():
    # Forget any user_id
    session.clear()

    return redirect('/')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Forget any user_id
    session.clear()

    if request.method == 'POST':
        # Ensuring of user input is given by field setup
        username = request.form.get('username')
        email = request.form.get('email').lower()
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        print(username, email, password, confirmation)
        # Ensure password confirmation
        if password != confirmation:
            return apology("password confirmation doesn't match", 400)
        hash = generate_password_hash(
            password, method='pbkdf2:sha256', salt_length=8)
        score = 1000
        print(hash, score)

        if db.session.query(Users).filter(Users.username == username).count() != 0:
            return apology('this username already exists', 400)
        elif db.session.query(Users).filter(Users.email == email).count() != 0:
            return apology('this email was already used', 400)
        else:
            print("hello")
            data = Users(username, email, hash, score)
            db.session.add(data)
            db.session.commit()
            send_mail(username, email, score)
            return success("Your account has been created!", "Congratulations!")

        return redirect('/')
    else:
        return render_template('signup.html')


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


if __name__ == '__main__':
    app.run()
