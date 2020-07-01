import requests
# import re
import json
from bs4 import BeautifulSoup

global codelist1
codelist1 = []
url = ["https://xn--i2ru8q2qg.com/user/invite", "https://xn--i2ru8q2qg.com/user/invite?page=2"]

chongfu = 0


def updatacode(bot,message):
    if str(message["from"]["id"]) == bot.config["root"]:
        for abc in url:
            a = shuaxin(bot,abc)
            if a == 1:
                status = bot.sendChatAction(message["chat"]["id"], "typing")
                bot.sendMessage(message["chat"]["id"], "更新失败,cookie失效或是遇到防火墙", "HTML")
            else:
                status = bot.sendChatAction(message["chat"]["id"], "typing")
                bot.sendMessage(message["chat"]["id"], "更新成功", "HTML")
                file = open(bot.plugin_dir + 'invite_code/code.txt', 'w+')
                for code1 in codelist1:
                    file.write(str(code1))
                codelist1.clear()
    else:
        status = bot.sendChatAction(message["chat"]["id"], "typing")
        bot.sendMessage(message["chat"]["id"], "您没有权限哦", "HTML")
    status = bot.sendChatAction(message["chat"]["id"], "typing")
    bot.sendMessage(message["chat"]["id"], "当前剩余数量：" + str(lentj(bot=bot)), "HTML")


def shuaxin(bot,urls):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    data = {
        "email": "",
        "passwd": "",
    }
    # 通过session模拟登录，每次请求带着session
    url1 = 'https://xn--i2ru8q2qg.com/auth/login'
    sess = requests.Session()
    f = sess.post(url1, data=data, headers=header)
    # print(f.text)
    e = sess.get(urls, headers=header)
    html = e.text
    soup = BeautifulSoup(html, 'lxml')
    codelist = soup.find_all('a', target='_blank')
    # print(codelist)
    code = []
    cloudflare = 'https://xn--i2ru8q2qg.comhttps://www.cloudflare.com/5xx-error-landing?utm_source=iuam'
    for i in codelist:
        code.append(i.get('href'))
    if len(code) <= 1:
        return 1
    else:
        n = '\n'
        http = 'https://xn--i2ru8q2qg.com'
        with open(bot.plugin_dir + 'invite_code/usertext.json') as f1:
            userjson = json.load(f1)
        for c in code:
            if http + c + n in userjson.values() or http + c + n in codelist1:
                # print(c + "存在")
                pass
            else:
                codelist1.append(http + c + n)
        return 0


def lentj(bot):
    count = 0
    for index, line in enumerate(open(bot.plugin_dir + 'invite_code/code.txt', 'r')):
        count += 1
    return count
