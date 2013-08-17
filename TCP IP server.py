import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("", 50000)) 
s.listen(1)

try: 
    while True: 
        comm, addr = s.accept() 
        while True: 
            data = comm.recv(1024)

            if not data: 
                comm.close() 
                break

            print "[%s] %s" % (addr[0], data) 
            message = raw_input("Answer: ") 
            comm.send(message) 
finally: 
    s.close()