from flask import Blueprint, render_template, request, flash, redirect
from .models import User
from argon2 import PasswordHasher
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from argon2.exceptions import VerifyMismatchError

auth_bp = Blueprint('auth', __name__)

ph = PasswordHasher()

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email = email).first()
    if user:
      try:
        # verify password
        if ph.verify(user.password, password):
          flash('Logged in successfully!', category='success')
          login_user(user, remember=True)
          return redirect('/')
        else:
          flash('Incorrect password, try again.', category='error')
          return redirect('/login')
        # handle password error
      except VerifyMismatchError:
        flash('Incorrect password, try again.', category='error')
        return render_template('login.html', user = current_user)
    else:
      flash('Email does not exist.', category='error')

  return render_template('login.html', user = current_user)

@auth_bp.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect('/login')

@auth_bp.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    user = User.query.filter_by(email=email).first()

    if user:
      flash('Email already exists.', category='error')
    elif len(email) < 6:
      flash('Email must be more than 5 characters.', category = 'error')
    elif len(firstName) < 2:
      flash('First name must be more than  a character.', category = 'error')
    elif len(password1) < 8:
      flash('Password must be at least 8 characters.', category = 'error')
    elif password1 != password2:
      flash('Passwords do not match.', category = 'error')
    else:
      hashed_password = ph.hash(password1)
      new_user = User(email=email, firstName=firstName, password=hashed_password)
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user, remember = True)
      flash('Account successfully created!')
      return redirect('/')
  return render_template('sign_up.html', user = current_user)



