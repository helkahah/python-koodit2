import json
from flask import Flask, Response, jsonify

app = Flask(__name__)

def is_prime(n):
    vastaus = True
    for i in range(2, n):
        if n % i == 0:
            vastaus = False
        return vastaus

@app.route('/alkuluku/<int:n>')
def alkuluku(n):
    tulos = is_prime(n)
    vastaus = {
        "Number": n,
        "isPrime": tulos
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