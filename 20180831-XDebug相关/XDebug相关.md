一.**DBGP协议**



1.   用途：用于调试应用程序的一种协议。

2. 对象：调试器引擎（就是你正在调试的语言引擎，如python解释器）和调试器IDE之间的通信。
3. 端口：IDE监听端口9000。

二.**XDebug**







- 用途：是一个 PHP 的调试工具，支持在本地通过源码远程调试服务器上的 PHP 代码。


- 调试步骤：

    服务器(Httpd服务器，PHP后端引擎，PHP配置好的Xdebug）

    调试者（IDE+Xdebug插件，浏览器）

    	1.调试者开启IDE的插件，监听9000端口
    	2.调试者通过浏览器进行访问Httpd服务器里的一个PHP文件。
    	3.上一步中，浏览器会发送一个XDEBUG_SESSION_START参数的请求，Httpd服务器收到这个请求之后交给后端的PHP进行处理
    	4.PHP引擎接收请求，通知已配置的Xdebug准备
    	5.服务器端Xdebug向调试者的9000发送debug请求
    	6.调试者的9000端口响应
    	7.服务器中的PHP引擎收到回复，开始执行代码，每一行都通过Xdebug过滤
    	8.Xdebug过滤就会暂停执行，向9000端口发送执行情况，等待客户端的决策。相应，IDE收到Xdebug发送过来的执行情况，就可以把这些信息展示给调试者，包括一些变量的值等。同时向Xdebug发送下一步应该什么。
    
    参考

 [https://my.oschina.net/atanl/blog/371424](https://my.oschina.net/atanl/blog/371424)

 [http://phonegap.me/post/27.html](http://phonegap.me/post/27.html)

三.**XDebug 远程调试漏洞（代码执行）复现**

[参考](https://github.com/FarFromBeing/vulhub/tree/master/php/xdebug-rce)