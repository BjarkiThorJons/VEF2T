from bottle import route,template,error,static_file,run,request,redirect,post
import csv
@route('/')
def index():
    return template("templates/index.tpl")

@route('/senda' ,method="POST")
def form():
    info={}
    nafn=request.forms.get("nafn")
    nafn=nafn.strip(" ")
    lykilord=request.forms.get("lykilord")
    notendanafn = request.forms.get("notendanafn")
    notendanafn=notendanafn.strip(" ")
    email = request.forms.get("email")
    email=email.strip(" ")
    simi = request.forms.get("simi")
    info.update({"nafn":nafn,"notendanafn":notendanafn,"email":email,"simi":simi,"lykilord":lykilord})
    if " " in notendanafn:
        info.update({"villa":"Ekki hafa bil í notendanafni"})
        return template("templates/villa.tpl", info)
    elif len(lykilord)<5:
        info.update({"lykilord":"","villa": "Lykilorð of stutt"})
        return template("templates/villa.tpl",info)
    elif "@" not in email or "." not in email:
        info.update({email:"","villa":"Email villa"})
        return template("templates/villa.tpl",info)
    elif len(simi)<7 or len(simi)>9:
        info.update({simi:"","villa":"Símanúmer rangt"})
        return template("templates/villa.tpl", info)
    else:
        with open("notendur.csv","a",newline='') as t:
            spamwriter = csv.writer(t, delimiter=',')
            spamwriter.writerow([nafn,lykilord,notendanafn,email,simi])
    return template("templates/svar.tpl")


@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

run(host='localhost', port=8080, debug=True)
