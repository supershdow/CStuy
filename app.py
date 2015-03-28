from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)
url_list = ["/shark","/number","/fight","/zoo","/fly","/pong"]
@app.route("/")
def index():
	return redirect(random.choice(url_list))
	#return render_template("base.html")
	
@app.route("/shark")
def robots():
	return render_template("shark.html")

"""@app.route("/robot")
def robot():
	return render_template("robots.html")"""

@app.route("/number")
def number():
	return render_template("Numberguess.html")
	
@app.route("/fight")
def fight():
	return render_template("Fight.html")

@app.route("/zoo")
def zooHerding():
	return render_template("Zoo herding.html")
	
@app.route("/fly")
def fly():
	return render_template("fly.html")

@app.route("/pong")
def pingPong():
	return render_template("pingpong.html")

"""@app.route("/form", methods=["GET", "POST"])
def form():
	if request.method == "GET":
		return "Please get here from the form"
	else:
		n = request.form["name"]
		return "Hello " + n"""



if __name__ == "__main__":
	app.debug = True
	app.run()
	
	



