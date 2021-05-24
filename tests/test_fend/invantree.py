from flask import Flask, render_template
app = Flask(__name__)

ADMIN_USERNAME = 'pj8664'
ADMIN_PASSWORD = 'notreal123'

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("site/login.html")


@app.route("/about")
def about():
    return render_template("site/about.html")

@app.route("/item")
def item():
    return render_template("site/item.html")


if __name__ == "__main__":
    app.run(debug=True)
    main()
