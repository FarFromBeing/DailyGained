# DailyGained
每天或者几天整理的新知识



*20180831*

一.**DBGP协议**



1.   用途：用于调试应用程序的一种协议。

2. 对象：调试器引擎（就是你正在调试的语言引擎，如python解释器）和调试器IDE之间的通信。
3. 端口：IDE监听端口9000。

二.**XDebug**



-  用途：是一个 PHP 的调试工具，支持在本地通过源码远程调试服务器上的 PHP 代码。

- 调试步骤：

    服务器(Httpd服务器，PHP后端引擎，PHP配置好的Xdebug）

    调试者（IDE+Xdebug插件，浏览器）

    1. 调试者开启IDE的插件，监听9000端口
    2. 调试者通过浏览器进行访问Httpd服务器里的一个PHP文件。
    3. 上一步中，浏览器会发送一个XDEBUG_SESSION_START参数的请求，Httpd服务器收到这个请求之后交给后端的PHP进行处理
    4. PHP引擎接收请求，通知已配置的Xdebug准备
    5. 服务器端Xdebug向调试者的9000发送debug请求
    6. 调试者的9000端口响应
    7. 服务器中的PHP引擎收到回复，开始执行代码，每一行都通过Xdebug过滤
    8. Xdebug过滤就会暂停执行，向9000端口发送执行情况，等待客户端的决策。相应，IDE收到Xdebug发送过来的执行情况，就可以把这些信息展示给调试者，包括一些变量的值等。同时向Xdebug发送下一步应该什么。
    
    参考

       [https://my.oschina.net/atanl/blog/371424](https://my.oschina.net/atanl/blog/371424)

       [http://phonegap.me/post/27.html](http://phonegap.me/post/27.html)

三.**XDebug 远程调试漏洞（代码执行）复现**

参考[https://github.com/FarFromBeing/vulhub/tree/master/php/xdebug-rce](https://github.com/FarFromBeing/vulhub/tree/master/php/xdebug-rce)


----------


*20180901*

一.**对XSS，CSRF有了新的理解**
对于结果来说都是通过cookie来搞事



- XSS是利用攻击的方式完成入侵，比如存储型的，长期控制式的入侵。


- CSRF是“借刀干活”，只是通过盗用一个合法身份的角色认证，去完成这个角色能干的事。

二.**htaccess文件**
Apache的配置总文件，存放于服务器的目录中，运行时会被加载，执行其中的设置。


三.**CTF日常**



1. php的敏感信息泄露形式
例如：user.php.bak

1. 通过提示构建爆破字段，使用battering ram选项进行爆破
介绍：攻城锤模式（Battering ram）——它使用单一的Payload集合，依次替换Payload位置上被§标志的文本（而没有被§标志的文本将不受影响），对服务器端进行请求，与sniper模式的区别在于，如果有多个参数且都为Payload位置标志时，使用的Payload值是相同的，而sniper模式只能使用一个Payload位置标志。

1. 文件上传，可以尝试的格式：
.php .php3 .php4 .php5 .pht .phtml等

----------

*20180902*

一.**对序列化和反序列化有了初步了解**
见[https://github.com/FarFromBeing/Python/tree/master/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/pickling](https://github.com/FarFromBeing/Python/tree/master/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/pickling)

二.**CDN**

内容分发网络，将用户的请求定向到最合适的缓存服务器上去获取内容，就近取材。
[图片来源](https://www.zhihu.com/question/36514327?rf=37353035 "图片来源")
![](https://i.imgur.com/wFVEJou.png)

三.**回顾XXE**

1. 漏洞产生原因

    应用程序解析 XML 输入时，没有禁止外部实体的加载。
2. 漏洞产生点
   
    可以上传xml 文件的地方。



----------

*20180904*

一.**在Ichunqiu上完成的一次综合网站渗透**


1. 前期工作略 
2. *一句话位置*: 在数据库设置里，将上传的图片生成代码作为数据库路径，然后设置了备份路径，是因为这个路径下具有可写可读权限，同理的还有友情链接的的设置。方便后面用菜刀进行连接。
3. *Administrator的hash的位置*：菜刀连接后，要获得Administrator的hash,这个保存在`C:\windows\system32\config\SAM`里，一个加密的文件。也可以尝试用SAMInside进行破解。
4. *提权方式*：在这次模拟中，是通过一个WIN2003下的本地提权漏洞，通过churrasco(巴西烤肉)工具进行添加用户，并把这个用户放到管理组里。通过`mstsc`进入win2003服务器*******
5. *hash获取*：通过菜刀传pwdump7和其dll文件，才服务器上运行`pwdump7 > hash.txt` dump下来一个有各路人员的账号密码hash值。[在这里进行破解](http://www.objectif-securite.ch/en/ophcrack.php)
6. *数据库SA密码获取*：因为web应用和数据库会有一个配置文件，用来保存数据库连接信息，包括数据库驱动、数据库名、用户名、密码等信息，找到这个文件就找到了密码
。


> Struts配置文件：struts-config.xml文件
> 
> Tomcat配置文件：config/server.xml文件

二.**一次问答**

前期情报收集：

[撒旦](https://www.shodan.io/)

[钟馗之眼](https://www.zoomeye.org/)

[censys](https://censys.io/)


三.**查看CMS的方法**

1./robots.txt
可能会出现版本的注释信息
2.在第一步基础上，将一些没有显示的Disallow选项代入搜索
3.看源码，或许有注释
四.收集服务器信息命令

- 查看下载补丁：

   `wmic qfe get Caption,Description,HotFixID,InstalledOn`

----------


*20180906*

一.**Linux提权**


> 
>  使用NC来连接
> 
> 
> - 扫描开放端口
> 
>     `nc -nvz 192.168.1.7 1-65535`
> 
> 
> - 连接
> 
> 	`nc 192.168.1.7 666`


利用**crontab**---*用来定期执行程序的命令*。当安装完成操作系统之后，默认便会启动此任务调度命令。



- linux任务调度的工作主要分为以下两类

系统执行的工作：系统周期性所要执行的工作，如备份系统数据、清理缓存。

个人执行的工作：某个用户定期要做的工作，例如每隔10分钟检查邮件服务器是否有新信，这些工作可由每个用户自行设置。


- 命令参数
`-u user`：用来设定某个用户的crontab服务；

`file`：file是命令文件的名字,表示将file做为crontab的任务列表文件并载入crontab。如果在命令行中没有指定这个文件，crontab命令将接受标准输入（键盘）上键入的命令，并将它们载入crontab。

`-e`：编辑某个用户的crontab文件内容。如果不指定用户，则表示编辑当前用户的crontab文件。

`-l`：显示某个用户的crontab文件内容，如果不指定用户，则表示显示当前用户的crontab文件内容。

`-r`：从/var/spool/cron目录中删除某个用户的crontab文件，如果不指定用户，则默认删除当前用户的crontab文件。

`-i`：在删除用户的crontab文件时给确认提示。



- 使用实例如图

![](https://i.imgur.com/60qCT62.png)

![](https://i.imgur.com/pratKMD.png)

   [图二来源](http://www.cnblogs.com/peida/archive/2013/01/08/2850483.html)


**提权操作过程**
1).确认是guest身份以后，检查是否安装corntab，命令是crontab -l.显示“no crontab for root”或者是没有回显，则证明，系统中有安装corntab。目的主机正好有安装crontab.

2).通过cat /etc/crontab命令查看crontab文件。

3).找到已存在的任务命令，进行修改，定时增加新用户。



二.**Linux命令记录**

w:查看当前活跃的用户

![](https://i.imgur.com/uWNjAzn.png)