from flask import Flask, render_template, request, jsonify
from services.password_service import analyze_password
from services.generator import generate_password

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    password = data.get("password", "")
    result = analyze_password(password)
    return jsonify(result)


@app.route("/api/generate", methods=["GET"])
def generate():
    password = generate_password()
    return jsonify({"password": password})


if __name__ == "__main__":
    app.run(debug=True)