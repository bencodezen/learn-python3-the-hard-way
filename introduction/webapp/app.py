from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
  greeting = "Test"
  return render_template("index.html", greeting=greeting)

@app.route("/hello")
def index():
  name = request.args.get('name', 'Nobody')

  if name:
    greeting = f"Hello, {name}"
  else:
    greeting = "Hello world!"
  
  return render_template("index.html", greeting=greeting)

@app.route("/form", methods=['POST', 'GET'])
def form():
  if request.method == "POST":
    name = request.form['name']
    return render_template("index.html", greeting=name)
  else:
    return render_template("form.html")

if __name__ == "__main__":
  app.run()
