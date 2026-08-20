from utils import load_template, load_data
import sqlite3


def index():
    imagem = "/static/img/getit.png"
    note_template = load_template('static/templates/components/note.html')
    notes_li = [
        note_template.format(id=note_id, title=titulo, details=conteudo)
        for note_id, titulo, conteudo in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('static/templates/index.html').format(notes=notes, imagem=imagem)

def submit(titulo, detalhes):
    db = sqlite3.connect("banco.db")
    cursor = db.cursor()

    if detalhes == '':
        detalhes = 'nota adicionada sem detalhes'
    if titulo == '':
        titulo = 'nota adicionada sem titulo'

    cursor.execute("INSERT INTO note (titulo, conteudo) VALUES (?, ?)",
                   (titulo, detalhes))
    
    db.commit()
    db.close()

def delete(note_id):

    db = sqlite3.connect("banco.db")
    cursor = db.cursor()

    cursor.execute("DELETE FROM note WHERE id = ?", (note_id,))

    db.commit()
    db.close()


def edit_template(note_id):
    db = sqlite3.connect("banco.db")
    cursor = db.cursor()

    cursor.execute("SELECT titulo, conteudo FROM note WHERE id = ?", (note_id,))
    note = cursor.fetchone()

    db.close()

    if note is None:
        return "Nota nao encontrada"

    titulo, conteudo = note
    return load_template('static/templates/components/edit.html').format(
        id=note_id,
        title=titulo,
        details=conteudo
    )


def update(note_id, titulo, detalhes):
    db = sqlite3.connect("banco.db")
    cursor = db.cursor()

    if detalhes == '':
        detalhes = 'nota adicionada sem detalhes'
    if titulo == '':
        titulo = 'nota adicionada sem titulo'

    cursor.execute(
        "UPDATE note SET titulo = ?, conteudo = ? WHERE id = ?",
        (titulo, detalhes, note_id)
    )

    db.commit()
    db.close()
