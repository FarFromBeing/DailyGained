一.**对序列化和反序列化有了初步了解**

见[Python](https://github.com/FarFromBeing/Python/tree/master/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/pickling)的一个记录例子

二.**CDN**

内容分发网络，将用户的请求定向到最合适的缓存服务器上去获取内容，就近取材。
[图片来源](https://www.zhihu.com/question/36514327?rf=37353035 "图片来源")
![](https://i.imgur.com/wFVEJou.png)

三.**回顾XXE**

1. 漏洞产生原因

    应用程序解析 XML 输入时，没有禁止外部实体的加载。
2. 漏洞产生点
   
    可以上传xml 文件的地方。