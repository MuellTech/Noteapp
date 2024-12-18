from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
  return render_template('login.html')

@auth_bp.route('/logout')
def logout():
  return '<h1>Logout<h1>'

@auth_bp.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 6:
      flash('Email must be more than 5 characters.', category = 'error')
    elif len(firstName) < 2:
      flash('First name must be more than  a character.', category = 'error')
    elif len(password1) < 8:
      flash('Password must be at least 8 characters.', category = 'error')
    elif password1 != password2:
      flash('Passwords do not match.', category = 'error')
    else:
      user = User(email = email, firstName = firstName, password = generate_password_hash(password1))
      flash('Account successfully created!')
  return render_template('sign_up.html')

