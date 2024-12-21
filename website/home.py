from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


home_bp = Blueprint('home', __name__ )

@home_bp.route('/', methods = ['POST', 'GET'])
@login_required
def home():
  if request.method == 'POST':
    note = request.form.get('note')

    if len(note) < 1:
      flash('Note is too short!', category = 'error')
    else:
      new_note = Note(data = note, user_id = current_user.id)
      db.session.add(new_note)
      db.session.commit()
      flash('Note has been added successfully!', category = 'success')
  return render_template('home.html', user = current_user)


@home_bp.route('/remove-note',  methods = ['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note and note.user_id == current_user.id:
      db.session.delete(note)
      db.session.commit()
      flash('Note deleted successfully!', category='success')
      return redirect('/')


    return jsonify({})