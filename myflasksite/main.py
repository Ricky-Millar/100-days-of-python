from flask import Flask
from flask import render_template
#initiates a Flask object, and tells it where to find all of its goodies, __name__ tells it to look in this file
site = Flask(__name__)

@site.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    site.run(debug=True)