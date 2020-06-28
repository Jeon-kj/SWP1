from cgi import parse_qs
from calc_template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    if environ['QUERY_STRING'] != '' :
        if a == '' and b.isdigit() == True :
            a, b= 0, int(b)
            response_body = html % {
                    'sum':a+b,
                    'mul':a*b,
            }

        elif a.isdigit() == True and b == '' :
            a, b = int(a), 0
            response_body = html % {
                    'sum':a+b,
                    'mul':a*b,
            }

        elif a == '' and b == '' :
            a, b = 0, 0
            response_body = html % {
                    'sum':a+b,
                    'mul':a*b,
            }

        elif a.isdigit() == True and b.isdigit() == True :
            a, b = int(a), int(b)
            response_body = html % {
                    'sum':a+b,
                    'mul':a*b,
            }

        elif a.isdigit() == False or b.isdigit() == False :
            response_body = html % {
                    'sum':-1,
                    'mul':-1,
            }

    else :
        response_body = html % {
                    'sum':0,
                    'mul':0,
            }


    status = '200 OK'
    response_headers = [
            ('Content-Type', 'text/html'),
            ('Conetent-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]
