import mysql.connector
from database.DB_connect import get_connection
from model.iscrizione import Iscrizione


def getIscrizioni():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = "select * from iscrizione i"

    cursor.execute(query)

    result = []

    for row in cursor:
        result.append(Iscrizione(row["matricola"], row["codins"]))

    cursor.close()
    cnx.close()
    return result


def setIscrizione(matricola, codice):
    cnx = get_connection()
    cursor = cnx.cursor()
    query = """insert into iscrizione (matricola, codins)
values (%s, %s)"""
    cursor.execute(query, (int(matricola), str(codice)))
    cnx.commit()
    cursor.close()
    cnx.close()
    return True
