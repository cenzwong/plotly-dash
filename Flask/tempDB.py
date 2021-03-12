# Last Edit: 20210312, By Cenz
# export FLASK_APP=app.py
# export FLASK_ENV=development # will reload itself on code changes
# flask run
# flask run --host=0.0.0.0

from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)

temp_db = {}

@app.route('/')
def index():
    return 'Index Page'

# http://127.0.0.1:5000/set/cenz?data=123
@app.route('/set/<key>')
def set_(key):
    # show the user profile for that user
    temp_db[key] = request.args.get('data')
    return temp_db[key]

# http://127.0.0.1:5000/get/cenz
@app.route('/get/<key>')
def get_(key):
    # show the user profile for that user
    if key in temp_db:
        return temp_db[key]
    else:
        return ""

# http://127.0.0.1:5000/clear/cenz
@app.route('/clear/<key>')
def clear_(key):
    # show the user profile for that user
    return temp_db.pop(key, "")

# http://127.0.0.1:5000/getAll
@app.route('/getAll')
def getAll_():
    print(str(temp_db))
    return str(temp_db)

# http://127.0.0.1:5000/clearAll?yes
@app.route('/clearAll')
def clearAll_():
    if request.args.get("yes") == "":
        temp_db.clear()
        return str(temp_db)
    
    return "Please confirm with ?yes"
