import json
import requests
from wxpy import *       

def reply(text):       #定义调用图灵聊天机器人的函数
    url = 'http://www.tuling123.com/openapi/api'     #调用图灵api
    api_key = '?'     #这个？换成你自己的apikey
    payload={
        "key":api_key,
        "info":text,
        "userid":"?"    #这里填写你在图灵的id
        }
    r = requests.post(url,data=json.dumps(payload))
    result = json.loads(r.content)
    if ('url' in result.keys()):
        return '' + result['text'] + result['url']
    else:
        return '' + result['text']

bot = Bot(cache_path=True)   #initial bot
my_friend = bot.friends()      #找到所有微信好友
print(my_friend)
@bot.register(my_friend)   #在微信机器人中注册微信好友
def message(msg):
    ret = reply(msg.text)    #调用上述函数
    print(msg.sender.name,':',msg.text,'Msg Type:',msg.type)   #打印发送消息的好友，文本信息，信息类型
    return ret
embed()  #堵塞线程


#作为新手的我做的，放在这里纯属是为了记录自己做过什么。
