from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Home Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)