# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
print (s.recv(1024)decode("utf-8"))
print (s.recv(1024).decode("utf-8"))
password = input("Type your password and press enter: ")
s.send(password.encode())
print (s.recv(1024)decode("utf-8"))
password = input("Type the 2FA code and press enter: ")
# close the connection 
s.close()   