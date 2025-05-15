from flask import Flask, render_template, request, redirect, flash
from data_structures import data_structures  # ✅ import correctly

app = Flask(__name__)

# Home route (About Me)
@app.route("/")
def home():
    return render_template("index.html")

# Selenium project page
@app.route("/selenium")
def selenium():
    return render_template("selenium.html")

# Placeholder routes (you can create these later)
@app.route("/playwright")
def playwright():
    return render_template("playwright.html")

@app.route("/docker")
def docker():
    return render_template("docker.html")

@app.route("/pytest")
def pytest():
    return render_template("pytest.html")

@app.route("/dsa")
def dsa():
    return render_template("dsa.html", data_structures=data_structures)

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Optional: print or log the message (or send to AWS SNS)
        print(f"Message from {name} <{email}>: {message}")
        flash("Your message has been sent. Thank you!")

        return redirect("/contact")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
