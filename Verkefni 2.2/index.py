from bottle import route,run,static_file,error
@route('/')
def index():
    return'''
    <!DOCTYPE html>
    <html>
    <head>
	    <title></title>
	    <meta charset="utf-8">
        <link type="text/css" href="/css/styles.css" rel="stylesheet">
    </head>
    <body>
    <a href="1">
    <img src="myndir/ITL-I57500.png" alt="Bottle">
    </a>
    <a href="2">
    <img src="myndir/ITL-I57600.png" alt="Bottle">
    </a>
    <a href="3">
    <img src="myndir/ITL-I57600K.jpeg" alt="Bottle">
    </a>
    <a href="4">
    <img src="myndir/ITL-I77700.png" alt="Bottle">
    </a>
    <a href="5">
    <img src="myndir/ITL-I77700K.png" alt="Bottle">
    </a>
    <a href="6">
    <img src="myndir/AMD-RYZEN51600.jpg" alt="Bottle">
    </a>
    <a href="7">
    <img src="myndir/AMD-RYZEN51600X.jpg" alt="Bottle">
    </a>
    <a href="8">
    <img src="myndir/AMD-RYZEN71700.jpg" alt="Bottle">
    </a>
    <a href="9">
    <img src="myndir/AMD-RYZEN71700X.jpg" alt="Bottle">
    </a>
    <a href="10">
    <img src="myndir/AMD-RYZEN71800X.jpg" alt="Bottle">
    </body>
    </html>


    '''
