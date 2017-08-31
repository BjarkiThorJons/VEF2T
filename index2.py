from bottle import route, run

@route('/hallo/heimur2')
def hello():
    return "<body><p>Halló heimur</p></body>"
run(host='localhost', port=8080)