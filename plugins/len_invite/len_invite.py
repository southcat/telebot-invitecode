from teelebot import Bot
import os
from .handler import config

config = config()
bot = Bot()
def len_invite(message):
    count_mps = lentj()
    status = bot.sendMessage(message["chat"]["id"], "喵帕斯剩余:"+str(lentj()), "HTML")
    if count_mps == 0 :
        status= bot.sendMessage(config["root"],"喵帕斯邀请码不足","HTML")

def lentj():
    count = 0
    for index, line in enumerate(open(bot.plugin_dir + 'invite_code/code.txt', 'r')):
        count += 1
    return count