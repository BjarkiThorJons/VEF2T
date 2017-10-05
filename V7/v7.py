from bottle import route,template,error,static_file,run,request,redirect,post,response
import datetime

@route("/")
def index():
    return template("templates/index.tpl")

nafn="admin"
password="admin"

@route('/login' ,method="POST")
def login():
    notendanafn=request.forms.get("notendanafn")
    lykilord=request.forms.get("lykilord")
    if notendanafn==nafn and lykilord==password:
        t=datetime.datetime.now() + datetime.timedelta(days=1000000)
        response.set_cookie("user", "yes", expires=t)
    redirect('/leynisida')

@route('/leynisida')
def leynisida():
    if request.get_cookie('user'):
        return template('templates/leynisida.tpl')
    else:
        redirect('/')

@route('/logout', method="POST")
def logout():
    response.set_cookie("user", "", expires=0)
    redirect('/')

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')


run(host='localhost', port=8080, debug=True)