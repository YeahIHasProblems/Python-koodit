from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="AdminST",
    database="flight_game"
)

@app.route("/kenttä/<icao>")
def hae_kentta(icao):
    cursor = db.cursor(dictionary=True)

    sql = """
        SELECT ident AS ICAO, name AS Name, municipality AS Municipality FROM airport WHERE ident = %s"""
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result is None:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404

    return jsonify(result)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
