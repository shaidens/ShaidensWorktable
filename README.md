# 项目介绍
```
本项目属于Shaiden定制计划的项目之一，主要负责在电脑系统平台的功能、工具、主题定制
```

# 环境依赖

```
Python3
	——pyside2
	——qfluentwidgets
	——simplejson
	——request
	——urllib3
	
```



    haha nothing here~
    └──res                 //资源文件

# 使用说明

 

```
暂无详细
```



# 版本内容更新
###### beta 25w02a - 2025/2/*: 
```()
1.部分重构Home界面(home.py)
	优化九宫格任务栏，新增顶部、右下部，新增顶部背景图
2.将GUI调整为dark主题
```

 

###### beta 25w02a - 2025/2/*: 

```
1.删除一些冗余的注释，补充一些必要的陈述...(doge)
```



###### beta 25w02b - 2025/2/19:

```
1.整改了gui文件的放置位置与命名，使其更加可读和整洁，间接提高了后期可维护性
2.规范了部分代码写法
3.完成了软件库的初始GUI设计
4.完善开发者文档
```



###### beta 25w02c - 2025/2/22:

```
1.完成并入了软件库(SoftWareLib)的GUI界面，并简单与Root_guiCore对接，暂未实现任何功能
2.修补了之前丢备份错版过时的代码
3.删除了部分无用注释
```



###### beta 25w03a - 2025/3/08:

```
1.完成了server与client关于软件库data的交互（暂未debug）
2.整理了代码逻辑
```



###### beta 25w04a - 2025/4/08:

```
1.将客户端及gui、guicore、function关于data交互的内容进行编写，但未完成
2.完善了json文件的基本格式说明注释
```



###### **beta 25w05a - 2025/5/02:**

```
1.完成了初步的软件库新增Card组件，但并未for循环应用和进行任何测试
2.修复了循环引用问题
3。新增了SoftwareLib_GUIcore文件
```



###### beta 25w05b - 2025/5/03:

```
1.完成了客户端与服务端的基本关于software——Data的数据传输，未进行处理
2.新增用于本地测试的配置组
2.修复了一些小bug
```



###### beta 25w05c - 2025/5/11:

```
1.修复了一些软件库data传输的小bug
2.完善了SoftwareLib_GUIcore的部分框架，从SoftwareLib_GUI中转移了部分内容

tips:本次测试后服务器配置组仍然设置在“test”本地调试
```



###### beta 25w05d - 2025/5/13:

```
1.修复了上次更新未debug发现的致命bug——SoftwareLib_GUIcore的鬼、不显示问题与function.API()单例问题
2.基本实现了SoftwareLib GUI界面for循环label选项卡，但图标及详细问题暂未处理和设置
```



###### beta 25w05e - 2025/5/24：

```
1.完成了解析url完成软件库icon图片显示的branch！
```



###### beta 25w06a -2025/6/25-2025/6/29：

```python
1.修复了代码小bug
2.完成了软件download按钮的下载功能，但未解决按钮信号与槽绑定后真格界面不显示的不过且多线程下载未经debug。
3.在SoftwareLib_GUIcore.SoftwareLib_ui中新增了 def _contents_reload(self) 方法，并对应完善了包括functions.api、client.py在内的功能小完善。
4.在function初始化时新增了必要目录初始化功能，新增的目录包括 ./Shaiden's/data内的所有目录
5.(第2点内容的分支)functions.api中相应添加了 def Software_if_exist(self,title:str) -> bool方法
```



###### beta 25w07a -2025/7/2:

```
1.基本重构了并完善了软件库内容的下载代码，改用了Thread并使用了单主线程领导多个子线程下载的方式。
***bug：当线程数较低时，可能出现Process finished with exit code -1073740791 (0xC0000409)，线程数20时没有问题
***sep：线程数的初始值为0，应更改为cpu核心数x2
***sep: 一些参数的更改没有与GUI相连接
2.修复了一些较为致命的bug
3.优化了关于在software下载中的文件夹创建逻辑
*4.将python更新到了64位 3.7.3，并重新创建了新的虚拟环境.venv
5.在function.py中加入了gc进行内存回收
```



###### beta 25w07b -2025/7/8:

```
1.优化了线程逻辑，修复了获取文件大小部分造成的堵塞，并修复了线程致命bug
```



###### beta 25w08\* -2025/8/*:

###### *(月开发巨大变更版本)*

```
对整个项目重置，重置包括但不限于
     1.架构
     2.代码逻辑
     3.前后端沟通
     4.部分代码内容

```
