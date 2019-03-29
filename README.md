## 欢迎使用Panda-Learning 中文名即熊猫学习



熊猫学习Panda-Learning是一个辅助学习强国的程序,帮助挤不出时间，却仍然需要学习的积极分子，熊猫学习强国(xuexiqiangguo)

觉得好用请点击右上star一下。

使用异常或者有更好的建议请联系邮箱 mypandalearning@gmail.com



## v2.2更新，各系统均已已上传

# 文档龟速更新中，源码以上传，请大家指正及贡献。





## 程序特性

**支持WIN7和WIN10，mac os ，linux，vps以及Raspberry Pi**  树莓派好像反馈不能运行，有树莓派的可以帮忙打包一下

**支持多用户同时使用，**

**支持本地保存钉钉账号密码登陆，**

**支持后台勿打扰学习，**

**支持多线程学习(可关闭)，缩减学习时间。**

**解决重复文章不加分问题，自动检查分数重复学习**



## 使用方法

2.0以上版本 使用方法：首次登陆需要输入并保存用户标记(标记用于区分本地用户以及保存学习历史纪录)，然后根据需要选择扫描或者钉钉账号密码登陆，若保存了账户密码，以后每次只需输入用户标记即可自动学习。

- 高级用法，终端运行` pandalearning ` 然后输入参数各参数用空格分开，

  - 第一个参数为用户标记，

  - 第二个参数为 ` hidden ` 或 ` show `，分别表示隐藏浏览器后台运行和前台显示运行

  - 第三个参数为 ` single  ` 或 ` multithread `, 分别表示仅用单线程和多线程学习。

  - 第四个参数为 ` num ` 为一个数字，表示学习完成后多少秒自动关机。  

    win平台示例

    ​	user1 为已经保存了顶顶账户的用户标记

    ​	` ./pandalearning.exe user1 ` 表示自动开启user1 学习

    ​	` ./pandalearning.exe user1 show single` 表示前台显示且单线程开启user1 学习

    ​	` ./pandalearning.exe user1 hidden multithread 300` 表示后台多线程开启user1 学习，学习完毕300秒关机

    其他平台同理，可以放在vps和树莓派了

#### Windows

- 请解压后点击 `pandalearn`ing 来启动程序。
- 开启后根据提示中输入用户名可以输入任何***`英文/中文/数字`***组成的用户名，作用是保存学习历史纪录以及多开程序区分用户，防止学习重复文章视频，
- 打开的chrome浏览器窗口中的程序自动完成“学习”，你可以用这台电脑做其他事情，但不能 最小化 或 关闭 学习窗口。
- 第一次使用后程序会自动生成 `user`文件夹，里面包含你的学习历史纪录，当学习文章篇数和视频数出现不加分情况，多半是你变更了用户名，解决办法为进入`user`文件夹下你`用户名`文件夹下的`a_log`和`v_log`文件，修改上面的数字，例如是0的时候可以改成20，12的时候改为30，就是根据上面的数字增加20~30，修改后仍为一个数样式如下`36`

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





## 更新说明
### 更新记得同步你的user文件信息，不然可能会学习重复文章视频
- v 2.2(preview) 
  - 修复逻辑问题，更加稳定好用。
- v 2.1(preview) 
  - 针对学习强国更新，紧急修复不能使用问题
- v 2.0(preview) 
  - 学满30位置，增加自动关机，保存账号，支持开关多线程及headless
- v 1.8
  - 增加账号登陆，可以卸载手机app了。
  - 改为后台学习，登陆后自动关闭浏览器。
  - 不保存用户信息，防止不法分子商用，需要用户每天登陆
- v 1.6
  - 修复win7 32位系统不能使用问题
  - 增加mac os系统支持，请仔细阅读使用说明。
- v 1.5
  - 加入活跃时间判断，优化用户自行学完文章篇书却没有学习时长等极端情况。
  - 开放python源码，可以自行在各平台使用，请勿商用，转发请注明出处





## **下载地址**

### [Windows v2.2 完整包](https://github.com/Alivon/Panda-Learning/raw/master/Panda_learning-32.7z) 57.5MB首次使用推荐下载

### [Windows v2.2 更新包](https://github.com/Alivon/Panda-Learning/raw/master/pandalearning.exe) 5.94MB下载覆盖即可使用



------

### [Macos v2.2](https://github.com/Alivon/Panda-Learning/raw/mac/pandalearning-mac/pandalearning_macos.zip) 12.9MB

###### [macos浏览器](https://github.com/Alivon/Panda-Learning/raw/mac/pandalearning-mac/googlechrome.dmg)

------



### [linux v2.2](https://github.com/Alivon/Panda-Learning/raw/linux/pandalearning-linux/pandalearning_linux.tar.gz) 11.2MB

###### [linux浏览器下载rpm（适用于 Fedora/openSUSE)](https://github.com/Alivon/Panda-Learning/blob/linux/pandalearning-linux/google-chrome-stable_current_x86_64.rpm?raw=true)

###### [ linux浏览器下载deb（适用于 Debian/Ubuntu）](https://github.com/Alivon/Panda-Learning/blob/linux/pandalearning-linux/google-chrome-stable_current_amd64.deb?raw=true)



#### windows旧版本

###### 因为学习强国规则更新，已删除








## win下报错解决办法

windous有可能提示`无法定位程序输入点ucrtbase.terminate于动态链接库api-ms-win-crt-runtime-|1-1-0.dll`等缺失dll文件的问题而无法使用，尝试安装`Visual C++ Redistributable for Visual Studio 2015`该程序包含在`不能运行时安装`的目录中

根据你的操作系统32/64选择x86/x64版本vc_redist安装，即可解决不能使用问题。

下载地址：

[vc_redist.x64.exe](https://github.com/Alivon/Panda-Learning/raw/master/windows%E4%B8%8D%E8%83%BD%E8%BF%90%E8%A1%8C%E6%97%B6%E5%AE%89%E8%A3%85/vc_redist.x64.exe)

[vc_redist.x86.exe](https://github.com/Alivon/Panda-Learning/raw/master/windows%E4%B8%8D%E8%83%BD%E8%BF%90%E8%A1%8C%E6%97%B6%E5%AE%89%E8%A3%85/vc_redist.x86.exe)



源码

[2.2源码](<https://github.com/Alivon/Panda-Learning/tree/master/Source%20Packages>)