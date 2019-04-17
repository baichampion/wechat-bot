import json
import requests
from wxpy import *

def reply(text):       #定义调用图灵聊天机器人的函数
    url = 'http://www.tuling123.com/openapi/api'     #调用图灵api
    api_key = '?'
    payload={
        "key":api_key,
        "info":text,
        "userid":"?"
        }
    r = requests.post(url,data=json.dumps(payload))
    result = json.loads(r.content)
    if ('url' in result.keys()):
        return '' + result['text'] + result['url']
    else:
        return '' + result['text']

bot = Bot(cache_path=True)   #initial bot
my_friend = bot.friends()
print(my_friend)
@bot.register(my_friend)   #在微信机器人中注册微信好友
def message(msg):
    ret = reply(msg.text)
    print(msg.sender.name,':',msg.text,'Msg Type:',msg.type)
    return ret
embed()