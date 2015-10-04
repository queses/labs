from flask import Flask, url_for

app = Flask(__name__)


@app.route("/index")
def index():
	f = open("html/index.html", 'r')
	c = f.read()
	return c

@app.route("/fonts")
def fonts():
	f = open("html/fonts.html", 'r')
	c = f.read()
	return c

@app.route("/table")
def table():
	f = open("html/table.html", 'r')
	c = f.read()
	return c

@app.route("/lists")
def lists():
	f = open("html/lists.html", 'r')
	c = f.read()
	return c

@app.route("/image")
def image():
	f = open("html/image.html", 'r')
	c = f.read()
	return c

@app.route("/user/<name>")
def user(name):
	return "Hello, %s" %name

@app.route("/")
def root():
	return index()

if __name__ == "__main__":
    app.run()