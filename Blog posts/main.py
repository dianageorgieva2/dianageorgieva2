from flask import Flask, render_template
import requests
app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/blog/<post_id>')
def blog(post_id):
    post_to_review = all_posts[int(post_id) - 1]
    return render_template("post.html", single_post=post_to_review)


if __name__ == "__main__":
    app.run(debug=True)
