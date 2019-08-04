#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@author: lianying
'''
import random

class Game:
    #init
    def __init__(self, size):
        self.size = size
        self.matrix = [[0]*self.size for i in range(self.size)]
    
    def start(self):

        #shallow copy  error
        #self.matrix = [[0]*self.size]*self.size
        self.add_random_num()
        self.display()
        while True:
            input=raw_input("Left(A/a),Right(D/d),Up(W/w),Down(D/d),Quit(S/s):")
            if input.lower() == 'a':
                self.slip_left() 
            elif input.lower() == 'd':
                self.slip_right() 
            elif input.lower() == 'w':
                self.slip_up() 
            elif input.lower() == 's':
                self.slip_down() 
            elif input.lower() == 'q':
                break
            else:
                print 'error input'
                continue
            if self.add_random_num():          
                self.display()
            else:
                print 'no place to generate new num'
                break
            #input=raw_input("Left(L/l),Right(R/d),Up(U/d),Down(D/d),Quit(Q/q):")
    
        print 'game over, the max num you get is %d' % self.get_max_num()
        
    #slip left 
    def slip_left(self):
        # move 0 to the tail
        for t_row in range(self.size):
            new_line = filter(lambda x:x != 0, self.matrix[t_row])
            new_line.extend([0] * (self.size - len(new_line)))
            self.matrix[t_row] = new_line
        #calculate
        for t_row in range(self.size):
            # list_b is a sign to the add action
            list_b = [0] * self.size
            for i in range(1, self.size):
                if self.matrix[t_row][i - 1] == self.matrix[t_row][i] and list_b[i - 1] != 1:
                    self.matrix[t_row][i - 1] = self.matrix[t_row][i - 1] * 2
                    list_b[i - 1] = 1
                    # the first el to iter is i
                    for j in range(i + 1, self.size):
                        self.matrix[t_row][j - 1] = self.matrix[t_row][j]
                        list_b[j - 1] = list_b[j]
                    # the last one is set to 0
                    self.matrix[t_row][self.size - 1] = 0
                    list_b[self.size - 1] = 0
                else:
                    pass
        return self.matrix
    #slip right 
    def slip_right(self):
        # move 0 to the front
        for t_row in range(self.size):
            new_line = filter(lambda x:x != 0, self.matrix[t_row])
            zero = [0] * (self.size - len(new_line))
            zero.extend(new_line)
            self.matrix[t_row] = zero
        #calculate
        for t_row in range(self.size):
            # list_b is a sign to the add action
            list_b = [0] * self.size
            for i in range(self.size - 1, 0, -1):
                if self.matrix[t_row][i - 1] == self.matrix[t_row][i] and list_b[i] != 1:
                    self.matrix[t_row][i] = self.matrix[t_row][i ] * 2
                    list_b[i] = 1
                    # the first el to iter is i
                    for j in range(i - 1, 0, -1):
                        self.matrix[t_row][j] = self.matrix[t_row][j - 1]
                        list_b[j] = list_b[j - 1]
                    self.matrix[t_row][0] = 0
                    list_b[0] = 0
                else:
                    pass
        return self.matrix
    #slip up 
    def slip_up(self):
        # move 0 to the bottom
        for t_col in range(self.size):
            col_line = [self.matrix[x][t_col] for x in range(self.size)]
            new_line = filter(lambda x:x != 0, col_line)
            zero = [0] * (self.size - len(new_line))
            new_line.extend(zero)
            for x in range(self.size):
                self.matrix[x][t_col] = new_line[x]
            
        for t_col in range(self.size):
            # list_b is a sign to the add action
            list_b = [0] * self.size
            for i in range(1, self.size):
                if self.matrix[i - 1][t_col] == self.matrix[i][t_col] and list_b[i] != 1:
                    self.matrix[i - 1][t_col] = self.matrix[i - 1][t_col] * 2
                    list_b[i - 1] = 1
                    # the first el to iter is i
                    for j in range(i + 1, self.size):
                        self.matrix[j - 1][t_col] = self.matrix[j][t_col]
                        list_b[j - 1] = list_b[j]
                    # the last one is set to 0
                    self.matrix[self.size - 1][t_col] = 0
                    list_b[self.size - 1] = 0
                else:
                    pass
        return self.matrix
    #slip down
    def slip_down(self):
        # move 0 to the top
        for t_col in range(self.size):
            col_line = [self.matrix[x][t_col] for x in range(self.size)]
            new_line = filter(lambda x:x != 0, col_line)
            zero = [0] * (self.size - len(new_line))
            zero.extend(new_line)
            for x in range(self.size):
                self.matrix[x][t_col] = zero[x]
                
        for t_col in range(self.size):
            list_b = [0] * self.size
            for i in range(self.size - 1, 0, -1):
                if self.matrix[i -1][t_col] == self.matrix[i][t_col] and list_b[i] != 1:
                    self.matrix[i][t_col] = self.matrix[i][t_col] * 2
                    list_b[i] = 1
                    for j in range(i - 1, 0, -1):
                        self.matrix[j][t_col] = self.matrix[j - 1][t_col]
                        list_b[j] = list_b[j - 1]
                    self.matrix[0][t_col] = 0
                    list_b[0] = 0
                else:
                    pass
        return self.matrix
    #add a new num in matrix where is 0   
    def add_random_num(self):
        zero_list = []
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == 0:
                    zero_list.append(i*self.size +j)         
        if len(zero_list) > 0:
            #get a random position--->random.choice(iterable)
            pos = random.choice(zero_list)
            num = random.choice([2,2,2,4])
            self.matrix[pos / self.size][pos % self.size] = num 
            return True
        else:
            return False
    #display the chess
    def display(self):
        print "The Chess is:\n"
        for i in range(self.size):
            for j in range(self.size):
                print '%4d' % self.matrix[i][j],
            print '\n',
    #get the max num in the chess
    def get_max_num(self): 
        return max([max(self.matrix[i]) for i in range(self.size)]) 
def main():
    print 'Welcome to the 2048 game:'
    while True:
        try:
            size = int(raw_input('choose the size you want:'))
            if size > 2:
                game = Game(size)
                game.start()
                break
            else:
                print 'the num should greater than 2'
        except:
            print 'wrong input!'

      
if __name__ == '__main__':
    main()