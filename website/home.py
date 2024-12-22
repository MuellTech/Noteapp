from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

home_bp = Blueprint('/', __name__ )

@home_bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST': 
    note = request.form.get('note') 

    if len(note) < 1:
      flash('Error: Note is too short!', category='error') 
    else:
      new_note = Note(data=note, user_id=current_user.id)  
      db.session.add(new_note) 
      db.session.commit()
      flash('Note has been added successfully!', category='success')
  return render_template("home.html", user=current_user)


@home_bp.route('/delete-note', methods=['POST'])
def delete_note():  
  note = json.loads(request.data) 
  noteId = note['noteId']
  note = Note.query.get(noteId)
  if note:
    if note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
  return jsonify()