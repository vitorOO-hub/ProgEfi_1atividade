from flask import Flask, url_for, render_template_string
from utils import load_notes


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

RESPONSE_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Get-it</title>
</head>
<body>

<img src="{{ url_for('static', filename='img/getit.png') }}">
<p>Como o Post-it, mas com outro verbo</p>

<ul>
{{notes | safe}}
</ul>

</body>
</html>
'''

@app.route('/')
def index():
    notes_html = load_notes()
    return render_template_string(
        RESPONSE_TEMPLATE, notes=notes_html
    )

if __name__ == '__main__':
    app.run(debug=True)
