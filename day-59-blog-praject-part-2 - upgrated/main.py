from flask import Flask
from flask import render_template

import requests

api_endpoint = "https://api.npoint.io/a0ab0230d98cf0e68f76"

posts = requests.get(api_endpoint).json()




app = Flask(__name__)

@app.route("/")
def get_all_post():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    requested_post_obje = None

    for each_post in posts:
        if each_post["id"] == post_id:
            requested_post_obje = each_post

    return render_template("post.html", post=requested_post_obje)

@app.route("/contact")
def contact():
    return  render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
