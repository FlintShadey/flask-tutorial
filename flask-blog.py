from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    name =request.args.get("name", "world")
    return '<h1>Home Page</h1>'

@app.route('/about')
def about():
    return'<h1>About</h1>'

if __name__ == '__main__':
    app.run(debug =True)