# Add whatever it is needed to interface with the DB Table corso
import mysql.connector
from database.DB_connect import get_connection
from model.studente import Studente


def getStudenti():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = "select * from studente s"

    cursor.execute(query)

    result = []

    for row in cursor:
        result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))

    cursor.close()
    cnx.close()
    return result
