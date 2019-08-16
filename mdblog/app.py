from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from .database import articles

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
	return render_template("welcome_page.jinja", text="Boch ťa vidí")

@flask_app.route("/about/")
def view_about():
	return render_template("about.jinja")

@flask_app.route("/admin/")
def view_admin():
	return render_template("admin.jinja")

@flask_app.route("/articles/")
def view_articles():
	return render_template("articles.jinja", articles=articles.items())

@flask_app.route("/articles/<int:art_id>")
def view_article(art_id):
	article = articles.get(art_id)
	if article:
		return render_template("article.jinja", article=article)
	else:
		return render_template("article_not_found.jinja", art_id=art_id)
		
@flask_app.route("/login/", methods=['GET'])
def view_login():
	return render_template("login.jinja")
		
@flask_app.route("/login/", methods=['POST'])
def login_user():
	username = request.form["username"]
	password = request.form["password"]
	if username == "admin" and password == "admin":
		return redirect(url_for("view_admin"))
	else:
		return redirect(url_for("view_login"))

