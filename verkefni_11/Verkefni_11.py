from re import *
from bottle import *
from pymysql import *
db=Connect(host="tsuts.tskoli.is",user="0207002620",password="snotra2000",db="0207002620_vef2verk11",)
cursor=db.cursor()
cursor.execute("select * from bilar")
numrows=int(cursor.rowcount)
bilar_listi=[]
for i in range(numrows):
    row=cursor.fetchone()
    if row:
        bilar = {}
        bilar["skraningarnumer"]=row[0]
        bilar["tegund"] = row[1]
        bilar["verksmidjunumer"] = row[2]
        bilar["skraningadagur"] = row[3]
        bilar["co2"] = row[4]
        bilar["þyngd"] = row[5]
        bilar["skodun"] = row[6]
        bilar["stada"] = row[7]
        bilar_listi.append(bilar)
@route('/')
def index():
    return template("templates/index.tpl",post=bilar_listi)

@route('/bill',method="POST")
def bill():
    cursor = db.cursor()
    cursor.execute("select * from bilar")
    numrows = int(cursor.rowcount)
    bilar_listi = []
    for i in range(numrows):
        row = cursor.fetchone()
        if row:
            bilar = {}
            bilar["skraningarnumer"] = row[0]
            bilar["tegund"] = row[1]
            bilar["verksmidjunumer"] = row[2]
            bilar["skraningadagur"] = row[3]
            bilar["co2"] = row[4]
            bilar["þyngd"] = row[5]
            bilar["skodun"] = row[6]
            bilar["stada"] = row[7]
            bilar_listi.append(bilar)
    global bilnumer
    bilnumer=request.forms.get("bill")
    for x in bilar_listi:
        if x["skraningarnumer"]==bilnumer:
            print("hæ")
            global bill
            bill=x
            return  template("templates/bill.tpl",post=bill)

@route('/d',method="POST")
def d():
    cursor = db.cursor()
    cursor.execute("select * from bilar")
    numrows = int(cursor.rowcount)
    bilar_listi = []
    for i in range(numrows):
        row = cursor.fetchone()
        if row:
            bilar = {}
            bilar["skraningarnumer"] = row[0]
            bilar["tegund"] = row[1]
            bilar["verksmidjunumer"] = row[2]
            bilar["skraningadagur"] = row[3]
            bilar["co2"] = row[4]
            bilar["þyngd"] = row[5]
            bilar["skodun"] = row[6]
            bilar["stada"] = row[7]
            bilar_listi.append(bilar)
    breyta=request.forms.get("bill")
    breyta_i=request.forms.get("texti")
    submit = request.forms.get("submit")
    numer=bill["skraningarnumer"]
    if submit == "delete":
        strengur = "delete " + "from bilar where skraningarnumer =" + ' "' + str(bill["skraningarnumer"] + '" ')
        print(strengur)
        cursor.execute(strengur)
        db.commit()
        cursor.close()
        redirect("/")
    strengur="update bilar set "+str(breyta)+" = "+str(breyta_i)+" where skraningarnumer = "+'"'+str(bill["skraningarnumer"]+'"')
    print(strengur)
    cursor.execute(strengur)
    db.commit()
    cursor.close()
    redirect("/")
@route('/+',method="POST")
def bill():
    cursor = db.cursor()
    cursor.execute("select * from bilar")
    numrows = int(cursor.rowcount)
    bilar_listi = []
    for i in range(numrows):
        row = cursor.fetchone()
        if row:
            bilar = {}
            bilar["skraningarnumer"] = row[0]
            bilar["tegund"] = row[1]
            bilar["verksmidjunumer"] = row[2]
            bilar["skraningadagur"] = row[3]
            bilar["co2"] = row[4]
            bilar["þyngd"] = row[5]
            bilar["skodun"] = row[6]
            bilar["stada"] = row[7]
            bilar_listi.append(bilar)
    skraningarnumer = request.forms.get("skraningarnumer")
    tegund = request.forms.get("tegund")
    verksmidjunumer = request.forms.get("verksmidjunumer")
    skraningardagur = request.forms.get("skraningadagur")
    co2 = request.forms.get("co2")
    þyngd = request.forms.get("t")
    skodun = request.forms.get("skodun")
    stada = request.forms.get("stada")
    print(skraningarnumer)
    print(tegund)
    print(verksmidjunumer)
    print(skraningardagur)
    print(co2)
    print(þyngd)
    print(skodun)
    print(stada)
    if len(skraningarnumer)>10 or len(skraningarnumer)<6:
        redirect("/")
    cursor.execute("""insert into bilar(skraningarnumer,Tegund,verksmidjunumer,skraningardagur,co2,þyngd,skodun,stada) values(%s,%s,%s,%s,%s,%s,%s,%s)""", (skraningarnumer, tegund,verksmidjunumer,skraningardagur,co2,þyngd,skodun,stada))
    db.commit()
    cursor.close()
    redirect("/")
@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

run(host='localhost', port=8080, debug=True)