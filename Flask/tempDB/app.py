# export FLASK_APP=app.py
# export FLASK_ENV=development # will reload itself on code changes
# flask run
# flask run --host=0.0.0.0
# file name should be app.py or wsgi.py
# https://flask.palletsprojects.com/en/1.1.x/patterns/lazyloading/#converting-to-centralized-url-map




from flask import Flask
from flask import request
from markupsafe import escape


app = Flask(__name__)
if __name__ == "__main__":
   app.run(host='0.0.0.0')

temp_db = {}

@app.route('/')
@app.route('/help')
def index():
    return "render_template(rootdoc)"

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
