from bottle import route, run

@route('/hallo/heimur')
def hello():
    return "Halló heimur"
run(host='localhost', port=8080)