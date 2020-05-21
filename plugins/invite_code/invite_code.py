import json
import time

# -*- coding:utf-8 -*-

from teelebot import Bot
import os
bot = Bot()
tips = "有问题联系@southcat解决"
def invite_code(message):
    sysl = lentj()   #sysl=剩余数量
    with open(bot.plugin_dir + 'invite_code/usertext.json','r') as f:
        userjson = json.load(f)
    file2 = str(open(bot.plugin_dir + 'invite_code/usertext.txt','a+'))
    file3 = open(bot.plugin_dir + 'invite_code/usertext.txt','a+')
    status = bot.sendChatAction(message["chat"]["id"], "typing")
    if yanzheng2(message["from"]["id"]) == 0:
        status = bot.sendChatAction(message["chat"]["id"], "typing")
        bot.sendMessage(message["chat"]["id"], "您已经获取过了哦", "HTML")
        bot.sendMessage(message["chat"]["id"], tips, "HTML")
    else:
        if sysl == 0:
            #status = bot.sendMessage(512466300, "喵帕斯邀请码不足", "HTML")  #数量不足通知模块  如需启动自行修改512466300为你的id并取消注释
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

def yanzheng(user_id):   #验证是否领取过验证吗
    file2 = str(open(bot.plugin_dir + 'invite_code/usertext.txt', 'a+'))
    j = 0
    for i in open(bot.plugin_dir + 'invite_code/usertext.txt','r+'):
        if str(user_id) in i:
            j = int(j) + 1
    if j != 0:
        return 0
    else:
        return 1

def lentj():  #验证码剩余数量统计
    count = 0
    for index, line in enumerate(open(bot.plugin_dir + 'invite_code/code.txt', 'r')):
        count += 1
    return count
def yanzheng2(user_id): #采用json数据进行用户校验
    with open(bot.plugin_dir + 'invite_code/usertext.json', 'r') as f:
        userjson = json.load(f)
    if str(user_id) in userjson:
        return 0
    else:
        return 1
