import requests
from math import *
from threading import Thread as thread


def scan_1(host, sec):
  
  global scan
  line = 0
  sub_list = open("sub_list.txt")
  
  subs = sub_list.read().split()
  length = len(subs) -1 * 0.5

  for i in range(floor(length -1)):
    try:
        sub = subs[line]
        if sec:
          link = f"https://{sub}.{host}"
      
          try:
            requests.get(link, timeout=0.3)
      
            scan.output.append(link)
            
          except requests.ConnectionError:
            pass
      
          line += 2
        
        else:
          
          link = f"http://{sub}.{host}"
      
          try:
            requests.get(link, timeout=0.3)
      
            scan.output.append(link)
      
          except ConnectionError:
            pass
      
          line += 2
    except:
      pass


def scan_2(host, sec):
  global scan
  line = 1
  sub_list = open("sub_list.txt")
  
  subs = sub_list.read().split()
  length = len(subs) -1 * 0.5

  for i in range(floor(length -1)):
    try:
        sub = subs[line]
        if sec:
          link = f"https://{sub}.{host}"
      
          try:
            requests.get(link, timeout=0.3)
      
            scan.output.append(link)
      
          except requests.ConnectionError:
            pass
      
          line += 2
        
        else:
          
          link = f"http://{sub}.{host}"
      
          try:
            requests.get(link, timeout=0.3)
      
            scan.output.append(link)
      
          except ConnectionError:
            pass
      
          line += 2
    except:
      pass
  
class scan:
  output = []

def start(host_domain, secure):
  r = thread(target=scan_1(host_domain, secure)).start()
  p = thread(target=scan_2(host_domain, secure)).run()
