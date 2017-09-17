from bottle import route,template,error,static_file,run
frett1={"css":"css/styles.css","title":"Ætla að banna bensín og dísil bíla","text":"Kínversk stjórnvöld hafa tilkynnt að þau hafi í hyggju að banna bifreiðar sem knúnar eru jarðefnaeldsneyti.","photo":"myndir/bill.jpg","frettamadur":"Baldur Guðmundsson"}
frett2={"css":"css/styles.css","title":"Montoya setti hraðamet á Bugatti","text":"Juan Pablo Montoya, fyrrum keppandi í formúlu 1, setti heimsmet um helgina á Bugatti Chiron ofurbíl. ","photo":"myndir/bugatti.jpg","frettamadur":"Guðný Hallardóttir"}
frett3={"css":"css/styles.css","title":"Ferrari með fjölskyldubíl","text":"Smíði Ferrari jeppa verður það fyrsti fjölskyldubíllinn sem fyrirtækið framleiðir. Sergio Marchionne, forstjóri Fiat segir að af smíðinni verði en á forsendum Ferrari. Hann vildi þó ekki staðhæfa að um jeppa væri endilega að ræða, en fjölskyldubíl þó alltjent.","photo":"myndir/ferrari.jpg","frettamadur":"Jón Kristjánsson"}
listi=[frett1,frett2,frett3]

@route("/")
def index():
    return template("templates/upphafs.tpl")

@route('/<tala>')
def tala(tala):
    tala1=int(tala)-1
    dictionary=listi[tala1]
    return template("templates/index.tpl",dictionary)

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

@route('/myndir/<filename:re:.*\.jpg>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/jpg')

@route('/myndir/<filename:re:.*\.png>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/png')

@error(500)
def error404(error):
    info={"css":"/css/error.css","title":"You have an error","link":"/","linktexti":"Upphafssíða","mynd":"myndir/error.png"}
    return template("templates/error.tpl",info)

@error(404)
def error404(error):
    info={"css":"/css/error.css","title":"You have an error","link":"/","linktexti":"Upphafssíða","mynd":"myndir/error.png"}
    return template("templates/error.tpl",info)

if __name__ == "__main__":
    run(debug=True)