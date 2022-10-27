import socket
host=socket.gethostname()
IPadd=socket.gethostbyname(host)
print("your host name is:",host)
print("\nyour ip adress is :",IPadd)