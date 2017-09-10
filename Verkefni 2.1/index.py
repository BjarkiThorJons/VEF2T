from bottle import route,run,static_file,error
@route('/<steve>')
def steve(steve):
    if steve=="steve":
        return '''
        <!DOCTYPE html>
            <html>
                <head>
                    <title>Seve Jobs</title>
                    <meta charset="utf-8">
                    <link type="text/css" href="/css/styles.css" rel="stylesheet">
                </head>
                <body>
                    <a href="/bio">Steve Jobs Bio</a>
                    <a href="/pictures">Pictures</a>
                    <h1>
                        Steve Jobs
                    </h1>
                     <img src="myndir/steve_jobs.png" alt="Bottle">
                    <p>
                        Steve Jobs (born as Steven Paul Jobs February 24, 1955 – October 5, 2011) was an American entrepreneur, businessman, inventor, and industrial designer.
                        Jobs was the chairman, and the chief executive officer (CEO), and a co-founder of Apple Inc.;
                        CEO and majority shareholder of Pixar;[2] a member of The Walt Disney Company's board of directors following its acquisition of Pixar;
                        and founder, chairman, and CEO of NeXT. Jobs and Apple co-founder Steve Wozniak are widely recognized as pioneers of the microcomputer revolution of the 1970s and 1980s.
                    </p>
                </body>
            </html>
            '''
    if steve=='bio':
        return '''
            <!DOCTYPE html>
                <html>
                    <head>
                        <title>Seve Jobs biography</title>
                        <meta charset="utf-8">
                        <link type="text/css" href="/css/styles2.css" rel="stylesheet">
                        </head>
                        <body>
                            <a href="/steve">Steve</a>
                            <a href="/pictures">Pictures</a>
                            <h1>
                                Steve Jobs
                            </h1>
                             <img src="myndir/steve_jobs2.png" alt="Bottle">
                            <p>
                             Steve Jobs was born in San Francisco, California, on February 24, 1955,
                             to two University of Wisconsin graduate students who gave him up
                             for adoption. Smart but directionless, Jobs experimented with different
                             pursuits before starting Apple Computer with Steve Wozniak in 1976.
                             Apple's revolutionary products, which include the iPod, iPhone and iPad,
                             are now seen as dictating the evolution of modern technology,
                             with Jobs having left the company in 1985 and returning more than a decade later.
                             He died in 2011, following a long battle with pancreatic cancer.
                            </p>
                        </body>
                    </html>
            '''
    if steve=="pictures":
        return'''
            <!DOCTYPE html>
                <html>
                    <head>
                        <title>Seve Jobs Pictures</title>
                        <meta charset="utf-8">
                        <link type="text/css" href="/css/styles2.css" rel="stylesheet">
                        </head>
                        <body>
                            <a href="/steve">Steve</a>
                            <a href="/bio">Biography</a>
                            <h1>
                                Steve Jobs
                            </h1>
                             <img class="img1" src="myndir/steve_jobs.png" alt="Bottle">
                             <img class="img2" src="myndir/steve_jobs2.png" alt="Bottle">
                             <img class="img3" src="myndir/steve_jobs3.png" alt="Bottle">
                            <p>
                             He was born in San Francisco to parents who had to put him up for adoption
                             at birth; he was raised in the San Francisco Bay Area during the 1960s.
                             Jobs then attended Reed College in 1972 before dropping out,
                             and decided to travel through India in 1974 seeking enlightenment
                             and studying Zen Buddhism. Jobs's declassified FBI report
                             stated that an acquaintance knew that Jobs had used marijuana
                             (the formerly illegalized drug in California), and LSD
                             while he was in college. Jobs once told a reporter that taking
                             LSD was "one of the two or three most important things" he did in
                             his life.
                            </p>
                        </body>
                    </html>
            '''

    else:
        return'''
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body>
           <a href="/bio">Biography</a>
           <a href="/pictures">Pictures</a>
           <a href="/steve">Steve</a>
           </body>
           </html>

        '''

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

@route('/myndir/<filename:re:.*\.png>')
def send_mynd(filename):
    return static_file(filename, root='myndir', mimetype='image/png')

@error(404)
def error404(error):
    return '''
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body>
           <a href="/bio">Biography</a>
           <a href="/pictures">Pictures</a>
           <a href="/steve">Steve</a>
           </body>
           </html>

        '''
run(host='localhost', port=8080, debug=True)
