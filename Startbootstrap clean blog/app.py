from flask import Flask, render_template
import requests

response = requests.get(url="https://api.npoint.io/cb188c580c019f88eea3")
posts = response.json()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/index.html")
def home_home():
    return render_template("index.html", all_posts=posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/post/<post_id>")
def post(post_id):
    post_to_review = posts[int(post_id) - 1]
    return render_template("post.html", single_post=post_to_review)


if __name__ == "__main__":
    app.run(debug=True)
