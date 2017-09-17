from bottle import route,template,error,static_file,run

@route('/steve')
def steve():
    info={"css":"/css/styles.css","title":"Steve Jobs","mynd":"myndir/steve_jobs.png","link1":"bio","link2":"pictures","texti":"Steve Jobs (born as Steven Paul Jobs February 24, 1955 – October 5, 2011) was an American entrepreneur, businessman, inventor, and industrial designer.Jobs was the chairman, and the chief executive officer (CEO), and a co-founder of Apple Inc.;CEO and majority shareholder of Pixar;[2] a member of The Walt Disney Company's board of directors following its acquisition of Pixar; and founder, chairman, and CEO of NeXT. Jobs and Apple co-founder Steve Wozniak are widely recognized as pioneers of the microcomputer revolution of the 1970s and 1980s."}
    return template("templates/steve_template.tpl",info)


@route('/bio')
def steve():
    info = {"css":"/css/styles.css","title": "Steve Jobs biography", "mynd": "myndir/steve_jobs2.png", "link1": "steve", "link2": "pictures",
            "texti":"Steve Jobs was born in San Francisco, California, on February 24, 1955,to two University of Wisconsin graduate students who gave him up for adoption. Smart but directionless, Jobs experimented with differen pursuits before starting Apple Computer with Steve Wozniak in 1976. Apple's revolutionary products, which include the iPod, iPhone and iPad, are now seen as dictating the evolution of modern technology, with Jobs having left the company in 1985 and returning more than a decade later. He died in 2011, following a long battle with pancreatic cancer."}
    return template("templates/steve_template.tpl", info)

@route('/pictures')
def steve():
    info = {"css":"/css/styles2.css","title": "Steve Jobs biography", "mynd1": "myndir/steve_jobs.png","mynd2":"myndir/steve_jobs2.png","mynd3":"myndir/steve_jobs3.png", "link1": "steve", "link2": "bio"}
    return template("templates/pictures.tpl", info)

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

@route('/myndir/<filename:re:.*\.png>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/png')

@error(404)
def error404(error):
    info={"css":"/css/error.css","title":"U ave en error","link1":"steve","link2":"bio","link3":"pictures","mynd":"myndir/error.png"}
    return template("templates/error.tpl",info)

run(host='localhost', port=8080, debug=True)
