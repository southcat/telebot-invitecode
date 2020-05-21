# -*- coding:utf-8 -*-

from teelebot import Bot
import os
bot = Bot()
tips = "有问题联系@southcat解决"
def invite_code(message):
    invite_code1 = code()
    sysl = lentj()   #sysl=剩余数量
    file2 = str(open(bot.plugin_dir + 'invite_code/usertext.txt','a+'))
    file3 = open(bot.plugin_dir + 'invite_code/usertext.txt','a+')
    status = bot.sendChatAction(message["chat"]["id"], "typing")
    if yanzheng(message["from"]["id"]) == 0:
        status = bot.sendChatAction(message["chat"]["id"], "typing")
        bot.sendMessage(message["chat"]["id"], "您已经获取过了哦", "HTML")
        bot.sendMessage(message["chat"]["id"], tips, "HTML")
    else:
        if sysl == 0:
            #status = bot.sendMessage(512466300, "喵帕斯邀请码不足", "HTML")  #数量不足通知模块  如需启动自行修改512466300为你的id并取消注释
            status = bot.sendMessage(message["chat"]["id"], "邀请码数量不足请等待补充", "HTML")
        else:
            status = bot.sendChatAction(message["chat"]["id"], "typing")
            bot.sendMessage(message["chat"]["id"], invite_code1, "HTML")
            bot.sendMessage(message["chat"]["id"], tips, "HTML")
            file3.write(str(message["from"]["id"])+"     "+invite_code1 + "\n")
            file3.close()


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