# moduuli 8 tehtävä 1

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user1',
        password='sala1',
        autocommit=True
    )
connection = connect_db()
#print(connection)

def get_airport(icao):
    query = f"select name, municipality from airport where ident='{icao}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    #print(result)
    if cursor.rowcount > 0:
        return f"Kentän nimi: {result[0]}, paikkakunta: {result[1]}"
    else:
        return "Ei tuloksia"

icao = input('Anna ICAO-koodi: ')
result = get_airport(icao)
print(result)