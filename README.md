## 第一次开发有问题及时反馈
email:admin@southcat.net

博客:[南猫](https://southcat.net)

基于[telebot](https://github.com/plutobell/teelebot)开源项目开发。

## 增加功能

1.邀请码自动发码模块 并且限制领取数量（邀请码添加在invite_code目录下的code.txt 一行一个）

2.邀请码数量统计，如果邀请码用完自动给管理员发消息（需自行修改len_invite.py里面的发送id）

3.补码模块已经开发 指令`/add_code邀请码`   请注意一行一码因为太菜要求比较严格 可能效果不是很理想，请等我再去学两天python再回来改

4.删除用户信息模块，删除后用户可以再次获取邀请码指令`/del用户id`目前只能删除单个用户

5.updatacode模块，目前仅支持从喵帕斯进行获取，会自动抓取邀请码页面前两页的邀请码，并和之前的数据进行对比，然后写入code，后续会支持更多网站
理论上所有和喵帕斯同模板的都可以使用，请在updatacode/updatacode.py 文件夹内填入你的账号密码
## 开发计划
1.增加管理员添加邀请码模块

2.多类邀请码模块支持

3.代码优化，目前存在大量多余的代码

4.添加白名单，白名单用户支持无限获取

## 环境要求 ##

### Python版本

teelebot 只支持 Python3.x，不支持Python2.x。





## 使用 ##

#### 一、源码运行 ####

1.克隆或点击下载本项目到本地，保证本机安装有`Python3.x`版本和包`requests`（删除了多余模块不需要了）；



2.`config.cfg` 配置文件

配置文件格式:

```python
[config]
key=your key
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



#### 二、Pip安装运行

##### 安装 #####

* 确保本机Python环境拥有pip包管理工具。

* 在本项目Releases页面下载包文件。

* 本机命令行进入包文件所在目录，执行：

  ```
  pip install <teelebot package file name>
  
  or
  
  pip3 install <teelebot package file name>
  ```

由于API未封装完毕，暂未上传至 `PyPI` ,故不能在线安装，忘谅解。

##### 运行 #####

任意路径打开终端，输入以下命令：

- 对于使用程序配置文件默认路径的：

  输入`teelebot` 回车,正常情况下你应该能看见屏幕提示机器人开始运行。

- 对于命令行手动指定配置文件路径的：

  输入`teelebot -c/-C <configure file path>` 回车,正常情况下你应该能看见屏幕提示机器人开始运行。





可配合`supervisor`使用。
