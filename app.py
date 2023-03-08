from flask import Flask, render_template

app = Flask(__name__)

jobs = [1,2,3,4,5]

@app.route("/")
def hello_world():
  return render_template("home.html", jobs = jobs)

  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug = True)