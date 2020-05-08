import sys
from webbrowser import open as openUrl
from configparser import ConfigParser
from os import getcwd
from threading import Thread

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QFont, QIcon, QMouseEvent
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QDesktopWidget,
                             QGridLayout, QInputDialog, QLabel, QMenu,
                             QPushButton, QWidget)

from foo.adb.adbCtrl import Adb
from foo.arknight.Battle import BattleLoop
from foo.arknight.task import Task
from foo.ui.console import Console


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initVar()
        self.initUI()
        self.initState()
        self.isRun = False
        
    def initUI(self): 
        self.setWindowIcon(QIcon(self.ico))
        self.setFixedSize(362,200)
        self.center()

        self.setWindowFlag(Qt.FramelessWindowHint) #隐藏边框
        self.setStyleSheet('''App{background:#272626}QLabel{color:#ffffff;font-family:"Microsoft YaHei", SimHei, SimSun;font:9pt;}
                                QPushButton{border:0px;background:#4d4d4d;color:#ffffff;font-family: "Microsoft YaHei", SimHei, SimSun;font:10pt;}
                                QPushButton:hover{border-style:solid;border-width:1px;border-color:#ffffff;}
                                QPushButton:pressed{background:#606162;font:9pt;}
                                QPushButton:checked{background:#70bbe4;}
                                QInputDialog{background-color:#272626;}''')

        self.btnStartAndStop = QPushButton('启动虚拟博士', self) #启动/停止按钮
        self.btnStartAndStop.setFixedSize(180, 180)
        self.btnStartAndStop.setStyleSheet('''QPushButton{font:13pt;}''')
        self.btnStartAndStop.clicked.connect(self.clickBtnStartAndStop)

        self.tbBattle = QPushButton('战斗', self) #战斗可选按钮
        self.tbBattle.setCheckable(True)
        self.tbBattle.setFixedSize(75, 40)
        self.tbBattle.clicked[bool].connect(self.functionSel)

        self.tbTask = QPushButton('任务交付', self) #任务交付可选按钮
        self.tbTask.setCheckable(True)
        self.tbTask.setFixedSize(75, 40)
        self.tbTask.clicked[bool].connect(self.functionSel)

        self.btnSet = QPushButton('设置',self) #设置按钮
        self.btnSet.setFixedSize(75, 40)

        self.settingMenu = QMenu() #创建设置按钮菜单
        self.settingMenu.setStyleSheet('''QMenu {color:#ffffff;font-family: "Microsoft YaHei", SimHei, SimSun;font:10pt;background-color:#222724; margin:3px;}
                                        QMenu:item {padding:8px 32px;}
                                        QMenu:item:selected { background-color: #3f4140;}
                                        QMenu:icon{padding: 8px 20px;}''')
        self.actSimulator = QMenu('模拟器', parent=self.settingMenu) #模拟器二级菜单
        self.actSlrBlueStacks = QAction('蓝叠模拟器', parent=self.actSimulator)
        self.actSlrMumu = QAction('Mumu模拟器', parent=self.actSimulator)
        self.actSlrYeshen = QAction('夜神模拟器', parent=self.actSimulator)
        self.actSlrXiaoyao = QAction('逍遥模拟器', parent=self.actSimulator)
        self.actSlrCustom = QAction('自定义', parent=self.actSimulator)
        
        self.slrList = [self.actSlrBlueStacks, self.actSlrMumu, self.actSlrXiaoyao, self.actSlrYeshen, self.actSlrCustom]

        self.actConsole = QAction('控制台', parent=self.settingMenu)
        self.checkUpdate = QAction('检查更新', parent=self.settingMenu)
        self.index = QAction('访问主页', parent=self.settingMenu)

        #添加菜单选项
        self.settingMenu.addMenu(self.actSimulator) #模拟器二级菜单
        for eachSlr in self.slrList:
            self.actSimulator.addAction(eachSlr)
            eachSlr.triggered.connect(self.simulatorSel)

        self.settingMenu.addAction(self.actConsole) #控制台
        self.actConsole.triggered.connect(self.console.showOrHide)

        self.settingMenu.addAction(self.checkUpdate) #蓝奏云地址
        self.checkUpdate.triggered.connect(self.openUpdate)

        self.settingMenu.addAction(self.index) #主页
        self.index.triggered.connect(self.openIndex)

        self.btnSet.setMenu(self.settingMenu) #关联按钮与菜单
        self.btnSet.setStyleSheet('''QPushButton:menu-indicator{image:none;width:0px;}''')

        self.btnMin = QPushButton('最小化',self) #最小化按钮
        self.btnMin.setFixedSize(155, 40)
        self.btnMin.clicked.connect(self.minimize)

        self.btnClose = QPushButton('退出',self) #退出按钮
        self.btnClose.setFixedSize(75, 40)
        self.btnClose.clicked.connect(self.exit)
        
        self.lNotice = QLabel('按此处可拖动窗口')

        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        
        self.grid.addWidget(self.btnStartAndStop, 0, 0, 4, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(self.tbBattle, 0, 1, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(self.tbTask, 0, 2, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(self.btnSet, 2, 1, 1,1, alignment=Qt.AlignCenter)
        self.grid.addWidget(self.btnMin, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        self.grid.addWidget(self.btnClose, 2, 2, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(self.lNotice, 3, 1, 1, 2, alignment=Qt.AlignRight)

        self.setLayout(self.grid)

        self.show()

    def initVar(self):
        self.cwd = getcwd().replace('\\', '/')

        self.ico = self.cwd + '/res/ico.ico'
        self.selectedPNG = self.cwd + '/res/gui/selected.png'

        self.console = Console(self.cwd) #接管输出与报错

        self.configPath = self.cwd + '/config.ini'
        self.config = ConfigParser()
        self.config.read(filenames=self.configPath, encoding="UTF-8")

        self.adb = Adb(self.cwd + '/bin/adb', self.config)
        self.battle = BattleLoop(self.adb, self.cwd, self.ico)
        self.task = Task(self.adb, self.cwd, self.ico)

        self.btnMainClicked = False

        self.battleFlag = None
        self.taskFlag = None
        self.doctorFlag = False


    def initState(self):
        self.initSlrSel()
        
        #功能开关
        self.battleFlag = self.config.getboolean('function', 'battle')
        self.tbBattle.setChecked(self.battleFlag) #战斗选项
        self.taskFlag = self.config.getboolean('function', 'task')
        self.tbTask.setChecked(self.taskFlag) #任务选项
        pass
    
    def initSlrSel(self):
        '初始化模拟器选择'
        slrName = self.config.get('connect', 'simulator')
        if slrName == 'bluestacks':
            self.actSlrBlueStacks.setIcon(QIcon(self.selectedPNG))
        elif slrName == 'mumu':
            self.actSlrMumu.setIcon(QIcon(self.selectedPNG))
        elif slrName == 'yeshen':
            self.actSlrYeshen.setIcon(QIcon(self.selectedPNG))
        elif slrName == 'xiaoyao':
            self.actSlrXiaoyao.setIcon(QIcon(self.selectedPNG))
        elif slrName == 'custom':
            self.actSlrCustom.setIcon(QIcon(self.selectedPNG))

    def center(self):
        #显示到屏幕中心
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePos = event.globalPos() - self.pos() #获取鼠标相对窗口的位置
            #print(self.mousePos.x(),self.mousePos.y()) #调试参考选择可移动区域
            if self.mousePos.x() > 190 and self.mousePos.y() > 150: #判断是否在可移动区域
                self.moveFlag = True
            else:
                self.moveFlag = False
            event.accept()
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.moveFlag:  
            self.move(QMouseEvent.globalPos() - self.mousePos) #更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        #停止窗口移动
        self.moveFlag = False
    
    def functionSel(self, isChecked):
        source = self.sender()
        if source.text() == '战斗':
            self.battleFlag = isChecked
        elif source.text() == '任务交付':
            self.taskFlag = isChecked

        

    def changeSlr(self, name, port, ip = '127.0.0.1'):
        self.config.set('connect', 'simulator', name)
        self.config.set('connect', 'port', port)
        self.config.set('connect', 'ip', ip)
        
        configInI = open(self.configPath, 'w')
        self.config.write(configInI)
        configInI.close()
        self.adb.changeConfig(self.config)


    def simulatorSel(self):
        slrName = self.sender().text()
        if slrName == '蓝叠模拟器':
            self.changeSlr('bluestacks', '5555')
        elif slrName == 'Mumu模拟器':
            self.changeSlr('mumu', '7555')
        elif slrName == '夜神模拟器':
            self.changeSlr('yeshen', '62026')
        elif slrName == '逍遥模拟器':
            self.changeSlr('xiaoyao', '21503')
        else:
            customIp, isOk = QInputDialog.getText(self, '自定义', '请输入模拟器IP地址')
            if isOk:
                customPort, isOk = QInputDialog.getText(self, '自定义', '请输入模拟器端口号')
                if isOk:
                    self.changeSlr('custom', customPort, customIp)

        for each in self.slrList:
            each.setIcon(QIcon(''))

        self.initSlrSel()
        
    def exit(self):
        '退出按钮'
        self.stop()
        self.console.exit()
        self.close()

    def minimize(self):
        '最小化按钮'
        self.showMinimized()

    def openUpdate(self):
        openUrl('https://www.lanzous.com/b0d1w6v7g')

    def openIndex(self):
        openUrl('https://github.com/MangetsuC/arkHelper')

    def start(self):
        self.doctorFlag = self.battle.connect()
        if self.doctorFlag and self.battleFlag:
            self.battle.run(self.doctorFlag)
        if self.doctorFlag and self.taskFlag:
            self.task.run(self.doctorFlag)
        self.stop()

    def stop(self):
        self.doctorFlag = False
        self.battle.stop()
        self.task.stop()
        self.btnMainClicked = False
        self.btnStartAndStop.setText('启动虚拟博士')

    def clickBtnStartAndStop(self):
        self.btnMainClicked = not self.btnMainClicked
        if self.btnMainClicked:
            self.btnStartAndStop.setText('停止虚拟博士')
            self.thRun = Thread(target=self.start)
            self.thRun.setDaemon(True)
            self.thRun.start()
        else:
            self.stop()
       
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())