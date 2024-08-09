from flask import Flask, render_template, request, redirect, url_for
from adaugare import adauga_inregistrari
from citire import citeste_date
# from stergere import sterge_inregistrare

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/adaugare', methods=['GET', 'POST'])
def adaugare():
    if request.method == 'POST':
        if request.form['form_type'] == 'cursant':
            nume = request.form['cursantNume']
            prenume = request.form['cursantPrenume']
            cnp = request.form['cursantCNP']
            prenume_mama = request.form['cursantParinteMama']
            prenume_tata = request.form['cursantParinteTata']
            locul_nasterii = request.form['cursantLocNastere']

            cursant_data = {
                'nume': nume,
                'prenume': prenume,
                'cnp': cnp,
                'prenume_mama': prenume_mama,
                'prenume_tata': prenume_tata,
                'locul_nasterii': locul_nasterii,
            }
            adauga_inregistrari(cursant_data, 'cursant')

        elif request.form['form_type'] == 'companie':
            nume = request.form['companieNume']
            ocupatie = request.form['companieOcupatie']
            cor = request.form['companieCOR']
            localitate = request.form['companieLocalitate']
            judet = request.form['companieJudet']
            numar_registru = request.form['companieNrRegistru']
            data_registru = request.form['companieDataRegistru']

            companie_data = {
                'nume': nume,
                'ocupatie': ocupatie,
                'cor': cor,
                'localitate': localitate,
                'judet': judet,
                'numar_registru': numar_registru,
                'data_registru': data_registru,
            }
            adauga_inregistrari(companie_data, 'companie')

        elif request.form['form_type'] == 'comisie':
            director = request.form['comisieDirector']
            secretar = request.form['comisieSecretar']
            presedinte = request.form['comisiePresedinte']

            comisie_data = {
                'director': director,
                'secretar': secretar,
                'presedinte': presedinte,
            }
            adauga_inregistrari(comisie_data, 'comisie')


        elif request.form['form_type'] == 'curs':
            nume_curs = request.form['cursNume']
            descriere = request.form['cursDescriere']
            data_incepere = request.form['cursData']
            durata = request.form['cursDurata']

            curs_data = {
                'nume_curs': nume_curs,
                'descriere': descriere,
                'data_incepere': data_incepere,
                'durata': durata
            }
            adauga_inregistrari(curs_data, 'curs')

        return redirect(url_for('adaugare'))
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
