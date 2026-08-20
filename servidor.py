from flask import Flask, render_template_string, request, redirect
import views
from utils import init_db

app = Flask(__name__)


# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'
init_db()

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit_form', methods=['POST'])
def submit_form():

    titulo = request.form.get('titulo')
    conteudo = request.form.get('detalhes')

    views.submit(titulo, conteudo)

    return redirect('/')

@app.route("/delete_note/<int:note_id>", methods=['POST'])
def delete_note(note_id):

    views.delete(note_id)

    return redirect('/')

@app.route("/update/<int:note_id>", methods=['GET'])
def edit_note(note_id):

    return render_template_string(views.edit_template(note_id))

@app.route("/update/<int:note_id>", methods=['POST'])
def update(note_id):

    titulo = request.form.get('titulo')
    conteudo = request.form.get('detalhes')

    views.update(note_id, titulo, conteudo)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
