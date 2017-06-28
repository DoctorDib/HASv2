import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('151.80.140.199', 2526)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)


try:
  while True:
      # Send data
      message = "This is the message.  It will be repeated."
      print (sys.stderr, 'sending "%s"' % message)
      sock.sendall(message.encode('ascii'))

      # Look for the response
      amount_received = 0
      amount_expected = len(message)


except:
  print ("ERROR")
