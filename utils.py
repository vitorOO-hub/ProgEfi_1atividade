import sqlite3
from dataclasses import dataclass


@dataclass
class Note:
    id: int
    title: str
    content: str


def load_data():
    db = sqlite3.connect('banco.db')

    cursor = db.cursor()
    cursor.execute("SELECT * FROM note")
    all_data = cursor.fetchall()

    db.close()

    return all_data


def load_notes():
    note_template = load_template('static/templates/components/note.html')
    notes_li = [
        note_template.format(id=note_id, title=titulo, details=conteudo)
        for note_id, titulo, conteudo in load_data()
    ]

    notes = '\n'.join(notes_li)

    return notes

def get_note(note_id):
    db = sqlite3.connect("banco.db")
    cursor = db.cursor()

    cursor.execute("SELECT id, title, content FROM note WHERE id = ?", (note_id,))
    row = cursor.fetchone()

    db.close()

    if row is None:
        return None

    note_id, titulo, conteudo = row

    return Note(id=note_id, title=titulo, content=conteudo)

def load_template(nome_template):
    with open(nome_template, "r", encoding="utf-8") as arquivo:
        return arquivo.read()


def init_db():
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS note
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL)"""
    )

    db.commit()
    db.close()
