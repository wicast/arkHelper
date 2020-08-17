# simpleArknightHelper
One Easy-Use Arknight Helper	一款明日方舟护肝小助手



##### 写在前面：

> 我本人并不是一名专业的程序员，代码质量并不高，时间也不充裕。同时也是一名github的新使用者，还请大家多多指教。



##### 下载地址：

| 网盘   | 链接                                          |
| :----- | --------------------------------------------- |
| 蓝奏云 | [下载地址](https://www.lanzous.com/b0d1w6v7g) |
|Github|[release](https://github.com/MangetsuC/arkHelper/releases)|
> * 下载提供的是master分支使用pyinstaller打包后的文件，可以直接使用，而无需安装python。
>
> * 国内用户可以使用蓝奏云链接，速度较快



##### **Requirements**：

| 库         | 版本  |
| ---------- | ----- |
| aircv      | 1.4.6 |
| win10toast | 0.9   |
| Pillow     | 7.1.2|
|PyQt5|5.15.0|

> 你也可以在仓库里找到requirements.txt，并使用pip install -r requirements.txt来部署环境。
***
##### 适用场景
# 任何场景！

##### 特别适用的场景
|活动|主线|剿灭作战|
|----|----|----|
|骑兵与猎人|1-7|全部|
|火蓝之心|||
|生于黑夜|||
***
## 关于这个小助手：

### 界面
***
![newUI.png](https://i.loli.net/2020/08/15/7kVP6Jc34GHzBsK.png)
* metro风格的界面参考了windows10的菜单，简洁明了  
* 可以方便地通过主界面上的菜单来选择您的模拟器！也可以自定义  
## 特色功能！——计划战斗
### 打开计划战斗选项
***
![schedule0.png](https://i.loli.net/2020/08/15/2QEaXCMcALoW41G.png)
* 小助手会根据您的配置，自动按规划的路线进行战斗
* 不论是正好差一次剿灭，还是想要从1-7中获得8个固源岩，都可以实现
* 仅支持主线、物资筹备、芯片搜索和剿灭作战，即一般不支持活动关卡
* 如果启用计划战斗，请在首页或是可以看到HOME图标的界面启动小助手
### 使用路线规划窗口编辑您的计划
***
![scheduleGIF.gif](https://i.loli.net/2020/08/17/cDr89tUMjqWfNYb.gif)
#### 通过次数设定
* 不选中素材模式，即可设定目标关卡的目标次数
#### 更棒的！通过素材设定！
* 选中素材模式，您便可以打开选择掉落物窗口，指定您想要获得的素材和它的个数！
***
* 可以通过新建配置将您的计划存储起来，而加载配置则可以方便的调用
* 素材设定的关卡与次数设定的关卡可以同时在规划中出现，图片中未演示
* 设置关卡的时候请务必填入正确的关卡名，否则会发生什么我也没试过（笑）
## 通用功能
### 单一关卡循环作战
***
![battle.png](https://i.loli.net/2020/08/15/WzCLcKe9EkyNMtS.png)
* 这个选项用于在您已选择的关卡不断循环，直到理智耗尽
#### 在何时启动
![auto.png](https://i.loli.net/2020/05/04/NbRDLEm437xFXWQ.png)
* 如果您仅使用循环作战，您至少应当在此状态下启动
* 实际上，您也可以先进入代理指挥开始战斗，再启动小助手
### 任务交付
***
![task.png](https://i.loli.net/2020/08/15/UYcVFzhCMbjSlk1.png)
* 不知您有没有注意到界面上被选中的任务开关，这代表在战斗结束后小助手会帮助您交付任务！
### 获取信用
***
![credit.png](https://i.loli.net/2020/08/15/mbayH2cWN4jl1eC.png)
* 自动访问你的好友来获取更多的信用点数！
### 获取额外的理智
***
![add.png](https://i.loli.net/2020/08/15/SlLdyjhxZDWEOC5.png)
* 您可以在这里设置当理智不足时是否使用理智合剂或源石恢复
* 源石恢复可以设置上限，计划作战与循环战斗共用一个上限值
> 实际上，使用源石恢复理智我并没有测试过，但是大概没有问题（笑）
### 关闭计算机
***
![shut.png](https://i.loli.net/2020/08/15/ZrvBLimK5W8tXya.png)
* 启用此选项，当小助手完成全部工作，它就会尝试关闭计算机并自动退出
* 该功能关闭计算机有2分钟倒计时，您可以用`shutdown -a`指令来取消关闭计算机的计划
### 这些是开关
***
![setDefault.png](https://i.loli.net/2020/08/15/T9CavxGuVpzDRoE.png)
* 因此，如果您不需要这个功能，可以单击以关闭
* 使用右键菜单来设置功能的默认状态
### 公开招募计算器
***
![publiccall.png](https://i.loli.net/2020/08/15/oXJdm3SKv6zltRV.png)
* 便捷的公开招募计算器，从你的模拟器屏幕上直接获取标签信息！
* 主要的作用是避免错过一些不起眼的标签组合
### 提示！
***
![notice.png](https://i.loli.net/2020/05/04/bEJzCVqj37ADLmk.png)
* 在理智耗尽或是其他一些活动完成后，会通知提示您！
## 一些小细节
### 1. 小助手执行任务的顺序
实际上是 计划战斗 ⟶ 循环战斗 ⟶ 任务交付 ⟶ 信用获取 ⟶ 关闭计算机，在战斗环节中判断是否消耗额外理智
### 2. 我想要在计划作战中无限循环某一关
当然，你可以设置某一关的次数是999。
但实际上，由执行顺序可以发现，如果你把想要无限循环的那一关放在计划的最后，并同时启用计划战斗和循环战斗，这一关就会不断执行直到理智耗尽了。
### 3. 关于ADB
实际上，只有当你按下开始按钮或者点击公招计算器的时候，小助手才会开始尝试启动adb。
但当你点击小助手的退出时，它会终止电脑上的所有adb进程，因此请注意在使用其它依赖adb的的程序时，不要退出小助手。
### 4. 有关下一步更新的计划
大概是在计划战斗中加入某材料多少个这样的判断条件吧，想着直接设置要3个扭转醇和5个固源岩就可以运行了，太美好了。
至于什么时候能真的上线，我并不清楚，而我目前的进度是，约1%我猜，还处在思考怎么实现的阶段（悲）。