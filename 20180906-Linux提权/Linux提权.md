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