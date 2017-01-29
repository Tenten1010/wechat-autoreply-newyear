import itchat, time, re
from itchat.content import *

@itchat.msg_register([TEXT])
#auto-reply if message contains any words relate to new year
def textReply(msg):
	match = re.search('(春节|新年|新春|过年好|鸡年|大吉|大运|财源)',msg['Text']).group()
	if match:
		itchat.send(('谢谢！你也是😇'),msg['FromUserName'])

#auto-reply all audio message
@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def otherReply(msg):
	itchat.send(('谢谢！!😇'),msg['FromUserName'])

#set hotReload to false if you want login with multiple account
itchat.auto_login(enableCmdQR=2, hotReload=True)
#set debug to true to read error log
itchat.run(debug=False)