from utils import load_template, load_data
import sqlite3


def index():
    imagem = "/static/img/getit.png"
    note_template = load_template('static/templates/components/note.html')
    notes_li = [
        note_template.format(title=titulo, details=conteudo)
        for i, titulo, conteudo in load_data()
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