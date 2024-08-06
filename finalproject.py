from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/adaugare', methods=['GET', 'POST'])
def adaugare():
    return render_template('adaugare_date.html')

@app.route('/generare_documente', methods=['GET', 'POST'])
def generare_documente():
    return render_template('generare_documente.html')

@app.route('/actualizare_date', methods=['GET', 'POST'])
def actualizare_date():
    return render_template('actualizare_date.html')

@app.route('/stergere_date', methods=['GET', 'POST'])
def stergere_date():
    return render_template('stergere_date.html')

if __name__ == '__main__':
    app.run(debug=True)
