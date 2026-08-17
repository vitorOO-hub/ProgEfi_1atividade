from flask import Flask, render_template_string, request, redirect

from database import db
import models
import views

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"

db.init_app(app)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit_form', methods=['POST'])
def submit_form():

    title = request.form.get('titulo')
    content = request.form.get('detalhes')
    
    note = models.Note(titulo = title, conteudo = content)

    views.submit(note)

    return redirect('/')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
