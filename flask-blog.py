from flask import Flask, request, render_template, url_for
from markupsafe import escape
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ec58e0a02e7d66b29d3c063d5a7293b8'

posts =[
    {
        'author': 'Flint Smith',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Nov 19, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'Nov 25, 2023'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    app.run(debug =True)