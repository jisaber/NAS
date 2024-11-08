# NAS
局域网轻型NAS软件

# 目录结构
```
G:.
├─.venv
│  ├─Include
|  └─...
├─source // 你要放置的源文件
│  ├─xxxx
│  ├─1053
│  │  ├─XXX.mp4
│  └─XXXZ
├─static // 你要放置的源文件
│  ├─xxxx
│  ├─1053
│  │  ├─XXX.mp4
│  └─XXXZ
├─templates // 用于显示的模板文件
│  ├─xxx.html
│  ├─error.html
├─nas.py
├─tool.py
└─xxx.py
```
# 简单运行
1、先安装python
参考 https://www.python.org/
2、创建虚拟和安装Flask
参考https://flask.palletsprojects.com/en/3.0.x/installation/
执行
```
python -m venv .venv
.venv\Scripts\activate
pip install Flask
pip install flask-bootstrap
```
3、运行flask即可
```
flask --app nas run --debug --host=192.168.2.244 --port=520
注：nas表示主python文件名, debug打开调试模式, host本地IP, port=端口
```

4、本地获取IP方法
执行ipconfig会得到下面的内容，其中网线看以太网那一栏，wifi接入看无线局域网那一栏
```
PS G:\迅雷下载\NAS> ipconfig

Windows IP 配置


未知适配器 本地连接:

   连接特定的 DNS 后缀 . . . . . . . :
   本地链接 IPv6 地址. . . . . . . . : 0123::0123:0123:0123:0123%9
   IPv4 地址 . . . . . . . . . . . . : 2.0.0.1
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . :

以太网适配器 以太网:

   连接特定的 DNS 后缀 . . . . . . . :
   本地链接 IPv6 地址. . . . . . . . : 0123::0123:0123:0123:0123%18
   IPv4 地址 . . . . . . . . . . . . : 192.168.137.1
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . :

无线局域网适配器 WLAN:

   连接特定的 DNS 后缀 . . . . . . . : lan
   本地链接 IPv6 地址. . . . . . . . : 0123::0123:0123:0123:0123%11
   IPv4 地址 . . . . . . . . . . . . : 192.168.2.244
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . : 192.168.2.1
```

5、示例
![Image text](images/)