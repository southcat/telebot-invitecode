# -*- coding:utf-8 -*-

from teelebot import Bot
import os
import json
bot = Bot()
tips = "有问题联系@southcat解决"
def invite_code(message):
    '''
    通过读取usertext.json文件 来对比用户是否获取过，如果没有则从code.txt读取第一行的邀请码发送给用户，并删除这个邀请码。
    邀请码为0时自动发送给管理员。
    '''
    sysl = lentj()   #sysl=剩余数量
    with open(bot.plugin_dir + 'invite_code/usertext.json','r') as f: #打开文件给f
        userjson = json.load(f)                                         #json.load读取f赋值给userjson
    status = bot.sendChatAction(message["chat"]["id"], "typing")        #显示回复状态
    if yanzheng2(message["from"]["id"]) == 0:                           #判断用户是否获取过
        status = bot.sendChatAction(message["chat"]["id"], "typing")    #显示发送状态
        bot.sendMessage(message["chat"]["id"], "您已经获取过了哦", "HTML")#发送提示
        bot.sendMessage(message["chat"]["id"], tips, "HTML")            #发送预设的提示
    else:
        if sysl == 0:                                                   #判断数量是否为0 比较容易理解
            #status = bot.sendMessage(512466300, "邀请码不足", "HTML") #邀请码不足提醒模块 如需开启请取消注释并将512466300修改为你的id
            status = bot.sendMessage(message["chat"]["id"], "邀请码数量不足请等待补充", "HTML")      #发送信息
        else:
            invite_code1 = code()                                                                   #函数赋值
            status = bot.sendChatAction(message["chat"]["id"], "typing")                            #显示发送状态
            bot.sendMessage(message["chat"]["id"], invite_code1, "HTML")                            #发送邀请码
            bot.sendMessage(message["chat"]["id"], tips, "HTML")                                    #发送预设的提示
            userid = message["from"]["id"]                                                          #获取用户id
            userjson[userid] = invite_code1                                                         #写入字典
            with open(bot.plugin_dir + 'invite_code/usertext.json','w') as f1:                      #打开文件
                json.dump(userjson,f1)                                                              #将修改过的字典写入文件


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