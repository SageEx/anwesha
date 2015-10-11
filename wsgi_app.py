#-*- coding: utf-8 -*-
def wsgi_app(environ, start_response):
    import sys
    output = sys.version.encode('utf8')
    status = '200 OK'
    headers = [('Content-type', 'text/plain'),
               ('Content-Length', str(len(output)))]
    start_response(status, headers)
    # yield output
    return [output]

# mod_wsgi need the *application* variable to serve our small app
application = wsgi_app

# def wsgi_app(environ, start_response):
#     status = '200 OK'
#     output = 'Hello World!'

#     response_headers = [('Content-type', 'text/plain'),
#                         ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)

#     # return [output]
#     yield output

# application = wsgi_app