@route("/<tala>")
def tala(tala):
    listimynd=['<img src="myndir/ITL-I57500.png" alt="Bottle">','<img src="myndir/ITL-I57600.png" alt="Bottle">','<img src="myndir/ITL-I57600K.jpeg" alt="Bottle">','<img src="myndir/ITL-I77700.png" alt="Bottle">','<img src="myndir/ITL-I77700K.png" alt="Bottle">','<img src="myndir/AMD-RYZEN51600.jpg" alt="Bottle">','<img src="myndir/AMD-RYZEN51600X.jpg" alt="Bottle">','<img src="myndir/AMD-RYZEN71700.jpg" alt="Bottle">','<img src="myndir/AMD-RYZEN71700X.jpg" alt="Bottle">','<img src="myndir/AMD-RYZEN71800X.jpg" alt="Bottle">']
    listitexti=['Sökkull: 1151 <br> Örgjörva týpa: Intel i5-7500<br> Fjöldi kjarna: 4<br>Fjöldi þráða: 4<br>Örgjörvatíðni: 3.4Ghz<br>Hámarks Turbo örgjörvatíðni: 3.8GHz<br>Flýtiminni: 6MB<br>Fjöldi QPI tenginga: <br>Instruction Set: 64-bit<br>Instruction Set Extensions: SSE 4.1/4.2, AVX 2.0<br>Framleiðslutækni: 14nm<br>Hámarksafl: 65W<br>Tækniupplýsingar um minni: <br>Hámarks minnisstærð: 64GB<br>Tegund minnis: DDR3L 1333/1600 DDR4 2133/2400<br>Fjöldi minnisrása: 2<br>Tækniupplýsingar um skjástýringu: <br>Skjástýring á örgjörva: Intel HD Graphics 630<br>Grunntíðni skjástýringar: 350MHz<br>Hámarkstíðni skjástýringar: 1.15GHz',
                'Sökkull: 1151 <br> Örgjörva týpa: Intel i5-7600<br> Fjöldi kjarna: 4<br>Fjöldi þráða: 4<br>Örgjörvatíðni: 3.5Ghz<br>Hámarks Turbo örgjörvatíðni: 4.1GHz<br>Flýtiminni: 6MB<br>Fjöldi QPI tenginga: <br>Instruction Set: 64-bit<br>Instruction Set Extensions: SSE 4.1/4.2, AVX 2.0<br>Framleiðslutækni: 14nm<br>Hámarksafl: 65W<br>Tækniupplýsingar um minni: <br>Hámarks minnisstærð: 64GB<br>Tegund minnis: DDR3L 1333/1600 DDR4 2133/2400<br>Fjöldi minnisrása: 2<br>Tækniupplýsingar um skjástýringu: <br>Skjástýring á örgjörva: Intel HD Graphics 630<br>Grunntíðni skjástýringar: 350MHz<br>Hámarkstíðni skjástýringar: 1.15GHz',
                'Sökkull: 1151 <br> Örgjörva týpa: Intel i5-7600K<br> Fjöldi kjarna: 4<br>Fjöldi þráða: 4<br>Örgjörvatíðni: 3.8Ghz<br>Hámarks Turbo örgjörvatíðni: 4.2GHz<br>Flýtiminni: 6MB<br>Fjöldi QPI tenginga: <br>Instruction Set: 64-bit<br>Instruction Set Extensions: SSE 4.1/4.2, AVX 2.0<br>Framleiðslutækni: 14nm<br>Hámarksafl: 91W<br>Tækniupplýsingar um minni: <br>Hámarks minnisstærð: 64GB<br>Tegund minnis: DDR3L 1333/1600 DDR4 2133/2400<br>Fjöldi minnisrása: 2<br>Tækniupplýsingar um skjástýringu: <br>Skjástýring á örgjörva: Intel HD Graphics 630<br>Grunntíðni skjástýringar: 350MHz<br>Hámarkstíðni skjástýringar: 1.15GHz',
                'Sökkull: 1151 <br> Örgjörva týpa: Intel i7-7700<br> Fjöldi kjarna: 4<br>Fjöldi þráða: 8<br>Örgjörvatíðni: 3.6Ghz<br>Hámarks Turbo örgjörvatíðni: 4.2GHz<br>Flýtiminni: 8MB<br>Fjöldi QPI tenginga: <br>Instruction Set: 64-bit<br>Instruction Set Extensions: SSE 4.1/4.2, AVX 2.0<br>Framleiðslutækni: 14nm<br>Hámarksafl: 65W<br>Tækniupplýsingar um minni: <br>Hámarks minnisstærð: 64GB<br>Tegund minnis: DDR3L 1333/1600 DDR4 2133/2400<br>Fjöldi minnisrása: 2<br>Tækniupplýsingar um skjástýringu: <br>Skjástýring á örgjörva: Intel HD Graphics 630<br>Grunntíðni skjástýringar: 350MHz<br>Hámarkstíðni skjástýringar: 1.15GHz',
                'Sökkull: 1151 <br> Örgjörva týpa: Intel i7-7700K<br> Fjöldi kjarna: 4<br>Fjöldi þráða: 8<br>Örgjörvatíðni: 4.2Ghz<br>Hámarks Turbo örgjörvatíðni: 4.5GHz<br>Flýtiminni: 8MB<br>Fjöldi QPI tenginga: <br>Instruction Set: 64-bit<br>Instruction Set Extensions: SSE 4.1/4.2, AVX 2.0<br>Framleiðslutækni: 14nm<br>Hámarksafl: 91W<br>Tækniupplýsingar um minni: <br>Hámarks minnisstærð: 64GB<br>Tegund minnis: DDR3L 1333/1600 DDR4 2133/2400<br>Fjöldi minnisrása: 2<br>Tækniupplýsingar um skjástýringu: <br>Skjástýring á örgjörva: Intel HD Graphics 630<br>Grunntíðni skjástýringar: 350MHz<br>Hámarkstíðni skjástýringar: 1.15GHz',
                'Sökkull: AM4 <br> Örgjörva týpa: AMD Ryzen 5 1600<br> Fjöldi kjarna: 6<br>Fjöldi þráða: 12<br>Örgjörvatíðni: 3.2Ghz<br>Hámarks Turbo örgjörvatíðni: 3.6GHz<br>XFR: NA<br>Flýtiminni: 16MB<br>Framleiðslutækni: 14nm<br>Instruction Set: 64-bit<br>Hámarksafl: 65W<br>Tegund minnis: DDR4<br>Kæling Wraith Spire<br>',
                'Sökkull: AM4 <br> Örgjörva týpa: AMD Ryzen 5 1600X<br> Fjöldi kjarna: 6<br>Fjöldi þráða: 12<br>Örgjörvatíðni: 3.6Ghz<br>Hámarks Turbo örgjörvatíðni: 4.0GHz<br>XFR: 4.0GHz+<br>Flýtiminni: 16MB<br>Framleiðslutækni: 14nm<br>Instruction Set: 64-bit<br>Hámarksafl: 95W<br>Tegund minnis: DDR4<br>Kæling fylgir ekki<br>',
                'Sökkull: AM4 <br> Örgjörva týpa: AMD Ryzen 7 1700<br> Fjöldi kjarna: 6<br>Fjöldi þráða: 12<br>Örgjörvatíðni: 3.0Ghz<br>Hámarks Turbo örgjörvatíðni: 3.7GHz<br>XFR: NA<br>Flýtiminni: 20MB<br>Framleiðslutækni: 14nm<br>Instruction Set: 64-bit<br>Hámarksafl: 65W<br>Tegund minnis: DDR4<br>',
                'Sökkull: AM4 <br> Örgjörva týpa: AMD Ryzen 7 1700X<br> Fjöldi kjarna: 8<br>Fjöldi þráða: 16<br>Örgjörvatíðni: 3.4Ghz<br>Hámarks Turbo örgjörvatíðni: 3.8GHz<br>XFR: 3.8GHz+<br>Flýtiminni: 20MB<br>Framleiðslutækni: 14nm<br>Instruction Set: 64-bit<br>Hámarksafl: 95W<br>Tegund minnis: DDR4<br>',
                'Sökkull: AM4 <br> Örgjörva týpa: AMD Ryzen 7 1800X<br> Fjöldi kjarna: 8<br>Fjöldi þráða: 16<br>Örgjörvatíðni: 3.6Ghz<br>Hámarks Turbo örgjörvatíðni: 4.0GHz<br>XFR: 4.0GHz+<br>Flýtiminni: 20MB<br>Framleiðslutækni: 14nm<br>Instruction Set: 64-bit<br>Hámarksafl: 95W<br>Tegund minnis: DDR4<br>',

                ]

    tala2=int(tala)-1
    return '<!DOCTYPE html><html><head></head><body>',listimynd[tala2],'<p>',listitexti[tala2],'</p></body></hmtl>'

@route('/myndir/<filename:re:.*\.png>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/png')

@route('/myndir/<filename:re:.*\.jpeg>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/jpeg')

@route('/myndir/<filename:re:.*\.jpg>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/jpg')

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')




run(host='localhost', port=8080, debug=True)
