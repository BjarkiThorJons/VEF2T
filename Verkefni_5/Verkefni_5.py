from bottle import route,template,error,static_file,run,request,redirect,post

@route('/')
def index():
    return template("templates/index.tpl")

@route('/senda' ,method="POST")
def form():
    staerd=request.forms.get("staerd")
    staerd=int(staerd)
    alegg=request.forms.getall("alegg")
    samtals=staerd
    for x in alegg:
        samtals+=int(x)
    samtals=samtals*1.25
    info={"verd":samtals}
    return template("templates/svar.tpl",info)

run(host='localhost', port=8080, debug=True)
