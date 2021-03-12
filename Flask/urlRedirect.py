# sudo su
# . ./venvFlask/bin/activate
# to run, export FLASK_APP=hello.py
# flask run --host=0.0.0.0 --port=80

# To run it detach flask run --host=0.0.0.0 --port=80 &
# kill -2 PID_OF_flask (you can check it with ps)
# ps aux | grep flask

from flask import Flask, redirect

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

@app.route('/')
@app.route('/help')
def index():
    return "help"

@app.route('/edit')
def edit():
    return redirect("http://172.16.10.1:8080")

# ====================== Sharepoint ======================
@app.route('/a')
@app.route('/along')
def a():
    return redirect("https://url1")

@app.route('/b')
@app.route('/blong/b')
def b():
    return redirect("https://2")

@app.route('/c')
@app.route('/c/cc')
def c():
    return redirect("https://3")
