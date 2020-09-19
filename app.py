import socket
print("Hello Shivam" )
print("You are on " + socket.gethostbyaddr(socket.gethostname())[0] + " machine")
