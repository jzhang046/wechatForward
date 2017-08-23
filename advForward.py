#!/usr/bin/python

import itchat
from itchat.content import *
import re
import sys
#from pprint import pprint

#TODO: 
#   Add logging function. 
def loginMessage(): 
    itchat.send('Login Successful', master)
    print('Login Successful')

masterAlias='jyzhang__'
master='master'
#Set the default master account according to wechatID 

if len(sys.argv) > 1:
    masterAlias=sys.argv[1]
#Set to user specified master account. 

itchat.auto_login(loginCallback=loginMessage, enableCmdQR=False, picDir='/dir_to_QR/QR.png', hotReload=True)
#Login
#Note that, this requires to manually change the setting in the itchat package. 
#I don't know if itchat support this, 
#but I just changed the package to just download the QR code 
#without doing anything else. 

friendUserName=[]
friendDispName=[]
#Create two lists for username and the displayed name. 
friendList=itchat.get_friends(update=True)[1:]
for friend in friendList:
    friendUserName.append(friend['UserName'])
    #Set username, a complecated and unique ID

    tmp_DispName=friend['RemarkName']
    if tmp_DispName=='':
        friendDispName.append(friend['NickName'])
    else:
        friendDispName.append(tmp_DispName)
    #Set displayed name. 
    #If there isn't a remark name, use nick name instead. 
    
    #pprint(friend)
    #if friend['Alias']==masterAlias:
    if friend['NickName'] == masterAlias:
        master=friend['UserName']
#Fill and complete lists. Get username for master. 

@itchat.msg_register([TEXT])
def text_forward(msg):
    if msg['FromUserName']!=master:
        forwardToMaster(msg, master)
    else:
        respondToMaster(msg, master)

def forwardToMaster(msg, master):
    itchat.send('%s:: %s' % (friendDispName[friendUserName.index(msg['FromUserName'])], msg['Text']), master);
    return

def respondToMaster(msg, master):
#    itchat.send('From master %s: %s' % (friendDispName[friendUserName.index(msg['FromUserName'])], msg['Text']), master);
    arg=re.compile('::::').split(msg['Text'])
    if len(arg)==2:
        itchat.send(arg[1], friendUserName[friendDispName.index(arg[0])])
        itchat.send('Message sent. ', master)
    else:
        itchat.send('Input error!', master)
    return

itchat.run();

#for i in range(len(friendUserName)):
#    print('%s: %s' % (friendUserName[i], friendDispName[i]))
