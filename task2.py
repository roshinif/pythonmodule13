from flask import Flask, request
import mysql.connector

app = Flask(__name__)


@app.route('/kentta/<icao>')
def kentta(icao):
    airport, municipal = details(icao)

    return f"ICAO: {icao}, Name: {airport}, Municipality: {municipal}"


def details(icao):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="airport"
    )

    cursor = mydb.cursor()

    cursor.execute("SELECT name from airports where ident = %s", (icao,))
    pack1 = cursor.fetchone()
    name = pack1[0]

    cursor.execute("select municipality from airports where ident = %s", (icao,))
    pack2 = cursor.fetchone()
    municipality = pack2[0]

    cursor.close()
    mydb.close()

    return name, municipality


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)