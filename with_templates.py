from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name=''):
    return render_template("index.html",name=name)
        
app.run(debug=True)

