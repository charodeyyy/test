def hello(environ, start_response):

  status = '200 OK'
  response_headers = [('Content-type','text/plain')]
  start_response(status, response_headers)
  # resp = environ.get('QUERY_STRING').split("&")
  # resp = [item+"\n" for item in resp]
  resp = "\n".join(environ.get('QUERY_STRING').split("&"))
  print(resp)
  return resp
