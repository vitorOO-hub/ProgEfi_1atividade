import json

def load_data(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def load_notes():
    notes_data = load_data('static/data/notes_getit.json')
    notes_li = [
        f"<li><h3>{dados['titulo']}</h3><p>{dados['detalhes']}</p></li>"
        for dados in notes_data
    ]
    
    return '\n'.join(notes_li)
