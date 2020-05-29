from teelebot import Bot
from teelebot.handler import config
import json
import os
config = config()
bot = Bot()
def deluser(message):
    hx = "\n"
    if str(message["from"]["id"]) == config["root"]:
        with open(bot.plugin_dir + "deluser/__init__.py", encoding="utf-8") as f:
            h = f.readline()[1:]
        if len(message["text"]) < len(h):
            status = bot.sendChatAction(message["chat"]["id"], "typing")
            status = bot.sendMessage(message["chat"]["id"], "删除失败，请输入用户id", "HTML")
            return False
        userid = message["text"][len(h) - 1:]
        with open(bot.plugin_dir + 'invite_code/usertext.json', 'r') as f:
            userjson = json.load(f)
        del userjson[userid]
        with open(bot.plugin_dir + 'invite_code/usertext.json', 'w') as f1:
            json.dump(userjson, f1)
        status = bot.sendChatAction(message["chat"]["id"], "typing")
        status = bot.sendMessage(message["chat"]["id"], "删除用户信息成功", "HTML")
    else:
        status = bot.sendChatAction(message["chat"]["id"], "typing")
        status = bot.sendMessage(message["chat"]["id"], "删除失败，您没有权限", "HTML")


