from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")  # goes to the home page
def home_page():
    blog_url = "https://api.npoint.io/b31682e16f34ffcc119d"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('index.html', blog_posts=all_posts)

@app.route("/projects")
def project_page():
    return render_template("projects.html")

@app.route("/post_article")
def post_article_page():
    return render_template("post_article.html")

@app.route("/articles")
def articles_page():
    return render_template("articles.html")

@app.route("/article")
def article_page():
    return render_template("article.html")

@app.route("/about_us")
def about_us_page():
    return render_template("about_us.html")

@app.route("/login", methods=["POST"])
def login():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name} Password: {password}</h1>"

@app.route("/post_article")
def post_article():
    return render_template("post_article.html")

@app.route("/bogus_function")
def bogus_function():
    return render_template("<h1>hello</h1>")

if __name__ == "__main__":  # is the same thing as calling the run function
    app.run(host="0.0.0.0")
