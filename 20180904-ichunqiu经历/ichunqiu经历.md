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