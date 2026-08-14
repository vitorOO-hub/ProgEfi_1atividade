from utils import load_data, load_template

def index():
    imagem = "/static/img/getit.png"
    note_template = load_template('static/templates/components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('static/data/notes_getit.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('static/templates/index.html').format(notes=notes, imagem=imagem)