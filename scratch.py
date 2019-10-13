import itchat,time
from itchat.content import *


chat = itchat.new_instance()
chat.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')

@chat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    chat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
                msg['FromUserName'])
    return '%s received' % msg['Type']

@chat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))
    print(msg.user)
    return msg.text


chat.run()
