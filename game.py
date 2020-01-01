from Game.ChessAi import ChessAi

class Comoku:

    def __init__(self):
        self.g_map = [[0 for y in range(15)] for x in range(15)]
        self.cur_step = 0 #步数
        self.result = 3
        self.ChessAi = ChessAi()

    def move_lstep(self,input_by_window = True,pos_x = None,pos_y = None):
        """玩家落子"""
        while True:
            try:
                if not input_by_window:
                    pos_x = int(input("x: "))
                    pos_y = int(input("y: "))
                if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:
                    if self.g_map[pos_x][pos_y] == 0:
                        self.g_map[pos_x][pos_y] = 1
                        self.cur_step += 1
                        return
            except ValueError:
                continue

    def game_result(self):
        """判断游戏结局:1.玩家胜利 2.电脑胜利 3.平局"""
        # 1.判断是否有横向5连珠
        for x in range(11):
            for y in range(11):
                if self.g_map[x][y + 4] == 1 and self.g_map[x][y + 3] == 1 and self.g_map[x][y + 2] == 1 and self.g_map[x][y + 1] == 1 and self.g_map[x][y + 0] == 1:
                    self.result = 1
                    return 1
                if self.g_map[x][y + 4] == 2 and self.g_map[x][y + 3] == 2 and self.g_map[x][y + 2] == 2 and self.g_map[x][y + 1] == 2 and self.g_map[x][y + 0] == 2:
                    self.result = 2
                    return 2
        # 2.判断纵向是否有5连珠
        for x in range(11):
            for y in range(11):
                if self.g_map[x + 4][y] == 1 and self.g_map[x + 3][y] == 1 and self.g_map[x + 2][y] == 1 and self.g_map[x + 1][y] == 1 and self.g_map[x + 0][y] == 1:
                    self.result = 1
                    return 1
                if self.g_map[x + 4][y] == 2 and self.g_map[x + 3][y] == 2 and self.g_map[x + 2][y] == 2 and self.g_map[x + 1][y] == 2 and self.g_map[x + 0][y] == 2:
                    self.result = 2
                    return 2
        # 3.判断左上--右下是否有5连珠
        for x in range(11):
            for y in range(11):
                if self.g_map[x][y] == 1 and self.g_map[x + 1][y + 1] == 1 and self.g_map[x + 2][y + 2] == 1 and self.g_map[x + 3][y + 3] == 1 and self.g_map[x + 4][y + 4] == 1:
                    self.result = 1
                    return 1
                if self.g_map[x][y] == 2 and self.g_map[x + 1][y + 1] == 2 and self.g_map[x + 2][y + 2] == 2 and self.g_map[x + 3][y + 3] == 2 and self.g_map[x + 4][y + 4] == 2:
                    self.result = 2
                    return 2
        # 4.判断是否有左下--右上有5连珠

        for x in range(11):
            for y in range(11):
                if self.g_map[x + 4][y] == 1 and self.g_map[x + 3][y + 1] == 1 and self.g_map[x + 2][y + 2] == 1 and self.g_map[x + 1][y + 3] == 1 and self.g_map[x][y + 4] == 1:
                    self.result = 1
                    return 1
                if self.g_map[x + 4][y] == 2 and self.g_map[x + 3][y + 1] == 2 and self.g_map[x + 2][y + 2] == 2 and self.g_map[x + 1][y + 3] == 2 and self.g_map[x][y + 4] == 2:
                    self.result = 2
                    return 2

        # 5.判断是否为平局
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:
                    return 0
        return 3

    def ai_move_lstep(self):
        """电脑落子
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:
                    self.g_map[x][y] = 2
                    self.cur_step += 1
                    return

        """
        BestCoordinate = self.ChessAi.FindBestMove(self.g_map)

        self.g_map[BestCoordinate[0]][BestCoordinate[1]] = 2
        self.cur_step += 1

        return

    def getWinnerStep(self):
        # 1.判断是否有横向5连珠
        for x in range(11):
            for y in range(11):
                if self.g_map[x][y + 4] == 1 and self.g_map[x][y + 3] == 1 and self.g_map[x][y + 2] == 1 and \
                        self.g_map[x][y + 1] == 1 and self.g_map[x][y + 0] == 1:
                    return (x,y),(x,y+1),(x,y+2),(x,y+3),(x,y+4)
                if self.g_map[x][y + 4] == 2 and self.g_map[x][y + 3] == 2 and self.g_map[x][y + 2] == 2 and \
                        self.g_map[x][y + 1] == 2 and self.g_map[x][y + 0] == 2:
                    return (x,y),(x,y+1),(x,y+2),(x,y+3),(x,y+4)
        # 2.判断纵向是否有5连珠
        for x in range(11):
            for y in range(11):
                if self.g_map[x + 4][y] == 1 and self.g_map[x + 3][y] == 1 and self.g_map[x + 2][y] == 1 and \
                        self.g_map[x + 1][y] == 1 and self.g_map[x + 0][y] == 1:
                    return (x,y),(x+1,y),(x+2,y),(x+3,y),(x+4,y)
                if self.g_map[x + 4][y] == 2 and self.g_map[x + 3][y] == 2 and self.g_map[x + 2][y] == 2 and \
                        self.g_map[x + 1][y] == 2 and self.g_map[x + 0][y] == 2:
                    return (x,y),(x+1,y),(x+2,y),(x+3,y),(x+4,y)
        # 3.判断左上--右下是否有5连珠
        for x in range(11):
            for y in range(11):
                if self.g_map[x][y] == 1 and self.g_map[x + 1][y + 1] == 1 and self.g_map[x + 2][y + 2] == 1 and \
                        self.g_map[x + 3][y + 3] == 1 and self.g_map[x + 4][y + 4] == 1:
                    return (x,y),(x+1,y+1),(x+2,y+2),(x+3,y+3),(x+4,y+4)
                if self.g_map[x][y] == 2 and self.g_map[x + 1][y + 1] == 2 and self.g_map[x + 2][y + 2] == 2 and \
                        self.g_map[x + 3][y + 3] == 2 and self.g_map[x + 4][y + 4] == 2:
                    return (x,y),(x+1,y+1),(x+2,y+2),(x+3,y+3),(x+4,y+4)
        # 4.判断是否有左下--右上有5连珠

        for x in range(11):
            for y in range(11):
                if self.g_map[x + 4][y] == 1 and self.g_map[x + 3][y + 1] == 1 and self.g_map[x + 2][y + 2] == 1 and \
                        self.g_map[x + 1][y + 3] == 1 and self.g_map[x][y + 4] == 1:
                    return (x+4,y),(x+3,y+1),(x+2,y+2),(x+1,y+3),(x,y+4)
                if self.g_map[x + 4][y] == 2 and self.g_map[x + 3][y + 1] == 2 and self.g_map[x + 2][y + 2] == 2 and \
                        self.g_map[x + 1][y + 3] == 2 and self.g_map[x][y + 4] == 2:
                    return (x+4,y),(x+3,y+1),(x+2,y+2),(x+1,y+3),(x,y+4)
        return None

    def play(self):
        while True:
            self.move_lstep()
            res = self.game_result()
            if res != 0:
                self.show(res)
                return
            self.ai_move_lstep()
            res = self.game_result()
            if res != 0:
                self.show(res)
                return
            self.show(0)