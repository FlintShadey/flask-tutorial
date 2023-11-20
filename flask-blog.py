from flask import Flask, request, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug =True)