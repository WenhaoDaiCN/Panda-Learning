## 欢迎使用Panda-Learning 中文名即熊猫学习

熊猫学习Panda-Learning是一个辅助学习强国的程序,帮助挤不出时间，却仍然需要学习的积极分子，熊猫学习强国(xuexiqiangguo)

觉得好用请点击右上star一下。

使用异常或者有更好的建议请联系邮箱 mypandalearning@gmail.com

## 跟新说明
### 更新记得同步你的user文件信息，不然会学习重复文章视频

- 2019.03.16
  - 增加账号登陆，可以卸载手机app了。
  - 改为后台学习，登陆后自动关闭浏览器。
  - 不保存用户信息，防止不法分子商用，需要用户每天登陆
- 2019.03.15 
  - 修复win7 32位系统不能使用问题
  - 增加mac os系统支持，请仔细阅读使用说明。
- 2019.03.14 
  - 加入活跃时间判断，优化用户自行学完文章篇书却没有学习时长等极端情况。
  - 开放python源码，可以自行在各平台使用，请勿商用，转发请注明出处



[源码下载](https://raw.githubusercontent.com/Alivon/Panda-Learning/master/pandalearn.py)




## **下载地址**

[windows版本](https://github.com/Alivon/Panda-Learning/archive/master.zip)

[macos版本](https://github.com/Alivon/Panda-Learning/raw/mac/pandalearning-mac/pandalearning-mac.zip)

[macos浏览器](https://github.com/Alivon/Panda-Learning/raw/mac/pandalearning-mac/googlechrome.dmg)（10.10以上版本）

[linux桌面版](https://github.com/Alivon/Panda-Learning/blob/linux/pandalearning-linux/pandalearning-linux.zip?raw=true)  linux需要安装chrome浏览器下载链接

[linux浏览器下载rpm（适用于 Fedora/openSUSE)](https://github.com/Alivon/Panda-Learning/blob/linux/pandalearning-linux/google-chrome-stable_current_x86_64.rpm?raw=true)

[ linux浏览器下载deb（适用于 Debian/Ubuntu）](https://github.com/Alivon/Panda-Learning/blob/linux/pandalearning-linux/google-chrome-stable_current_amd64.deb?raw=true)

**关于下载缓慢问题可以尝试用迅雷等工具下载**

## 程序特性

支持WIN7和WIN10，mac os ，linux操作系统

支持多用户同时使用，

支持钉钉账号密码登陆

多线程学习，大大缩减学习时间，活跃时间学满只需25min

解决重复文章不加分问题，正确使用每天都能学满31分



## 使用方法

#### Windows

- 请解压后点击 `pandalearn` 来启动程序。
- 开启后根据提示中输入用户名可以输入任何***英文/中文/数字***组成的用户名，作用是保存学习历史纪录以及多开程序区分用户，防止学习重复文章视频，每次开启程序需要输入你的用户名读取记录以便学满31分。
- 第一次登陆需要扫描二维码登陆学习强国，再次使用6小时之内会免登陆。
- 打开的chrome浏览器窗口中的程序自动完成“学习”，你可以用这台电脑做其他事情，但不能 最小化 或 关闭 学习窗口。
- 第一次使用后程序会自动生成 `user`文件夹，里面包含你的学习历史纪录，当学习文章篇数和视频数出现不加分情况，多半是你变更了用户名，解决办法为进入`user`文件夹下你`用户名`文件夹下的`log.txt`文件，修改上面的数字，例如是0的时候可以改成20，12的时候改为30，就是根据上面的数字增加20~30，修改后仍为一个数样式如下`36`

#### Mac

- mac os需要先安装chrome浏览器

  浏览器下载地址 [官网](https://www.google.com/intl/zh-CN_ALL/chrome/)   [镜像](https://github.com/Alivon/Panda-Learning/raw/mac/pandalearning-mac/googlechrome.dmg)(不能翻墙的下载)

- 直接双击程序会出错！！

- 解压文件，用终端进入该位置  `yournameMac:pandalearning-mac yourname$`

- 输入 ` ./pandalearn`  执行程序

- 其他同windows



#### Linux

- 必须先安装chrome浏览器
- 双击执行
- 其他同windows






## win下报错解决办法

windous有可能提示`无法定位程序输入点ucrtbase.terminate于动态链接库api-ms-win-crt-runtime-|1-1-0.dll`等缺失dll文件的问题而无法使用，尝试安装`Visual C++ Redistributable for Visual Studio 2015`该程序包含在`不能运行时安装`的目录中

根据你的操作系统32/64选择x86/x64版本vc_redist安装，即可解决不能使用问题。



