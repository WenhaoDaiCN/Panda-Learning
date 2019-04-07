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



直接运行源码需要安装Python的WebDriver组件

`pip3 install selenium`

` pip3 install requests`

之后可直接运行源码

 `python3 pandalearning.py`