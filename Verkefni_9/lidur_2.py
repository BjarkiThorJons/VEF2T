from bottle import *
import urllib.request,json

with urllib.request.urlopen("http://apis.is/concerts") as url:
    data=json.loads(url.read().decode())
@route("/")
def index():
    return template("templates/lidur_2.tpl",posts=data)

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')
@route('/myndir/<filename:re:.*\.jpg>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/png')

run(host='localhost', port=8080, debug=True)