from flask import render_template
from . import hacks


@hacks.route('/')
def index():
    return render_template('hacks/index.html')


@hacks.route('/user/<username>')
def user(username):
    return render_template('hacks/user.html', username=username)

