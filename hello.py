def hello(environ, start_response):

  status = '200 OK'
  response_headers = [('Content-type','text/plain')]
  start_response(status, response_headers)
  resp = "\n".join(environ.get('QUERY_STRING').split("&"))
  return [str.encode(resp)]
  