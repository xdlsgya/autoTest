# ord(c)  返回对应的十进制整数  ord(‘a’)  —>97
# dict(key/value) 创建一个字典
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# keyboard    键盘监听模块
# getch()方法返回一个整数;输入字符，无需回车，如果它在0到255之间，它表示按下的键的ASCII码。大于255的值是特殊键，例如Page Up，Home或光标键。您可以比较回到常量，如价值curses.KEY_PPAGE， curses.KEY_HOME或curses.KEY_LEFT。
# randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1
# choice(a)  返回a中的一个随机项，a可以是列表，元组或字符串



def main(stdscr):

    def init():
        #重置游戏棋盘
        return 'Game'

    def not_game(state):
        #画出 GameOver 或者 Win 的界面
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        responses = defaultdict(lambda: state) ＃默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit' #对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        #画出当前棋盘状态
        #读取用户输入得到action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #if 成功移动了一步:
            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    state = 'Init'

    #状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()


def get_user_action(keyboard):    
    char = "N"
    while char not in actions_dict:    
        char = keyboard.getch()
    return actions_dict[char]


# 矩阵转置：正序返回
def transpose(field):
    return [list(row) for row in zip(*field)]


# 矩阵逆转（不是逆矩阵）：逆序返回
def invert(field):
    return [row[::-1] for row in field]



# 初始化棋盘的参数，可以指定棋盘的高和宽以及游戏胜利条件，默认是最经典的 4x4～2048。
    class GameField(object):
        def __init__(self, height=4, width=4, win=2048):
            self.height = height       #高
            self.width = width         #宽
            self.win_value = 2048      #过关分数
            self.score = 0             #当前分数
            self.highscore = 0         #最高分
            self.reset()               #棋盘重置

# 随机生成一个 2 或者 4
def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element
# 重置棋盘
def reset(self):
    if self.score > self.highscore:
        self.highscore = self.score
    self.score = 0
    self.field = [[0 for i in range(self.width)] for j in range(self.height)]
    self.spawn()
    self.spawn()


# 一行向左合并
# (注：这一操作是在 move 内定义的，拆出来是为了方便阅读)
def move_row_left(row):
    def tighten(row): # 把零散的非零单元挤到一块
        new_row = [i for i in row if i != 0]
        new_row += [0 for i in range(len(row) - len(new_row))]
        return new_row

    def merge(row): # 对邻近元素进行合并 [4,2,2,0]
        pair = False
        new_row = []
        for i in range(len(row)):
            if pair:
                new_row.append(2 * row[i])
                self.score += 2 * row[i]
                pair = False
            else:
                if i + 1 < len(row) and row[i] == row[i + 1]:
                    pair = True
                    new_row.append(0)
                else:
                    new_row.append(row[i])
        assert len(new_row) == len(row)
        return new_row
    #先挤到一块再合并再挤到一块
    return tighten(merge(tighten(row)))




# 棋盘走一步
# 通过对矩阵进行转置与逆转，可以直接从左移得到其余三个方向的移动操作

def move(self, direction):
    def move_row_left(row):
        #一行向左合并

        moves = {}
        moves['Left']  = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up']    = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down']  = lambda field: transpose(moves['Right'](transpose(field)))

    if direction in moves:
        if self.move_is_possible(direction):
            self.field = moves[direction](self.field)
            self.spawn()
            return True
        else:
            return False
#判断输赢
def is_win(self):
    return any(any(i >= self.win_value for i in row) for row in self.field)

def is_gameover(self):
    return not any(self.move_is_possible(move) for move in actions)

#判断能否移动
def move_is_possible(self, direction):
    def row_is_left_movable(row): 
        def change(i):
            if row[i] == 0 and row[i + 1] != 0: # 可以移动
                return True
            if row[i] != 0 and row[i + 1] == row[i]: # 可以合并
                return True
            return False
        return any(change(i) for i in range(len(row) - 1))

    check = {}
    check['Left']  = lambda field: any(row_is_left_movable(row) for row in field)

    check['Right'] = lambda field: check['Left'](invert(field))

    check['Up']    = lambda field: check['Left'](transpose(field))

    check['Down']  = lambda field: check['Right'](transpose(field))

    if direction in check:
        return check[direction](self.field)
    else:
        return False




#绘制游戏界面
def draw(self, screen):
    help_string1 = '(W)Up (S)Down (A)Left (D)Right'
    help_string2 = '     (R)Restart (Q)Exit'
    gameover_string = '           GAME OVER'
    win_string = '          YOU WIN!'
    def cast(string):
        screen.addstr(string + '\n')

    #绘制水平分割线
    def draw_hor_separator():
        line = '+' + ('+------' * self.width + '+')[1:]
        separator = defaultdict(lambda: line)
        if not hasattr(draw_hor_separator, "counter"):
            draw_hor_separator.counter = 0
        cast(separator[draw_hor_separator.counter])
        draw_hor_separator.counter += 1

    def draw_row(row):
        cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

    screen.clear()

    cast('SCORE: ' + str(self.score))
    if 0 != self.highscore:
        cast('HIGHSCORE: ' + str(self.highscore))

    for row in self.field:
        draw_hor_separator()
        draw_row(row)

    draw_hor_separator()

    if self.is_win():
        cast(win_string)
    else:
        if self.is_gameover():
            cast(gameover_string)
        else:
            cast(help_string1)
    cast(help_string2)


