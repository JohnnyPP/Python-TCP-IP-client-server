import socket

ip = raw_input("IP-Address: ") 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((ip, 50000))

try: 
    while True: 
        message = raw_input("Message: ") 
        s.send(message) 
        answer = s.recv(1024) 
        print "[%s] %s" % (ip,answer) 
finally: 
    s.close()