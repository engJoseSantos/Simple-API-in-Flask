from flask import Flask

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
            "code" :self.code,
            "value" :self.value_to_usd
        }
app = Flask(__name__)

@app.route("/")
def index():
    return "Simple API in flask"

@app.route("/python")
def info_python():
    return "Python is a high-level, general-purpose programming language."

if __name__ == "__main__":
    btc = Crypto(1, "Bitcoin", "BTC", 73550.97)
    print(btc.to_dict())
    app.run(debug=True)