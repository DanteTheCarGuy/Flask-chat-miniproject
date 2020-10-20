import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []


"""Add messages to the 'messages' list"""
def add_message(username,message):
    messages.append("{}: {}".format(username, messages))

def get_all_messages():
    """Gel all of the messages and separate them with a 'br'"""
    return "<br>".join(messages)


@app.route('/')
def imdex():
    """Main page with instructions"""
    return"To send a message use /<USERNAME>/<MESSAGE>"


@app.route('/<username>')
def user(username):
    """Display chat message"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())  


@app.route('/<username/<message>')
def send_message(username,message):
    """Create a new message and redirect back to the chat page"""
    add_message(username, message)
    return redirect(username)

    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
