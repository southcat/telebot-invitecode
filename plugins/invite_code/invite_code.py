# -*- coding:utf-8 -*-

from teelebot import Bot
import os
import json
bot = Bot()
tips = "有问题联系@southcat解决"
def invite_code(message):
    sysl = lentj()   #sysl=剩余数量
    with open(bot.plugin_dir + 'invite_code/usertext.json','r') as f:
        userjson = json.load(f)
    status = bot.sendChatAction(message["chat"]["id"], "typing")
    if yanzheng2(message["from"]["id"]) == 0:
        status = bot.sendChatAction(message["chat"]["id"], "typing")
        bot.sendMessage(message["chat"]["id"], "您已经获取过了哦", "HTML")
        bot.sendMessage(message["chat"]["id"], tips, "HTML")
    else:
        if sysl == 0:
            #status = bot.sendMessage(512466300, "邀请码不足", "HTML") #邀请码不足提醒模块 如需开启请取消注释并将512466300修改为你的id
            status = bot.sendMessage(message["chat"]["id"], "邀请码数量不足请等待补充", "HTML")      
        else:
            invite_code1 = code()
            status = bot.sendChatAction(message["chat"]["id"], "typing")
            bot.sendMessage(message["chat"]["id"], invite_code1, "HTML")
            bot.sendMessage(message["chat"]["id"], tips, "HTML")
            userid = message["from"]["id"]
            userjson[userid] = invite_code1
            with open(bot.plugin_dir + 'invite_code/usertext.json','w') as f1:
                json.dump(userjson,f1)


def code():   #获取验证吗
    file = open(bot.plugin_dir + 'invite_code/code.txt','r')
    a = file.readline()
    lines = (i for i in open(bot.plugin_dir + 'invite_code/code.txt', 'r') if a not in i)
    f = open(bot.plugin_dir + 'invite_code/test_new.txt', 'w', encoding="utf-8")
    f.writelines(lines)
    f.close()
    os.rename(bot.plugin_dir + 'invite_code/code.txt', bot.plugin_dir + 'invite_code/test.bak')
    os.rename(bot.plugin_dir + 'invite_code/test_new.txt', bot.plugin_dir + 'invite_code/code.txt')
    os.remove(bot.plugin_dir + 'invite_code/test.bak')
    file.close()
    return a

def lentj():  #验证码剩余数量统计
    count = 0
    for index, line in enumerate(open(bot.plugin_dir + 'invite_code/code.txt', 'r')):
        count += 1
    return count

def yanzheng2(user_id):
    with open(bot.plugin_dir + 'invite_code/usertext.json', 'r') as f:
        userjson = json.load(f)
    if str(user_id) in userjson.keys():
        return 0
    else:
        return 1