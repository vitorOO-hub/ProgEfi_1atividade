from utils import load_data, load_template
import json 

def index():
    imagem = "/static/img/getit.png"
    note_template = load_template('static/templates/components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('static/data/notes_getit.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('static/templates/index.html').format(notes=notes, imagem=imagem)

def submit(titulo, detalhes):

    data = load_data('static/data/notes_getit.json')
    
    if detalhes == '':
        detalhes = 'nota adicionada sem detalhes'
    if titulo =='':
        titulo = 'nota adicionada sem detalhes'
    print(f"detalhesssss{detalhes}")

    data.append({'titulo':titulo, 'detalhes':detalhes})

    with open("static/data/notes_getit.json", "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo, indent=4, ensure_ascii=False)