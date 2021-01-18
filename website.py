from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)

app.secret_key = "12345"

@app.route("/")
def index():
    return render_template("index.html")

# LOGIN PAGE
@app.route("/login", methods=["POST", "GET"])
def login():
    # TODO check against existing usernames/passwords
    # if receives POST request from HTML form
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        session["password"] = password

        flash("Message: Login Successful!")
        return redirect(url_for("home"))
    else:
        if "username" in session and "password" in session:
            flash("Message: You are already logged in")
            return redirect(url_for("home"))
        
        return render_template("login.html")

# HOMEPAGE after login
@app.route("/home")
def home():
    if "username" in session and "password" in session:
        return render_template("home.html", username=session["username"])
    else:
        flash("Message: You are not logged in.")
        return redirect(url_for("login"))

# LOGOUT - function, not a page
@app.route("/logout")
def logout():
    flash("Message: You have been logged out.", "info")
    session.pop("username", None)
    session.pop("password", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)