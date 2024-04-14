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
