# moduuli 8 tehtävä 2

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

def get_airport(maakoodi):
    query = f"select type, count(*) as total from airport where airport.iso_country = '{maakoodi}' group by type order by type desc"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    #print(result)
    return result

maakoodi = input('Anna maakoodi:')
result = get_airport(maakoodi)
print(result)