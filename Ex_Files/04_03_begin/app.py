import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    
    results = []
    if not request.args.get("surname"):
        return jsonify(results)

    search_string = request.args.get("surname").lower().strip()
    
    for laureate in laureates:
        if search_string in laureate("surname").lower():
            results.append(laureate)
    return jsonify(results)

app.run(debug=True)
