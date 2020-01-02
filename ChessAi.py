from PyQt5.QtCore import QTimer
#from Game.game import Comoku
import copy

#class game():
#    g_map = [[0 for x in range(15)] for y in range(15)]#导入游戏棋盘数据

class ChessAi():

    def __init__(self):
        self.Aicoordinate = (0,0)
        self.Aicode = 0
        self.Opcoordinate = (0,0)
        self.Opcode = 0
        #self.g = Comoku()
    def FindBestMove(self,g_map):
        """获取最佳下棋位置"""
        DecisionCoordinate = ((0,0))
        self.Aicoordinate = (0, 0)
        self.Aicode = 0
        self.Opcoordinate = (0, 0)
        self.Opcode = 0
        for x in range(15):
            for y in range(15):
                if g_map[x][y] == 0:
                    recode = self.Evaluation(2, g_map, x, y)
                    if  recode > self.Aicode:
                        self.Aicode = recode
                        self.Aicoordinate = (x,y)
        suppose_map = copy.deepcopy(g_map)
        suppose_map[self.Aicoordinate[0]][self.Aicoordinate[1]] = 2

        for a in range(15):
            for b in range(15):
                if suppose_map[a][b] == 0:
                    opcode = self.Evaluation(1,suppose_map,a,b)
                    if opcode > self.Opcode:
                        self.Opcode = opcode
                        self.Opcoordinate = (a,b)
        print("Aicode = %d"%self.Aicode,end='')
        print(self.Aicoordinate)
        print("Opcode = %d "%self.Opcode,end='')
        print(self.Opcoordinate)
        if self.Aicode <= self.Opcode and g_map[self.Opcoordinate[0]][self.Opcoordinate[1]] == 0:
            self.Aicoordinate = self.Opcoordinate

        return self.Aicoordinate
        def GetDecisionCoordinate():
            """获取决策坐标"""
            for i in range(15):
                for j in range(15):
                    # 1.不在边缘
                    if i > 0 and i < 14 and j > 0 and j < 14:
                        if self.g.g_map[i][j] == 0 and (self.g.g_map[i + 1][j + 1] != 0 or self.g.g_map[i + 1][j] != 0 or \
                                                        self.g.g_map[i][j + 1] != 0 or self.g.g_map[i+ 1][j - 1] != 0 or \
                                                        self.g.g_map[i][j - 1] != 0 or self.g.g_map[i - 1][j - 1] != 0):
                            pass

            pass
        def CreateTree():
            """创建决策树"""
            pass
        def max():
            pass
        def min():
            pass
    def  Evaluation(self,true,current_map,x,y):
        """评估函数"""
        Evaluation_Criteria = {"眠2":1,"活2":10,"眠3":100,"冲4":1000,"活3":10000,"活4":100000,"连5":1000000}
        suppose_map = copy.deepcopy(current_map)
        suppose_map[x][y] = true

        code = 0
        if true == 1:
            opponent = 2
        else:
            opponent = 1
        #"""5连判断"""
        for i in range(11):
            for j in range(11):
                #"""横向判断"""
                if suppose_map[i][j] == true and suppose_map[i + 1][j] == true and suppose_map[i + 2][j] == true and suppose_map[i + 3][j] == true and suppose_map[i + 4][j] == true:
                    code += Evaluation_Criteria["连5"]

                #"""纵向判断"""
                if suppose_map[i][j] == true and suppose_map[i][j + 1] == true and suppose_map[i][j + 2] == true and suppose_map[i][j + 3] == true and suppose_map[i][j + 4] == true:
                    code += Evaluation_Criteria["连5"]
                #"""左上----右下"""
                if suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == true and suppose_map[i + 2][j + 2] == true and suppose_map[i + 3][j + 3] == true and suppose_map[i + 4][j + 4] == true:
                    code += Evaluation_Criteria["连5"]
                #"""左下----右上"""
                if suppose_map[i + 4][j] == true and suppose_map[i + 3][j + 1] == true and suppose_map[i + 2][j + 2] == true and suppose_map[i + 1][j + 3] == true and suppose_map[i][j + 4] == true:
                    code += Evaluation_Criteria["连5"]

        #"""连续4连判断"""
        for i in range(12):
            for j in range(12):
                #"""横向判断"""
                if suppose_map[i][j] == true and suppose_map[i + 1][j] == true and suppose_map[i + 2][j] == true and suppose_map[i + 3][j] == true:
                    # 1.不在棋盘边缘
                    if i > 0 and i < 11:
                        if suppose_map[i - 1][j] == 0 and suppose_map[i + 4][j] == 0:
                            code += Evaluation_Criteria["活4"]
                        elif (suppose_map[i -1][j] == opponent and suppose_map[i + 4][j] == 0) or (suppose_map[i -1][j] == 0 and suppose_map[i + 4][j] == opponent):
                            code += Evaluation_Criteria["冲4"]
                        else  :#无意义
                            code += 0
                    # 2.在棋盘左边边缘
                    elif i == 0:
                        if suppose_map[i + 4][j] == 0:
                            code += Evaluation_Criteria["冲4"]

                    # 3.在棋盘右边边缘
                    elif i == 11:
                        if suppose_map[i - 1][j] == 0:
                            code +=Evaluation_Criteria["冲4"]

                #"""纵向判断"""
                if suppose_map[i][j] == true and suppose_map[i][j + 1] == true and suppose_map[i][j + 2] == true and suppose_map[i][j + 3] == true:
                    # 1.不在棋盘边缘
                    if j > 0 and j < 11:
                        if suppose_map[i][j - 1] == 0 and suppose_map[i][j + 4] == 0:
                            code += Evaluation_Criteria["活4"]
                        elif (suppose_map[i][j - 1] == 0 and suppose_map[i][j + 4] == opponent) or (suppose_map[i][j - 1] == opponent and suppose_map[i][j + 4] == 0):
                            code += Evaluation_Criteria["冲4"]
                        else:
                            code += 0
                    # 2. 在棋盘上边边缘
                    elif j == 0:
                        if suppose_map[i][j + 4] == 0:
                            code += Evaluation_Criteria["冲4"]

                    elif j == 11:
                        if suppose_map[i][j - 1] == 0:
                            code += Evaluation_Criteria["冲4"]

                #"""左上----右下判断"""
                if suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == true and suppose_map[i + 2][j + 2] == true and suppose_map[i + 3][j + 3]== true:
                    # 1.不在边缘
                    if i > 0 and i < 11 and j > 0and j < 11:
                        if suppose_map[i - 1][j - 1] == true and suppose_map[i + 4][j + 4] == true:
                            code += Evaluation_Criteria["活4"]
                        elif suppose_map[i - 1][j - 1] == opponent and suppose_map[i + 4][j + 4] == opponent:
                            code += 0
                        else:
                            code +=Evaluation_Criteria["冲4"]
                    # 2.在左上角
                    elif (i == 0 and j < 11) or (i < 11 and j == 0):
                        if suppose_map[i + 4][j + 4] == 0:
                            code += Evaluation_Criteria["冲4"]

                    # 3.在右下角
                    elif (i == 11 and j > 3) or (i > 0 and j == 11):
                        if suppose_map[i - 1][j - 1] == 0:
                            code += Evaluation_Criteria["冲4"]

                #"""左下----右上判断"""
                if suppose_map[i + 3][j] == true and suppose_map[i + 2][j + 1] == true and suppose_map[i + 1][j + 2] == true and suppose_map[i][j + 3] == true:
                    # 1.不在边缘
                    if i > 0 and i < 11 and j < 11  and j > 0:
                        if suppose_map[i + 4][j - 1] == 0 and suppose_map[i - 1][ j + 4] == 0:
                            code += Evaluation_Criteria["活4"]
                        elif suppose_map[i + 4][j - 1] == opponent and suppose_map[i - 1][i + 4] == opponent:
                            code += 0
                        else:
                            code += Evaluation_Criteria["冲4"]
                    # 2.在左下角
                    elif (i == 0 and j > 3) or (i < 11 and j == 11):
                        if suppose_map[i + 4][j - 1] == 0:
                            code += Evaluation_Criteria["冲4"]

                    # 3.在右上角
                    elif (i > 3 and j == 3) or (i == 11 and j < 11):
                        if suppose_map[i - 1][j + 4] == 0:
                            code += Evaluation_Criteria["冲4"]
        #"""非连续4连判断"""
        for i in range(11):
            for j in range(11):
                #"""横向判断"""
                if (suppose_map[i][j] == true and suppose_map[i + 1][j] == 0 and suppose_map[i + 2][j] == true and suppose_map[i + 3][j] == true and suppose_map[i + 4][j] == true )or \
                   (suppose_map[i][j] == true and suppose_map[i + 1][j] == true and suppose_map[i + 2][j] == 0 and suppose_map[i + 3][j] == true and suppose_map[i + 4][j] == true ) or \
                       (suppose_map[i][j] == true and suppose_map[i + 1][j] == true and suppose_map[i + 2][j] == true and suppose_map[i + 3][j] == 0 and suppose_map[i + 4][j] == true ):
                        code += (Evaluation_Criteria["冲4"] - Evaluation_Criteria["眠3"] - Evaluation_Criteria["眠2"])# 避免眠3 ，眠2 重复计算
                #"""纵向判断"""
                if (suppose_map[i][j] == true and suppose_map[i][j + 1] == 0 and suppose_map[i][j + 2] == true and suppose_map[i][j + 3] == true and suppose_map[i][j + 4] == true)or \
                    (suppose_map[i][j] == true and suppose_map[i][j + 1] == true and suppose_map[i][j + 2] == 0 and suppose_map[i][j + 3] == true and suppose_map[i][j + 4] == true)or \
                   (suppose_map[i][j] == true and suppose_map[i][j + 1] == true and suppose_map[i][j + 2] == true and suppose_map[i][j + 3] == 0 and suppose_map[i][j + 4] == true):
                        code += (Evaluation_Criteria["冲4"] - Evaluation_Criteria["眠3"] - Evaluation_Criteria["眠2"])# 避免眠3 ，眠2 重复计算
                #"""左上----右下"""
                if (suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == 0 and suppose_map[i + 2][j + 2] == true and suppose_map[i + 3][j + 3] == true and suppose_map[i + 4][j + 4] == true)or \
                   (suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == true and suppose_map[i + 2][j + 2] == 0 and suppose_map[i + 3][j + 3] == true and suppose_map[i + 4][j + 4] == true)or \
                       (suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == true and suppose_map[i + 2][j + 2] == true and suppose_map[i + 3][j + 3] == 0 and suppose_map[i + 4][j + 4] == true):
                        code += (Evaluation_Criteria["冲4"] - Evaluation_Criteria["眠3"] - Evaluation_Criteria["眠2"])# 避免眠3 ，眠2 重复计算
                #"""左下----右上"""
                if (suppose_map[i + 4][j] == true and suppose_map[i + 3][j + 1] == 0 and suppose_map[i + 2][j + 2] == true and suppose_map[i + 1][j + 3] == true and suppose_map[i][j + 4] == true)or \
                   (suppose_map[i + 4][j] == true and suppose_map[i + 3][j + 1] == true and suppose_map[i + 2][j + 2] == 0 and suppose_map[i + 1][j + 3] == true and suppose_map[i][j + 4] == true)or \
                   (suppose_map[i + 4][j] == true and suppose_map[i + 3][j + 1] == true and suppose_map[i + 2][j + 2] == true and suppose_map[i + 1][j + 3] == 0 and suppose_map[i][j + 4] == true):
                        code += (Evaluation_Criteria["冲4"] - Evaluation_Criteria["眠3"] - Evaluation_Criteria["眠2"])# 避免眠3 ，眠2 重复计算

        #"""连续3连判断"""
        for i in range(13):
            for j in range(13):
                #"""横向判断"""
                if suppose_map[i][j] == true and suppose_map[i + 1][j] == true and suppose_map[i + 2][j] == true:
                    # 1.不在边缘
                    if i > 0 and j > 0 and i < 12 and j < 12:
                        if suppose_map[i - 1][j] == 0 and suppose_map[i + 3][j] == 0:
                            code += Evaluation_Criteria["活3"]
                        elif suppose_map[i - 1][j] == opponent and suppose_map[i + 3][j] == opponent:
                            code += 0
                        else:
                            code += Evaluation_Criteria["眠3"]
                    # 2.在左边
                    elif i == 0 :
                        if suppose_map[i + 3][j] == 0:
                            code += Evaluation_Criteria["眠3"]

                    # 3.在右边
                    elif i == 12:
                        if suppose_map[i - 1][j] == 0:
                            code += Evaluation_Criteria["眠3"]

                #"""纵向判断"""
                if suppose_map[i][j] == true and suppose_map[i][j + 1] == true and suppose_map[i][j + 2] == true:
                    # 1.不在边缘
                    if i > 0 and j > 0 and i < 12 and j < 12:
                        if suppose_map[i][j - 1] == 0 and suppose_map[i][j + 3] == 0:
                            code += Evaluation_Criteria["活3"]
                        elif suppose_map[i][j - 1] == opponent and suppose_map[i][j + 3] == opponent:
                            code += 0
                        else:
                            code += Evaluation_Criteria["眠3"]
                    # 2.在上边
                    elif j == 0:
                        if suppose_map[i][j + 3] == 0:
                            code += Evaluation_Criteria["眠3"]
                        else:
                            code += 0
                    # 3.在下边
                    elif j == 12:
                        if suppose_map[i][j - 1] == 0:
                            code += Evaluation_Criteria["眠3"]

                #"""左上----右下"""
                if suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == true and suppose_map[i + 2][j + 2] == true:
                    # 1.不在边缘
                        if i > 0 and i < 12 and j > 0 and j < 12:
                            if suppose_map[i - 1][j -1] == 0 and suppose_map[i + 3][j + 3] == 0:
                                code += Evaluation_Criteria["活3"]
                            elif suppose_map[i - 1][j - 1] == opponent and suppose_map[i + 3][j + 3] == true:
                                code += 0
                            else:
                                code += Evaluation_Criteria["眠3"]
                    # 2. 在左上角
                        elif (i == 0 and j < 12) or (i < 12 and j == 0):
                            if suppose_map[i + 3][j + 3] == 0:
                                code += Evaluation_Criteria["眠3"]

                    # 3.在右下角
                        elif (i > 2 and j == 12) or (i == 12 and j > 2):
                            if suppose_map[i - 1][j - 1] == 0:
                                code += Evaluation_Criteria["眠3"]

                #"""左下----右上"""
                if suppose_map[i + 2][j] == true and  suppose_map[i + 1][j + 1] == true and suppose_map[i][j + 2] ==true:
                    # 1.不在边缘
                    if (j == 0 and i > 2) or (i == 12 and j < 12):
                        if suppose_map[i - 1][j + 3] == 0 and suppose_map[i + 3][j - 1] == 0:
                            code += Evaluation_Criteria["活3"]
                        elif suppose_map[i - 1][j + 3] == opponent and suppose_map[i + 3][j - 1] == opponent:
                            code += 0
                        else:
                            code += Evaluation_Criteria["眠3"]
                    # 2.在左下角
                    elif (i == 0 and j > 2) or (j == 12 and i < 12):
                        if suppose_map[i + 3][ j -1] == 0:
                            code += Evaluation_Criteria["眠3"]
                    # 3.在右上角
                    elif (i > 2 and j == 0) or (i == 12 and j < 12):
                        if suppose_map[i - 1][j + 3] == 0:
                            code += Evaluation_Criteria["眠3"]
        #"""非连续3连判断"""
        for i in range(12):
            for j in range(12):
                #"""横向判断"""
                if (suppose_map[i][j] == true and suppose_map[i + 1][j] == 0 and suppose_map[i + 2][j] == true and suppose_map[i + 3][j] == true)or \
                   (suppose_map[i][j] == true and suppose_map[i + 1][j] == true and suppose_map[i + 2][j] == 0 and suppose_map[i + 3][j] == true):
                    code += Evaluation_Criteria["眠3"] - Evaluation_Criteria["眠2"]
                #"""纵向判断"""
                if (suppose_map[i][j] == true and suppose_map[i][j + 1] == true and suppose_map[i][j + 2] == 0 and suppose_map[i][j + 3] == true)or \
                   (suppose_map[i][j] == true and suppose_map[i][j + 1] == 0 and suppose_map[i][j + 2] == true and suppose_map[i][j + 3] == true):
                    code += Evaluation_Criteria["眠3"] - Evaluation_Criteria["眠2"]
                #"""左上----右下"""
                if (suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == 0 and suppose_map[i + 2][j + 2] == true and suppose_map[i + 3][j + 3] == true)or \
                   (suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == true and suppose_map[i + 2][j + 2] == 0 and suppose_map[i + 3][j + 3] == true):
                    code += Evaluation_Criteria["眠3"] - Evaluation_Criteria["眠2"]
                #"""左下----右上"""
                if (suppose_map[i + 3][j] == true and suppose_map[i + 2][j + 1] == 0 and suppose_map[i + 1][j + 2] == true and suppose_map[i][j + 3] == true ) or \
                   (suppose_map[i + 3][j] == true and suppose_map[i + 2][j + 1] == true and suppose_map[i + 1][j + 2] == 0 and suppose_map[i][j + 3] == true):
                    code += Evaluation_Criteria["眠3"] - Evaluation_Criteria["眠2"]

        #"""连续2连判断"""
        for i in range(14):
            for j in range(14):
                #"""横向判断"""
                if suppose_map[i][j] == true and suppose_map[i + 1][j] == true:
                    # 1.不在边缘
                    if i > 0 and i < 13:
                        if suppose_map[i - 1][j] == 0 and suppose_map[i + 2][j] == 0:
                            code += Evaluation_Criteria["活2"]
                        elif suppose_map[i - 1][j] == opponent and suppose_map[i + 2] == opponent:
                            code += 0
                        else:
                            code += Evaluation_Criteria["眠2"]
                    # 2.在左边
                    elif i == 0:
                        if suppose_map[i + 2][j] == 0:
                            code += Evaluation_Criteria["眠2"]

                    # 3.在右边
                    elif i == 13:
                        if suppose_map[i - 1][j] == 0:
                            code += Evaluation_Criteria["眠2"]

                #"""纵向判断"""
                if suppose_map[i][j] == true and suppose_map[i][j + 1] == true:
                    # 1. 不在边缘
                    if j > 0 and j < 13:
                        if suppose_map[i][j - 1] == 0 and suppose_map[i][j + 2] == 0:
                            code += Evaluation_Criteria["活2"]
                        elif suppose_map[i][j - 1] == opponent and suppose_map[i][j + 2] == opponent:
                            code += 0
                        else:
                            code += Evaluation_Criteria["眠2"]
                    # 2. 在上边
                    elif j == 0:
                        if suppose_map[i][j + 2] == 0:
                            code += Evaluation_Criteria["眠2"]

                    # 3.在下边
                    elif j == 13:
                        if suppose_map[i][j - 1] == 0:
                            code += Evaluation_Criteria["眠2"]

                #"""左上----右下"""
                if suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == true:
                    # 1.不在边缘
                    if i > 0 and j < 13 and i < 13 and j > 0:
                        if suppose_map[i - 1][j - 1] == 0 and suppose_map[i + 2][j + 2] == 0:
                            code += Evaluation_Criteria["活2"]
                        elif suppose_map[i - 1][j - 1] == opponent and suppose_map[i + 2][j + 2] == 0:
                            code += 0
                        else:
                            code += Evaluation_Criteria["眠2"]
                    # 2.在左上角
                    elif (j == 0 and i < 13) or (i == 0 and j < 13):
                        if suppose_map[i + 2][j + 2] == 0:
                            code += Evaluation_Criteria["眠2"]

                    # 3.在右下角
                    elif (i == 13 and j > 2) or (i > 2 and j == 13):
                        if suppose_map[i - 1][j - 1] == 0:
                            code += Evaluation_Criteria["眠2"]

                #"""左下----右上"""
                if suppose_map[i + 1][j] == true and suppose_map[i][j + 1] == 0:
                    # 1.不在边缘
                    if i > 0 and j > 0 and j < 13 and i < 13:
                        if suppose_map[i - 1][j + 2] == 0 and suppose_map[i + 2][j - 1] == 0:
                            code += Evaluation_Criteria["活2"]
                        elif suppose_map[i - 1][j + 2] == opponent and suppose_map[i + 2][j - 1] == opponent:
                            code += 0
                        else:
                            code += Evaluation_Criteria["眠2"]
                    # 2.在左下角
                    elif (i == 0 and j > 1) or (i < 13 and j == 13):
                        if suppose_map[i + 2][j - 1] == 0:
                            code += Evaluation_Criteria["眠2"]
                    # 3.在右上角
                    elif (i > 1 and j == 0) or (i == 13 and j < 13):
                        if suppose_map[i - 1][j + 2] == 0:
                            code += Evaluation_Criteria["眠2"]
        #"""非连续2连判断"""
        for i in range(13):
            for j in range(13):
                # 1.横向判断
                if (suppose_map[i][j] == true and suppose_map[i + 1][j] == 0 and suppose_map[i + 2][j] == true):
                    code += Evaluation_Criteria["眠2"]
                # 2.纵向判断
                elif (suppose_map[i][j] == true and suppose_map[i][j + 1] == 0 and suppose_map[i][j + 2] == true):
                    code += Evaluation_Criteria["眠2"]
                # 3.左上----右下
                elif (suppose_map[i][j] == true and suppose_map[i + 1][j + 1] == 0 and suppose_map[i + 2][j + 2] == true):
                    code += Evaluation_Criteria["眠2"]
                # 4.左下----右上
                elif (suppose_map[i + 2][j] == true and suppose_map[i + 1][j + 1] == true and suppose_map[i][j + 2] == true):
                    code += Evaluation_Criteria["眠2"]
        return code












