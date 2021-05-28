from flask import Flask, render_template, request, session, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.secret_key = 'secretkey'
db = SQLAlchemy(app)


class UserTwo(db.Model):
    stock_number = db.Column(db.Integer, unique=True, primary_key=True)
    brand = db.Column(db.String(80), nullable=False)
    product_name = db.Column(db.String(120), nullable=False)
    size = db.Column(db.String(80), nullable=False)
    colour = db.Column(db.String(80), nullable=False)
    stockroom_location = db.Column(db.String(80), nullable=False)
    shopfloor_loaction = db.Column(db.String(80), nullable=True)
    stock_quantity = db.Column(db.Integer, unique=False, nullable=False)
    stock_description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric, nullable=False)
    link = db.Column(db.String(400), nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
    return '<name %r>' % self.id


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<user: {self.username}>"


users = []
users.append(User(id=1, username="pj8664", password="notmypassword"))
users.append(User(id=2, username="pj0000", password="password"))

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user



@app.route("/login", methods=['GET', 'POST'])
@app.route("/",methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['un']
        password = request.form['pass']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home'))

        return redirect(url_for('login'))

    return render_template("site/login.html")



@app.route("/home")
def home():
    if not g.user:
        return redirect(url_for('login'))

    return render_template("home.html")

@app.route('/sign_out')
def sign_out():
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route("/about")
def about():
    if not g.user:
        return redirect(url_for('login'))

    return render_template("site/about.html")


@app.route("/item")
def item():
    if not g.user:
        return redirect(url_for('login'))

    return render_template("site/item.html")


if __name__ == "__main__":
    app.run(debug=True)
    main()
