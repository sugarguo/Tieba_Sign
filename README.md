# Tieba_Sign

>You can automatically sign~ :)你能够在贴吧自动签到



#Summary

你能够通过我的i贴吧获取你喜欢的贴吧列表，然后得到你的连接v码和需要签到的页数times

>http://tieba.baidu.com/i/********/forum
>>星号为你的v码

然后通过火狐浏览器的F12查看网络连接得到你的tbs和账号的cookie

通过这些能够让这个python脚本运行起来

通过判断返回的error码获取是否签到成功，记录保存在tieba_log.txt



#Attention

* python版本为2.7.10 python2基本通用

* 需要requests、lxml

* times = 3 三为我的i贴吧页码，如果你的i贴吧有1面，则将3改为2

* 需要获取v号码

* 需要得到tbs号码

* 需要你的账号cookie

* ###当需要签到的贴吧多的时候，会有验证码提示，请停止程序然后用手机签到，隔天再使用脚本签到



#Update History

###2015-10-12 Just OK 已经可以进行简单的签到

###2015-10-12 Create  确定想法
