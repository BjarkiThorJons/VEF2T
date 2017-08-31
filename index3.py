from bottle import route, run
@route('/<id:int>')
def id(id):
    if id==1:
        return "<p>Gunnar</p>"
    if id==2:
        return "<p>Daniel</p>"
    if id==3:
        return "<p>Þórarinn</p>"
    else:
        return "<p>nei takk</p>"
run(host='localhost', port=8080)