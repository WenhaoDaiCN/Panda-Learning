Fedora/openSUSE快速安装Chrome和Chromedriver

 `cp google-chrome.repo /etc/yum.repos.d/`

 `dnf install google-chrome-stable`

 `dnf install chromedriver`

此方法既快速又可避免缺少依赖造成的安装失败

注意：chromium ≠ chrome
试图安装使用chromium替代chrome的同学 可能会无法学习

Fedora默认将chrome安装在
/opt/google/chrome/
默认将chromedriver安装在
/usr/lib64/chromium-browser/

源码需修改/pdlearn/mydriver.py

修改13、14行

```python
if os.path.exists("./chrome/chrome.exe"):
	self.options.binary_location = "./chrome/chrome.exe"
```

改为

```python
if os.path.exists("/opt/google/chrome/chrome"):
	self.options.binary_location = "/opt/google/chrome/chrome"
```

修改27、28行

```python
if os.path.exists("./chrome/chromedriver.exe"):
	self.driver = self.webdriver.Chrome(executable_path="./chrome/chromedriver.exe", chrome_options=self.options)
```

改为

```python
if os.path.exists("/usr/lib64/chromium-browser/chromedriver"):
	self.driver = self.webdriver.Chrome(executable_path="/usr/lib64/chromium-browser/chromedriver", chrome_options=self.options)
```

直接运行源码需要安装Python的WebDriver组件

 `pip3 install selenium`

` pip3 install requests`

之后可直接运行源码

 `python3 pandalearning.py`