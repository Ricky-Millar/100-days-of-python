from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = request_posts())

@app.route('/blog_posts/<id>')
def get_post(id):
    all_posts = request_posts()
    body = all_posts[int(id)-1]['body']
    title = all_posts[int(id)-1]['title']
    subtitle = all_posts[int(id)-1]['subtitle']
    return render_template('post.html',body = body, title = title, subtitle = subtitle)

def request_posts():
    blog_url = 'https://api.npoint.io/ed99320662742443cc5b'
    response = requests.get(url=blog_url)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)
