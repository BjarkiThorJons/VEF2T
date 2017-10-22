import json
from bottle import *
myndir={"myndir":["myndir/pig.jpg","myndir/dog.jpg","myndir/cheetah.jpg"]}
with open("myndir.json","w") as skra:
    json.dump(myndir,skra)

with open("myndir.json","r")as skra:
    myndir=json.load(skra)

myndir=dict(myndir)
listi=list(myndir["myndir"])
listi.append("myndir/elephant.png")
myndir["myndir"]=listi

with open("myndir.json","w") as skra:
    json.dump(myndir,skra)

with open("myndir.json","r")as skra:
    myndir=json.load(skra)

myndir=dict(myndir)
listi=list(myndir["myndir"])

@route('/myndir/<filename:re:.*\.png>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/png')

@route('/myndir/<filename:re:.*\.jpg>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/png')
@route("/")
def index():
    return template("templates/index.tpl",posts=listi)

run(host='localhost', port=8080, debug=True)