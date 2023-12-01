from flask import Flask, request, render_template, url_for,flash, redirect
from markupsafe import escape
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "ec58e0a02e7d66b29d3c063d5a7293b8"

posts = [
    {
        "author": "Flint Smith",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "Nov 19, 2023",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "second post content",
        "date_posted": "Nov 25, 2023",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    else:
        print(form.errors)  # This will print form validation errors to the console
    return render_template("register.html", title="Register", form=form)




@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
