from flask import Flask , render_template
import random
from datetime import datetime
import requests



app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.now().year
    random_number =  random.randint(0,9)
    return render_template('index.html',random_number = random_number, year = year)

@app.route("/guess/<string:name>")
def nameguess(name):
    name = name.title()
    ageify_endpoint = "https://api.agify.io"
    genderise_endpoint = "https://api.genderize.io"
    params = {'name':name}
    age_response = requests.get(url = ageify_endpoint, params=params)
    genderise_response = requests.get(url=genderise_endpoint, params=params)
    age_stuff = age_response.json()
    gender_stuff = genderise_response.json()
    print(name)
    gender = gender_stuff['gender']
    age = age_stuff['age']

    return render_template('nameguess.html', age = age, gender = gender, name = name)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/ed99320662742443cc5b'
    response = requests.get(url=blog_url)
    print(response.json())
    all_posts = response.json()
    return render_template('blog.html', all_posts = all_posts)








if __name__ == '__main__':
    app.run(debug=True)

