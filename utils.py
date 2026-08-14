import json

def load_data(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def load_notes():
    notes_li = [
            load_template('static/templates/components/note.html').format(title=dados['titulo'], details=dados['detalhes'])
            for dados in load_data('static/data/notes_getit.json')
        ]
    
    notes = '\n'.join(notes_li)

    return notes

def load_template(nome_template):
    with open(nome_template, "r", encoding="utf-8") as arquivo:
        return arquivo.read()
