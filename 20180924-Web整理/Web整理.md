**之前对Web一系列的组织结构有点疑惑，在此做个简单记录，有空进行手动搭建的再进行详细记录。**

 1. Web框架：Django,Flask,Tornado等，**编程语言构成的一种整合**
 2. Web服务器：Nginx，Apache，IIS等，**起到转发服务器的作用。**
 3. 应用服务器：Gunicorn，uWSGI等WSGI容器，**在web服务器和框架之间进行一个处理调度作用**。
 
下图是以Nginx为例

![](https://i.imgur.com/47mQL07.png)

公网发来请求，

先通过Nginx-Web服务器进行请求的转发，

再由WSGI容器进行调度处理请求，

最后由应用层框架来相应每个请求。



[参考文章][2]


  
  [2]: http://www.cnblogs.com/piperck/p/5150115.html