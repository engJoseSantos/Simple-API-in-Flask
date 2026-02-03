from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Simple API in flask"

@app.route("/python")
def info_python():
    return "Python is a high-level, general-purpose programming language."

if __name__ == "__main__":
    app.run(debug=True)