def send(msg):
  print("MSGSEND")
  print("Sending message :\"" + msg + "\"...")
  with open("tosend.txt", "a+") as msgs:
    msgs.write(msg + "\n")
  print("Sent message, check PyChat for confirmation!")

def __init__():
  import os
  from http.server import HTTPServer, CGIHTTPRequestHandler
  # Make sure the server is created at current directory
  os.chdir('.')
  # Create server object listening the port 80
  server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
  # Start the web server
  server_object.serve_forever()
  