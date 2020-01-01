import traceback
import time
from PyQt5.QtCore import Qt,QPoint,QTimer
import sys
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from PyQt5.QtGui import QPainter,QPen,QColor,QPalette,QBrush,QPixmap,QRadialGradient
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtMultimedia
from Game.game import Comoku
from Game.Game_widget import CornerWidget

def run_with_exc(f):
    """游戏运行出错时，messagebox弹窗显示出无信息"""
    def call(window,*args,**kwargs):
        try:
            return f(window,*args,**kwargs)
        except Exception:
            exc_info = traceback.format_exc()
            QMessageBox.about(window,"错误信息",exc_info)
    return call

class ComokuWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.g = Comoku()
        self.display = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.operate)
        self.count = 0
    def operate(self):

        if self.display == True:
            self.display = False

        else:
            self.display = True
            self.count += 1
        self.repaint(0,0,650,650)
        if self.count >= 3:
            self.game_restart(self.g.result)
    def init_ui(self):
        """初始化游戏界面"""
        # 1.确定游戏界面的标题、大小和背景颜色
        self.setObjectName("MainWindow")
        self.setWindowTitle("五子棋")
        self.setFixedSize(650,650)

        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(QPixmap("bgp.jpg")))
        self.setPalette(palette)
        # 2.鼠标位置追踪
        self.setMouseTracking(True)
        # 3. 鼠标位置移动时，对鼠标位置进行标记
        self.corner_widget = CornerWidget(self)
        self.corner_widget.repaint()
        self.corner_widget.hide()

        # 2.显示初始化游戏界面
        self.show()

    @run_with_exc
    def paintEvent(self,e):
        """绘制游戏内容"""

        def draw_map():
            """绘制棋盘"""

            qp.setPen(QPen(QColor(0,0,0),2,Qt.SolidLine))
            #绘制横线
            for x in range(15):
                qp.drawLine(40 * (x + 1),40,40 * (x + 1),600)
            #绘制竖线
            for y in range(15):
                qp.drawLine(40,40 * (y + 1),600,40 * (y + 1))
            #绘制棋盘星位
            qp.setBrush(QColor(0, 0, 0))
            key_point = [(4,4),(12,4),(4,12),(12,12),(8,8)]
            for t in key_point:
                qp.drawEllipse(QPoint(40 * t[0], 40 * t[1]),5,5)

        def draw_piecess():
            """绘制棋子"""
            winstep = self.g.getWinnerStep()

            #绘制黑棋子
            qp.setPen(QPen(QColor(0,0,0),1,Qt.SolidLine))
            #qp.setBrush(QColor(0,0,0))
            for x in range(15):
                for y in range(15):
                    if self.g.g_map[x][y] == 1:
                        if winstep != None:
                            if (x,y) in winstep :
                                if self.display == True:
                                    radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)
                                    radial.setColorAt(0, QColor(96, 96, 96))
                                    radial.setColorAt(1, QColor(0, 0, 0))
                                    qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)

                            else:
                                radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)
                                radial.setColorAt(0, QColor(96, 96, 96))
                                radial.setColorAt(1, QColor(0, 0, 0))
                                qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)


                        else:
                            radial = QRadialGradient(40 * (x + 1),40 * (y + 1), 15, 40 * x + 35,40 * y + 35)
                            radial.setColorAt(0,QColor(96,96,96))
                            radial.setColorAt(1,QColor(0,0,0))
                            qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)
            #绘制白棋子
            qp.setPen(QPen(QColor(160, 160, 160), 1, Qt.SolidLine))
            qp.setBrush(QColor(255, 255, 255))
            for x in range(15):
                for y in range(15):
                    if self.g.g_map[x][y] == 2:
                        if winstep != None:
                            if (x,y) in winstep :
                                if self.display == True:
                                    radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)
                                    radial.setColorAt(0, QColor(255, 255, 255))
                                    radial.setColorAt(1, QColor(255, 255, 255))
                                    qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)

                            else:
                                radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)
                                radial.setColorAt(0, QColor(255, 255, 255))
                                radial.setColorAt(1, QColor(255, 255, 255))
                                qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)

                        else:
                            radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)
                            radial.setColorAt(0, QColor(255, 255, 255))
                            radial.setColorAt(1, QColor(255, 255, 255))
                            qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)


        qp = QPainter()
        qp.begin(self)
        draw_map()
        draw_piecess()
        qp.end()

    def mouseMoveEvent(self, e):
        """鼠标移动追踪"""
        # 1.获取鼠标当前位置
        mouse_x = e.windowPos().x()
        mouse_y = e.windowPos().y()

        self.setMouseTracking(True)

        if (mouse_x % 40 <= 15 or mouse_x % 40 >= 25) and (mouse_y % 40 <= 15 or mouse_y % 40 >= 25):
            game_x = int((mouse_x + 15) // 40) - 1
            game_y = int((mouse_y + 15) // 40) - 1
            #判读鼠标位置的变化

            pos_change = False
            #if game_x != self.last_pos[0] or game_y != self.last_pos[1]:
            #     print("4")
            pos_change = True
            # 3.根据鼠标的位置变化，绘制标记
            if pos_change and game_x != -1:
                    self.setCursor(Qt.PointingHandCursor)
            if pos_change and game_x == -1:
                    self.setCursor(Qt.ArrowCursor)
            if pos_change and game_x != -1:
                    self.corner_widget.move(25 + game_x * 40, 25 + game_y * 40)
                    self.corner_widget.show()
            if pos_change and (game_x == -1 or game_x >14 or game_y <= -1 or game_y >14):
                    self.corner_widget.hide()


    @run_with_exc
    def mousePressEvent(self, e):

        """根据鼠标移动位置，确定落子"""
        if e.button() == Qt.LeftButton:
            # 1. 首先判断按下了那个格子
            mouse_x = e.windowPos().x()
            mouse_y = e.windowPos().y()

            if (mouse_x % 40 <= 15 or mouse_x % 40 >= 25) and (mouse_y % 40 <= 15 or mouse_y % 40 >=25):
                game_x = int((mouse_x + 15) // 40) - 1
                game_y = int((mouse_y + 15) // 40) - 1
            else:
                return
            self.g.move_lstep(True,game_x,game_y)

            # 2.根据操作结果进行一轮游戏循环
            res = self.g.game_result()
            if res != 0:
                self.timer.start(500)
                self.repaint(0,0,650,650)

                return
            self.g.ai_move_lstep()
            res = self.g.game_result()
            if res != 0:
                self.timer.start(500)
                self.repaint(0, 0, 650, 650)

                return
            self.repaint(0,0,650,650)#游戏未结束，重新绘制游戏界面
            #self.show(0)
    def game_restart(self,res):
        """游戏结束，重新开始游戏"""
        if res == 1:
                self.timer.stop()
                QMessageBox.about(self,"游戏结束","玩家获胜！")

        elif res == 2:
                self.timer.stop()
                QMessageBox.about(self,"游戏结束","电脑获胜！")

        elif res == 3:
            QMessageBox.about(self,"游戏结束","平局！")
        else:
            raise ValueError("游戏结束的标志必须为1、2或3")
        #游戏重新开始
        self.count = 0
        self.g = Comoku()
