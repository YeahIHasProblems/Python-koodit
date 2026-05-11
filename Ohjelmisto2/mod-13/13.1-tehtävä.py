from flask import Flask, jsonify

app = Flask(__name__)

def on_alkuluku(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

@app.route("/alkuluku/<int:luku>", methods=["GET"])
def tarkista_alkuluku(luku):
    tulos = on_alkuluku(luku)
    vastaus = {
        "Number": luku,
        "isPrime": tulos
    }
    return jsonify(vastaus)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
