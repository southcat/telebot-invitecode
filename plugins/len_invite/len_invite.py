from teelebot import Bot
import os
bot = Bot()
def len_invite(message):
    count_mps = lentj()
    status = bot.sendMessage(message["chat"]["id"], "邀请码剩余:"+str(lentj()), "HTML")
    if count_mps == 0 :
        status= bot.sendMessage(512466300,"邀请码不足","HTML")

def lentj():
    count = 0
    for index, line in enumerate(open(bot.plugin_dir + 'invite_code/code.txt', 'r')):
        count += 1
    return count