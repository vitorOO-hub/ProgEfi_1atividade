from database import db
from utils import load_template
import models


def index():
    imagem = "/static/img/getit.png"
    note_template = load_template('static/templates/components/note.html')
    notes_li = [
        note_template.format(title=note.titulo, details=note.conteudo)
        for note in models.Note.query.all()
    ]
    notes = '\n'.join(notes_li)

    return load_template('static/templates/index.html').format(notes=notes, imagem=imagem)


def submit(note):
    if note.conteudo == '':
        note.conteudo = 'nota adicionada sem detalhes'
    if note.titulo == '':
        note.titulo = 'nota adicionada sem titulo'

    db.session.add(note)
    db.session.commit()
