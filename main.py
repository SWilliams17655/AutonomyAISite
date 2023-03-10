from flask import Flask, render_template, request
import requests

global blog_url
blog_url = "https://api.npoint.io/478c3a413404cfb6fb97"
app = Flask(__name__)

@app.route("/")  # goes to the home page
def home_page():
    global blog_url
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
    global blog_url
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('articles.html', blog_posts=all_posts)

@app.route("/article")
def article_page():
    global blog_url
    response = requests.get(blog_url)
    all_posts = response.json()
    article = all_posts["articles"][0]
    print(article["date"])
    return render_template("article.html", article=article)

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


if __name__ == "__main__":  # is the same thing as calling the run function
    app.run(host="0.0.0.0")
