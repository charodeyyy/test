def hello(environ, start_response):

	response_string = [('Content-type', 'text/plain')]
    start_response('200 OK', response_string)
    
	return "\n".join(environ.get('QUERY_STRING').split("&"))