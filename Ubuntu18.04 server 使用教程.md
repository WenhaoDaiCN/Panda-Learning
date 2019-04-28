# Ubuntu18.04 server 使用教程

服务器配置 pandalearning 自动刷分，步骤如下：

* 安装指定版本chrome浏览器
* 配置chromedriver
* 运行pandalearning

测试环境： Ubuntu18.04 server 64bit



使用 pandalearning 二进制文件运行一直失败，尝试多种方法无果，这里使用Python源码能够正确运行。欢迎提供二进制文件运行配置方法~

本方法在安装有 Ubuntu18.04 的服务器端运行成功，服务器端需要配置python环境并安装指定版本的 Chrome浏览器。

## 运行程序

### 下载源码

```
mkdir ~/pandalearning && cd ~/pandalearning
sudo apt update
sudo apt install -y wget xvfb  
wget https://github.com/Alivon/Panda-Learning/archive/master.zip  # 下载源码
unzip -q -d master.zip   # 解压
mkdir panda_code/ && cp -r Panda-Learning-master/'Source Packages'/* panda_code # 将所需代码移动到指定文件夹
```

### 安装指定版本Chrome 浏览器

```
cd ~/pandalearning
wget https://github.com/Alivon/Panda-Learning/raw/linux/pandalearning-linux/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

### 配置webdriver

运行下面的命令获取正确版本的webdriver, 需要确保 webdriver 与源码pandalearning.py在同一目录下面，或者将webdriver配置到系统路径也可。

```
cd ~/pandalearning
wget https://github.com/Alivon/Panda-Learning/raw/linux/pandalearning-linux/pandalearning_linux.tar.gz
tar -zxvf pandalearning_linux.tar.gz -C  ~/pandalearning/panda_code/ # 解压webdriver到源码文件夹

```

### 配置 Python 环境并运行程序

源码运行的python环境为 python3 + selenium ，只需安装 selenium 即可

```
pip install selenium
pip install requests
```

运行程序

```
cd ~/pandalearning/panda_code/   # 切换到源码文件夹
python pandalearning.py
```

运行结果如下：

![ubuntu](img_floder/ubuntu-run.png)



