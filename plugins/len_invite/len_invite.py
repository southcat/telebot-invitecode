import os
import json
def len_invite(bot,message):
    count_mps = lentj(bot=bot)
    with open(bot.plugin_dir + 'invite_code/usertext.json','r') as f: #打开文件给f
        userjson = json.load(f)
    status = bot.sendMessage(message["chat"]["id"], "邀请码剩余:"+str(lentj(bot=bot))+"\n"+"已发放用户："+str(len(userjson)), "HTML")
    if count_mps == 0 :
        status= bot.sendMessage(512466300,"邀请码不足","HTML")

def lentj(bot):
    count = 0
    for index, line in enumerate(open(bot.plugin_dir + 'invite_code/code.txt', 'r')):
        count += 1
    return count