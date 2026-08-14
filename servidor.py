from flask import Flask, render_template_string
from utils import load_notes, load_template

app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    notes = load_notes()
    imagem_getit =  "/static/img/getit.png"
    response = load_template('static/templates/index.html').format(notes=notes, imagem=imagem_getit)

    return render_template_string(response)


if __name__ == '__main__':
    app.run(debug=True)