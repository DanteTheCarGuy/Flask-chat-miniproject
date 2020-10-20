import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret.key = "randomstring123"
messages = []


def add_message(username,message):
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S")
    message.append({"timestamp": now, "from": username, "messages": message})


@app.route('/', methods = ["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return"render_template("index.html")


@app.route("/chat/<username>", methods=["GET","POST"])
def user(username):
    """Add and display chat message"""
    if request.method == "POST":
        username = sessions["username"]
        message = request.form["message"]
        add_message(username, messages)
        return redirect(url_for("user", username=session["username"]))

    return render_template("chat.html", username=username, chat_messages=messages)  



    app.run(host=os.getenv("IP", "0.0.0.0"),
     port=int(os.getenv("PORT", "5000")), debug=False)