# moduuli 8 tehtävä 3

import mysql.connector
import geopy

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

def hae_tieto(icao):
    query = f"select latitude_deg, longitude_deg from airport where airport.ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result



icao = input('Anna lentokentän ICAO-koodi:')
lentokenttä1 = hae_tieto(icao)
#print(lentokenttä1)
icao = input('Anna toisen lentokentän ICAO-koodi: ')
lentokenttä2 = hae_tieto(icao)
#print(lentokenttä2)

from geopy.distance import geodesic
print(f"{geodesic(lentokenttä1, lentokenttä2).kilometers}km")


