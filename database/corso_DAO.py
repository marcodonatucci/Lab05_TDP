# Add whatever it is needed to interface with the DB Table corso
import mysql.connector
from database.DB_connect import get_connection
from model.corso import Corso


def getCorsi():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = "select * from corso c"

    cursor.execute(query)

    result = []

    for row in cursor:
        result.append(Corso(row["codins"], row["nome"], row["crediti"], row["pd"]))

    cursor.close()
    cnx.close()
    return result
