from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/welcome')
def welcome():
    return 'Welcome to Flask project!'

@app.route('/about')
def about():
    return 'Techevolvo Technologies'

@app.route('/contact')
def contact():
    return 'Contact at techevolvo_technologies.com '



if __name__ == '__main__':
    app.run(debug=True)
