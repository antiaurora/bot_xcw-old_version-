# bot_xcw

private QQ robot, whose persona is about an animation character called "xcw" among players. 

私人QQ机器人，它的人设是被玩家称为xcw的动漫角色。
（相关人设的应答更新于2021.4.13）

（上传完毕后会修改QQ密码）

先咕



慢慢上传



6.22
最近机器人一直崩，不知道什么原因 raise SSLError(e, request=request) 
莽一波，去修改requests
修改了C:\Users\Administrator\AppData\Local\Programs\Python\Python38\lib\site-packages\requests\adapters.py的394行和61行，verify=~~True~~False

6.23
稳定一天了，好家伙，奇怪的知识增加了

7.2
升级mirai框架了，差得还挺多，图片的具体类型也纪录了
例如：接受到一张图片，旧版记录的是[CQ:image,file={691AAC1E-DF02-37DA-A690-831512CFE3FD}.mirai.mnimg]，现在记录的是[CQ:image,file={691AAC1E-DF02-37DA-A690-831512CFE3FD}.jpg.mnimg]
导致的结果就是，以前基于图片的应答要进行修改（关键词中，mirai.mnimg->jpg.mning），好在回答不用改，或许是做了兼容。
