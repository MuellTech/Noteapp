# Flask Web Application

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Inspiration](#inspiration)
7. [Future Improvements](#future-improvements)

## Overview
This is a Flask-based web application that implements essential features such as user authentication, a signup and login system, database integration, and dynamic HTML rendering. It is designed as a foundation for further development into a fully functional web service.

## Features
- **User Authentication**: Secure login and logout functionality using Flask-Login.
- **User Registration**: Allows new users to register with hashed passwords using Argon2.
- **Database Integration**: Utilizes SQLAlchemy for seamless database management.
- **Flashed Messages**: Displays dynamic feedback messages for user actions such as errors or success events.
- **Bootstrap Styling**: Clean and responsive UI powered by Bootstrap.

## Technologies Used
- **Backend**: Flask, Flask-Login
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLAlchemy, sqlite
- **Password Hashing**: Argon2

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\Activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Create a database file (e.g., `site.db`).
   - Initialize the database by running the following commands in a Python shell:
     ```python
     from app import db
     with app.app_context():
      db.create_all()
     ```

5. **Run the Application**:
   ```bash
   python run.py
   ```

## Usage
- Navigate to the signup page to create a new account.
- Use the login page to access your account.
- Once logged in, interact with protected pages or logout securely.

## Inspiration
The project was inspired by the need to understand and implement essential web development practices, particularly in creating a full-stack application. Flask was chosen for its simplicity, flexibility, and lightweight nature, making it ideal for learning and quick prototyping.

Developing this project provided practical experience in building secure authentication systems and integrating databases, skills that are fundamental in modern web application development.

## Improvements underway...
- **Role-Based Access Control**: Implement admin and user roles.
- **Password Reset**: Add functionality to reset forgotten passwords.
- **Enhanced Security**: Include features like account lockout after multiple failed login attempts.
- **Email verification**:will enhance account security by ensuring users verify their email addresses before accessing the application. .
- **JWT authentication**:will replaces session-based login with a stateless and secure authentication system using JSON Web Tokens.

