from flask import Flask, render_template, request, redirect, url_for
from connect import DBConnection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/adaugare', methods=['GET', 'POST'])
def adaugare():
    if request.method == 'POST':
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

        adauga_inregistrari(cursant_data)
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

def citeste_date():
    db = DBConnection()
    with db.connection.cursor() as cursor:
        sql = "SELECT * FROM cursant;"
        cursor.execute(sql)
        lista_cursanti = cursor.fetchall()
    return lista_cursanti

def sterge_inregistrare(cnp):
    db = DBConnection()
    with db.connection.cursor() as cursor:
        sql = f"DELETE FROM cursant WHERE cnp='{cnp}';"
        cursor.execute(sql)
        db.connection.commit()

def adauga_inregistrari(date):
    db = DBConnection()
    date_existente = citeste_date()
    cnp = date.get('cnp')
    existent = False
    for ex in date_existente:
        cnp_existent = ex.get('cnp')
        if cnp_existent == cnp:
            sql = (f"UPDATE cursant SET nume='{date.get('nume')}', "
                   f"prenume='{date.get('prenume')}', "
                   f"prenume_mama='{date.get('prenume_mama')}', "
                   f"prenume_tata='{date.get('prenume_tata')}', "
                   f"locul_nasterii='{date.get('locul_nasterii')}' "
                   f"WHERE cnp='{cnp}';")
            existent = True
            break
    if not existent:
        sql = (f"INSERT INTO cursant (nume, prenume, cnp, "
               f"prenume_mama, prenume_tata, locul_nasterii) VALUES "
               f"('{date.get('nume')}', '{date.get('prenume')}', '{date.get('cnp')}', "
               f"'{date.get('prenume_mama')}', '{date.get('prenume_tata')}', "
               f"'{date.get('locul_nasterii')}');")
    with db.connection.cursor() as cursor:
        cursor.execute(sql)
        db.connection.commit()

if __name__ == '__main__':
    app.run(debug=True)
