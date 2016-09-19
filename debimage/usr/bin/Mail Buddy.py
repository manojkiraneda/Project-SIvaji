#!/usr/bin/python

from __future__ import unicode_literals
from imapclient import IMAPClient
from subprocess import call
from multiprocessing import Process

USERNAME = 'manoj.kiran@iiitb.org'
PASSWORD = 'XXXXXXX'
server = 'outlook.office365.com'
new_message = "Hai sir You got a Message"
no_message = "Hai sir you didn't get any Message"
PORT = 993
ssl_id = True

def espeak_fun(my_message):
    call(['espeak',my_message])
def xcow_fun(my_message):
    call(['xcowsay','-t 10',my_message])

serverobj = IMAPClient(server,ssl=ssl_id)
serverobj.login(USERNAME,PASSWORD)
selection_info = serverobj.select_folder("INBOX")
# print selection_info
total_number = selection_info['EXISTS']
seen_number = len(serverobj.search('SEEN'))
# print total_number
# print seen_number
if total_number - seen_number == 0:
    p1 = Process(target=espeak_fun(no_message))
    p1.start()
    p2 = Process(target=xcow_fun(no_message))
    p2.start()
    p1.join()
    p2.join()
else:
    p1 = Process(target=espeak_fun(new_message))
    p1.start()
    p2 = Process(target=xcow_fun(new_message))
    p2.start()
    p1.join()
    p2.join()
serverobj.logout()
