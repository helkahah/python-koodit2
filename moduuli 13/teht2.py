import mysql.connector
import json
from flask import Flask, Response, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

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

def get_airport(icao):
    query = f"select ident, name, municipality from airport where airport.ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    #print(result)
    return result

@app.route('/kenttä/<icao>')
def kenttä(icao):
    result = get_airport(icao)
    vastaus = {
        "ICAO": result[0],
        "Name": result[1],
        "Municipality": result[2]
    }
    return jsonify(vastaus)

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)