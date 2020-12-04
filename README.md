## 框架更新了我还没同步过来 大的结构会有变化 三天之内全部修改完 我说的  耶稣也拦不住我(更新完了)

## 新手安装教程请看
https://southcat.net/2526/

## 插件必看
喵帕斯的已经没了 自动补码是喵帕斯的  需要dlercloud的请把updatacode目录下的dlercloud.py文件名修改为updatacode.py覆盖掉源文件，需要其他的自己修改或是可以找我
我有时间就做一个 马上放假了时间多的是

## 第一次开发有问题及时反馈
email:admin@southcat.net

博客:[南猫](https://southcat.net)

基于[teelebot](https://github.com/plutobell/teelebot)开源项目开发。

## 增加功能

1.邀请码自动发码模块 并且限制领取数量（邀请码添加在invite_code目录下的code.txt 一行一个）

2.邀请码数量统计，如果邀请码用完自动给管理员发消息（需自行修改len_invite.py里面的发送id）

3.补码模块已经开发 指令`/add_code邀请码`   请注意一行一码因为太菜要求比较严格 可能效果不是很理想，请等我再去学两天python再回来改

4.删除用户信息模块，删除后用户可以再次获取邀请码指令`/del用户id`目前只能删除单个用户

5.updatacode模块，目前仅支持从喵帕斯进行获取，会自动抓取邀请码页面前两页的邀请码，并和之前的数据进行对比，然后写入code，后续会支持更多网站
理论上所有和喵帕斯同模板的都可以使用，请在updatacode/updatacode.py 文件夹内填入你的账号密码

6.很遗憾喵关门了 在plguins/updatacode文件夹下更新了dlercloud的自动更新模块，需要使用的话备份原文件，将文件名修改为updatacode.py即可，理论上喵帕斯的补码支持所有同模板的网站只需要更改里面的网站即可，接下来会针对所有有邀请码模块的网站开发补码模块，或是你们也可以从邮箱或是tg发给我网站，我尽量进行适配（放假闲的）
## 开发计划
1.增加管理员添加邀请码模块

2.多类邀请码模块支持

3.代码优化，目前存在大量多余的代码

4.添加白名单，白名单用户支持无限获取

环境要求
Python版本
teelebot 只支持 Python3.x，不支持Python2.x。

本项目在 Python 3.5 及以上版本测试通过。

安装
pip install teelebot
升级
pip install teelebot --upgrade
使用
一行命令启动 (Polling Mode)
teelebot -c/--config <config file path> -k/--key <bot key> -r/--root <your user id>
此命令会自动生成在Polling模式下适用的配置文件，但仍需手动配置插件路径。

一、运行模式
teelebot 支持以 Webhook 模式和 Polling 模式运行。生产环境推荐使用 Webhook 模式，而 Polling 则仅用于开发环境。

1、Webhook 模式
要以 Webhook 模式运行，请将配置文件字段 webhook 设置为 True ，此模式涉及的配置文件字段如下：

[config]
webhook=True
self_signed=False
cert_key=your private cert path
cert_pub=your public cert path
server_address=your server ip address or domain
server_port=your server port
local_address=webhook local address
local_port=webhook local port
self_signed 用于设置是否使用自签名证书，而 cert_key 和 cert_pub 则是你的证书路径(绝对路径)，server_address 为你的服务器公网IP, server_port 为服务器的端口(目前 telegram 官方仅支持 443, 80, 88, 8443)，local_address 为Webhook 本地监听地址， local_port 为 Webhook 本地运行的端口。

推荐搭配 nginx 使用，自签名证书生成请参考：Generating a self-signed certificate pair (PEM)

2、Polling 模式
要以 Polling 模式运行，只需要保证配置文件 webhook 字段为 False 即可。此模式最基本的配置文件如下:

[config]
key=bot key
pool_size=40
webhook=False
root_id=your user id
debug=False
plugin_dir=your plugin dir
二、运行
任意路径打开终端，输入以下命令：

对于使用程序配置文件默认路径的：

输入teelebot 回车,正常情况下你应该能看见屏幕提示机器人开始运行。

对于命令行手动指定配置文件路径的：

输入teelebot -c/--config <configure file path> 回车,正常情况下你应该能看见屏幕提示机器人开始运行。(更多指令请通过 -h/--help 查看)

可配合supervisor使用。

三、配置文件
完整的配置文件如下所示:

[config]
key=bot key
plugin_dir=your plugin dir
pool_size=40 //the thread pool size, default 40, range(1, 101)
webhook=False
self_signed=False //Optional while webhook is False
cert_key=your private cert path //Optional while webhook is False
cert_pub=your public cert path //Optional while webhook is False
server_ip=your server ip address //Optional while webhook is False
server_port=your server port //Optional while webhook is False
local_address=webhook local address //Optional while webhook is False
local_port=webhook local port //Optional while webhook is False
root_id=your user id
debug=False
drop_pending_updates=False
local_api_server=local api server address //[Optional]
在 1.13.0 及以上版本，支持自动生成配置文件。（默认为Polling模式）

1.在命令行未指定配置文件路径的情况下，会在默认配置文件路径下不存在配置文件时自动生成配置文件 config.cfg。

在Linux下，会自动在用户目录下创建文件夹 .teelebot ，并生成配置文件 config.cfg

在Windows下，则会在 C:\Users\<username> 目录下创建文件夹 .teelebot ，并生成配置文件 config.cfg

2.指定配置文件

Linux 和 Windows 都可在命令行通过参数手动指定配置文件路径，命令格式：

teelebot -c/--config <configure file path>
路径必须为绝对路径，此情况下也会在指定路径上不存在配置文件时自动生成配置文件 ，配置文件命名由指定的路径决定。

Tip: 自动生成的配置文件未设置这几个字段值：key、root_id、plugin_dir，key 和 root_id 为必须，但我们仍然可以通过命令行设置他们：

teelebot -c/--config <config file path> -k/--key <bot key> -r/--root <your user id>
使用以上命令会以Polling模式运行框架，而无需困扰于处理配置文件。

之后请手动设置 plugin_dir 。

插件开发指南 (以 Hello 插件为例) BETA 0.8
一、插件结构
一个完整的 teelebot 插件应当呈现为一个文件夹，即一个Python包，以 Hello 插件为例，最基本的目录结构如下：

Hello/
  ./__init__.py
  ./Hello.py
  ./Hello_screenshot.png
  ./readme.md
  ./requirement.txt
二、规则
命名
在构建teelebot插件中应当遵守的规则是：每个插件目录下应当存在一个与插件同名的.py 文件，比如插件 Hello 中的 Hello.py 文件，并且此文件中必须存在作为插件入口的同名函数，以插件 Hello 为例：

#file Hello/Hello.py

# -*- coding:utf-8 -*-

def Hello(bot, message):
    pass
函数 Hello() 即为插件的入口函数，参数 bot 为Bot接口库实例化对象，参数 message 用于接收消息数据。

资源路径
若要打开某个插件目录下的文件资源，需要使用的路径应当遵循以下的格式：

bot.path_converter(bot.plugin_dir + "<plugin dir name>/<resource address>")
方法 path_converter 根据操作系统转换路径格式。

三、自定义触发指令
插件指令
插件的触发指令可不同于插件名，允许自定义。以插件 Hello 为例，触发指令为 /helloworld 而不是 Hello。

修改插件目录下的 __init__.py 文件设置触发指令：

#file Hello/__init__.py

#/helloworld
#Hello World插件例子
第一行为触发指令，默认以 / 作为前缀；第二行为插件简介。

不用作插件的特殊情况
通常情况下，位于 plugins 目录下的所有包都将被识别为插件并自动加载到 teelebot 中。但在某些情况下，存在并不用作插件而只是多个插件共用包的情况，若想该包不被 teelebot 加载，请将触发指令设置为 ~~ 。以 tools 共用包为例， __init__.py 文件内容如下：

#fille tools/__init__.py

#~~
#tools 包的简介
建议用作插件的包名遵守 Pascal命名法，即每个单词的首字母大写；而不用做插件的包名使用全小写的包名，每个单词之间以_ 分隔。以区分 插件包 和 非插件包 ：

- plugins
  - Menu    #插件包
  - tools   #非插件包
四、插件模板创建工具
在 v1.9.20_dev 及以上版本，可以通过命令行指令一键创建插件模板。

teelebot -p/--plugin <plugin name>
该指令会使用框架配置文件(config.cfg)中的插件路径作为所创建插件模板的存放路径。

五、周期性任务
在 v1.11.1 及以上版本，可以创建周期性任务，功能类似循环定时器。

可获得的方法：

schedule.add : 添加任务
schedule.delete : 移除任务
schedule.find : 查找任务
schedule.clear : 清空任务池
schedule.status : 查看任务池状态
例：

ok, uid = bot.schedule.add(gap, event, (bot, ))
ok, uid = bot.schedule.delete(uid)
ok, uid = bot.schedule.find(uid)
ok, uid = bot.schedule.clear()
ok, uid = bot.schedule.status()
周期性任务池的大小为全局线程池的三分之一 ，线程池大小则可通过配置文件指定。
1.克隆或点击下载本项目到本地，保证本机安装有`Python3.x`版本和包`requests` ；



2.`config.cfg` 配置文件

配置文件格式:

```python
[config]
key=your key
pool_size=40 //the thread pool size, default 40, range(1, 101)
webhook=False
cert_pub=your public certificate dir //Optional while webhook is False
server_ip=your server ip address //Optional while webhook is False
server_port=your server port //Optional while webhook is False
local_address=webhook local address //Optional while webhook is False
local_port=webhook local port //Optional while webhook is False
root=your user id
debug=False
timeout=60
plugin_dir=your plugin dir   //[Optional]
```

* Linux

在 `/root` 目录下创建文件夹 `.teelebot` ,并在其内新建配置文件 `config.cfg` ,按照上面的格式填写配置文件

* Windows

在 `C:\Users\<username>`  目录下创建文件夹 `.teelebot` ,并在其内新建配置文件 `config.cfg` ,按照上面的格式填写配置文件

* 指定配置文件

Linux 和 Windows 都可在命令行通过参数手动指定配置文件路径，命令格式：

```
python -m teelebot -c/-C <configure file path>
```

路径必须为绝对路径。



3.运行

终端下进入teelebot文件夹所在目录。

* 对于使用程序配置文件默认路径的：

  输入`python -m teelebot` 回车,正常情况下你应该能看见屏幕提示机器人开始运行。

* 对于命令行手动指定配置文件路径的：

  输入`python -m teelebot -c/-C <configure file path>` 回车,正常情况下你应该能看见屏幕提示机器人开始运行。



#### 三、Pip安装运行

##### 安装 #####

* 确保本机Python环境拥有pip包管理工具。

* 在本项目Releases页面下载包文件。

* 本机命令行进入包文件所在目录，执行：

  ```
  pip install <teelebot package file name>
  
  or
  
  pip3 install <teelebot package file name>
  ```

由于API未封装完毕，暂未上传至 `PyPI` ,故不能在线安装，望谅解。

##### 运行 #####

任意路径打开终端，输入以下命令：

- 对于使用程序配置文件默认路径的：

  输入`teelebot` 回车,正常情况下你应该能看见屏幕提示机器人开始运行。

- 对于命令行手动指定配置文件路径的：

  输入`teelebot -c/-C <configure file path>` 回车,正常情况下你应该能看见屏幕提示机器人开始运行。



可配合`supervisor`使用。





## 插件开发指南 (以 Hello 插件为例) BETA 0.6

#### 一、插件结构

一个完整的 `teelebot` 插件应当呈现为一个文件夹，即一个Python包，以 `Hello` 插件为例，最基本的目录结构如下：

```Python
Hello/
  ./__init__.py
  ./Hello.py
  ./Hello_screenshot.png
  ./readme.md
```

#### 二、规则

##### 命名

在构建teelebot插件中应当遵守的规则是：每个插件目录下应当存在一个与插件同名的`.py` 文件，比如插件 `Hello ` 中的 `Hello.py` 文件，并且此文件中必须存在作为插件入口的同名函数，以插件 `Hello` 为例：

```python
#file Hello/Hello.py

# -*- coding:utf-8 -*-

def Hello(bot, message):
    pass
```

函数 `Hello()` 即为插件的入口函数，参数 `bot` 为Bot接口库实例化对象，参数 `message` 用于接收消息数据。





##### 资源路径

若要打开某个插件目录下的文件资源，需要使用的路径应当遵循以下的格式：

```python
bot.plugin_dir + "<plugin dir name>/<resource address>"
```

#### 三、自定义触发指令

##### 插件指令

插件的触发指令可不同于插件名，允许自定义。以插件 `Hello` 为例，触发指令为 `/helloworld` 而不是 `Hello`。

修改插件目录下的 `__init__.py` 文件设置触发指令：

```python
#file Hello/__init__.py

#/helloworld
#Hello World插件例子
```

第一行为触发指令，默认以 `/`  作为前缀；第二行为插件简介。



##### 不用作插件的特殊情况

通常情况下，位于 `plugins` 目录下的所有包都将被识别为插件并自动加载到 `teelebot` 中。但在某些情况下，存在并不用作插件而只是多个插件共用包的情况，若想该包不被 `teelebot` 加载，请将触发指令设置为 `~~`  。以 `tools` 共用包为例， `__init__.py` 文件内容如下：

```python
#fille tools/__init__.py

#~~
#tools 包的简介
```

建议用作插件的包名遵守 `Pascal命名法`，即每个单词的首字母大写；而不用做插件的包名使用全小写的包名，每个单词之间以`_`  分隔。以区分 `插件包` 和 `非插件包` ：

```python
- plugins
  - Menu    #插件包
  - tools   #非插件包
```
