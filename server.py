# first of all import the socket library 
import socket, emailSender, os               
from random import randint
randint(100, 999)
passcode = 'password1'
SecAuth = randint(100000, 999999)
SecAuth = str(SecAuth)
print(SecAuth)
command = "python C:\\Users\\David\\Documents\\MFA19\\cyberPhy\\finalProject\\emailSender.py "+SecAuth
print(command)
s = socket.socket()          
print("Socket successfully created")

port = 12345                
s.bind(('', port))         
print ("socket binded to %s" %(port))
  
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening")          
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print ('Got connection from', addr)
  
   # send a thank you message to the client.  
   c.send('Thank you for connecting'.encode()) 
   c.send('please enter enter your password to be granted server access'.encode()) 
   password = c.recv(1024)
   password = password.decode("utf-8")
   print(password)
   if(passcode == password):
       c.send('your password was correct, please see your email for the 2FA code'.encode())
       #os.system(command)
       #python emailSender.py '12345'
       #call to email program here
       emailSender.send(SecAuth)
       TwoFA = c.recv(1024).decode("utf-8")
       if(SecAuth == TwoFA):
            c.send('you have gotten both forms of authentication correct, and have been granted access'.encode())
       else:
            c.send('you have gotten the second form of authentication incorrect and are being denied access'.encode())
            c.close()
   else:
        c.send('you have gotten the first form of authentication incorrect and are being denied access'.encode())
        c.close()


  
   # Close the connection with the client 
   c.close() 