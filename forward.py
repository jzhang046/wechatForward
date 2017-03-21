import itchat
from itchat.content import *


def searchName(value, searchField, returnField, friendList):
	for friend in friendList:
		if friend[searchField]==value:
			return friend[returnField]

itchat.auto_login(enableCmdQR=2, hotReload=True)

friendList = itchat.get_friends(update=True)[1:]

masterAlias = 'jyzhang__'
master = searchName(masterAlias, 'Alias', 'UserName', friendList)

@itchat.msg_register([TEXT])
def text_forward(msg):
	itchat.send('%s: %s' % (searchName(msg['FromUserName'], 'UserName', 'NickName', friendList), msg['Text']), master);


def searchNickname(username, friendList):
	for friend in friendList:
		if friend['UserName']==username:
			return friend['NickName']

def searchUsername(nickname, friendList):
	for friend in friendList:
		if friend['NickName']==nickname:
			return friend['UserName']

itchat.run()
