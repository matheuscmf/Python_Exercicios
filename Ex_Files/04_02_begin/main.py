from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Olá Navegantes,vamos estudar esta bela linguagem que é Python!!!!!"

app.run(debug=True)
