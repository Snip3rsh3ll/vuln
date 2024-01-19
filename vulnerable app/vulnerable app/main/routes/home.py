from flask import render_template, redirect
from flask_login import login_required, current_user

from app import app
from main.utils.notes import user_notes


@app.route("/")
@login_required
def index():
    return redirect('/home')


@app.route('/home')
@login_required
def home():
    return render_template('home.html',
                           notes=user_notes(current_user.id))
