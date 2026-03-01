from flask import Flask, jsonify, render_template, request
from crypto import *
import re
import secrets
import hashlib


# This dictionary is just a simulation with static data
# In the future, it will be updated automatically.
cryptos = {
    "btc" : Crypto(1, "Bitcoin", "BTC", 69869.73),
    "eth" : Crypto(2, "Ethereum", "ETH", 2086.21),
    "ltc" : Crypto(3, "Litecoin", "LTC", 56.41),
    "sol" : Crypto(4, "Solana", "SOL", 88.28),
    "doge": Crypto(5, "Dogecoin", "DOGE", 0.11)
}   
API_KEY = ""    
app = Flask(__name__)

def generate_api_key():
    #random_string = secrets.token_hex(32)
    #return hashlib.sha256(random_string.encode()).hexdigest()
    return secrets.token_hex(16)

def require_api_key(f):
    def decorated(*args, **kwargs):
        key = request.headers.get("x-api-key")

        if not key:
            return jsonify({"error": "API key is missing"}), 401

        if key != API_KEY:
            return jsonify({"error": "Invalid API key"}), 403

        return f(*args, **kwargs)

    decorated.__name__ = f.__name__
    return decorated

@app.route("/")
def index():
    #return "Simple API in flask"
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    # GET
    if request.method == "GET":
        return render_template("contact.html")

    # POST 
    if request.method == "POST":
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        if not name or not email or not message:
            return jsonify({"error": "All fields are required"}), 400

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"error": "Invalid email"}), 400

        print(name)
        print(email)
        print(message)

        return jsonify({
            "status": "success",
            "message": "Your message was received"
        }), 201


@app.route("/token/<string:code>")
@require_api_key
def get_crypto(code):
    crypto = cryptos.get(code.lower())

    if not crypto:
        return jsonify({"error": "Crypto not found"}), 404

    return jsonify(crypto.to_dict())

@app.route("/tokens")
def get_tokens():
    return jsonify({
        "cryptos" : [c.to_dict() for c in cryptos.values()]
    })

if __name__ == "__main__":
    API_KEY = generate_api_key()
    print(API_KEY)
    app.run(debug=True)