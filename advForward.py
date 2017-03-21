import itchat
from itchat.content import *

masterAlias='jyzhang__'
master=''
#Set the master account according to wechatID 

itchat.auto_login(enableCmdQR=2, hotReload=True)
#Login

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

    if friend['Alias']==masterAlias:
        master=friend['UserName']
#Fill and complete lists. Get username for master. 

@itchat.msg_register([TEXT])
def text_forward(msg):
    if msg['FromUserName']!=master
        itchat.send('%s: %s' % (friendDispName(friendUserName.index(msg['FromUserName'])), msg['Text']), master);

itchat.run();

#for i in range(len(friendUserName)):
#    print('%s: %s' % (friendUserName[i], friendDispName[i]))
