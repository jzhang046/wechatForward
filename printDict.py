import itchat
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
	print(msg['FromUserName'])
	itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

itchat.auto_login(enableCmdQR=2, hotReload=True)

friendList = itchat.get_friends(update=True)[1:]
#print(friendList)
for friend in friendList:
	#print(friend['UserName'])
	#print(friend)
	#print(friend['NickName'])
	#print('end')
	if friend['Alias']=='luzhen94':
		print(friend)
        print(friend['DisplayName'])
#itchat.run()
