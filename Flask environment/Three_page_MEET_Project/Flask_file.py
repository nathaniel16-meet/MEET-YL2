from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('MEET_Home.html')

@app.route("/about")
def about():
	return render_template("MEET_About.html")

@app.route("/contact")
def contact():
	return render_template("MEET_Contact.html")




if __name__ == "__main__":
	app.debug = True
	app.run()
