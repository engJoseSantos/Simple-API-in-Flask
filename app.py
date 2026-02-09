from flask import Flask, jsonify, render_template, request

class Crypto:
    def __init__(self, id, name, code, value_to_usd):
        self.id = id
        self.name = name
        self.code = code
        self.value_to_usd = value_to_usd
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" :self.name,
            "code" :self.code.upper(),
            "price_usd" :self.value_to_usd
        }

cryptos = {
    "btc" : Crypto(1, "Bitcoin", "BTC", 73550.97),
    "eth" : Crypto(2, "Ethereum", "ETH", 2074.85),
    "ltc" : Crypto(3, "Litecoin", "LTC", 55.44),
    "sol" : Crypto(4, "Solana", "SOL", 88.20),
    "doge": Crypto(5, "Dogecoin", "DOGE", 0.098)
}       
app = Flask(__name__)

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

        #if not name or not email or not message:
        #    return jsonify({"error": "All fields are required"}), 400

        #if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        #    return jsonify({"error": "Invalid email"}), 400

        print(name)
        print(email)
        print(message)

        return jsonify({
            "status": "success",
            "message": "Your message was received"
        }), 201


@app.route("/token/<string:code>")
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
    app.run(debug=True)