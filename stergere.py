from connect import DBConnection


def sterge_inregistrare(cnp, tabel):
    db = DBConnection()
    with db.connection.cursor() as cursor:
        sql = f"DELETE FROM {tabel} WHERE cnp='{cnp}';"
        cursor.execute(sql)
        db.connection.commit()