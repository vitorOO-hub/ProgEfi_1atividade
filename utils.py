import json
import models

def load_notes():
    note_template = load_template('static/templates/components/note.html')
    notes_li = [
        note_template.format(title=note.titulo, details=note.conteudo)
        for note in models.Note.query.all()
    ]

    notes = '\n'.join(notes_li)

    return notes


def load_template(nome_template):
    with open(nome_template, "r", encoding="utf-8") as arquivo:
        return arquivo.read()
