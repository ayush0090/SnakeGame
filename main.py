import keyboard
import random
import time
import os


class SnakeGame:
    snake = []
    boundry_length = 30
    boundry_width = 30
    head_coords = []
    snake_body_array = []
    snake_head_chr = "O"
    snake_tail_chr = "o"
    snake_chr = "#"
    snake_direction = [1, 0]
    score = 0
    game_over = False
    egg_coords = []
    sleep_time = 0.3

    def __init__(self):
        for i in range(30):
            self.snake.append([])
            for j in range(30):
                self.snake[i].append(" ")
        
        self.snake[2][1] = self.snake_chr

        self.snake_body_array.append([2, 1])

        keyboard.add_hotkey("down", self.move_down)
        keyboard.add_hotkey("up", self.move_up)
        keyboard.add_hotkey("left", self.move_left)
        keyboard.add_hotkey("right", self.move_right)

        self.print_snake()
        self.place_egg()

        while not self.game_over:
            self.egg_eaten()
            self.move_snake()


    def print_snake(self):
        os.system("cls")
        for i in range(len(self.snake)):
            for j in range(len(self.snake[i])):
                if i == 0 or i == self.boundry_length-1:
                    print("-"*2, end="")
                elif j == 0:
                    print("|", end="")
                elif j == self.boundry_width-1:
                    print("|", end="")

                else:
                    print(self.snake[i][j], end=" ")
            print()
        print("Score: ", self.score, end="")
        print("%47s"%"High Score: ", 0)
        time.sleep(self.sleep_time)


    def move_snake(self):
        prev_coords = self.snake_body_array[0]
        self.head_coords = prev_coords
        temp = []
        self.snake_body_array[0] = [self.snake_body_array[0][0] + self.snake_direction[0], self.snake_body_array[0][1] + self.snake_direction[1]]
        for i in range(1, len(self.snake_body_array)):
            temp = self.snake_body_array[i]
            self.snake_body_array[i] = prev_coords
            prev_coords = temp
        
        if self.snake_body_array[0][0] < 1:
            self.snake_body_array[0][0] = self.boundry_length - 2
        
        if self.snake_body_array[0][0] > self.boundry_length - 2:
            self.snake_body_array[0][0] = 1

        if self.snake_body_array[0][1] < 1:
            self.snake_body_array[0][1] = self.boundry_width - 2

        if self.snake_body_array[0][1] > self.boundry_width - 2:
            self.snake_body_array[0][1] = 1

        # print(self.snake_body_array[0], self.head_coords)

        self.snake = []
        for i in range(30):
            self.snake.append([])
            for j in range(30):
                if [i, j] in self.snake_body_array:
                    self.snake[i].append(self.snake_chr)
                elif [i, j] == self.egg_coords:
                    self.snake[i].append("@")
                else:
                    self.snake[i].append(" ")
        
        self.snake[self.snake_body_array[-1][0]][self.snake_body_array[-1][1]] = self.snake_tail_chr
        self.snake[self.snake_body_array[0][0]][self.snake_body_array[0][1]] = self.snake_head_chr
        
        if self.snake_body_array[0] in self.snake_body_array[1:]:
            self.game_over = True
            self.print_snake()
            print("%30s"%"Game Over")
            return
        self.print_snake()

    
    def move_down(self):
        if self.snake_direction != [-1, 0]:
            self.snake_direction = [1, 0]
    

    def move_up(self):
        if self.snake_direction != [1, 0]:
            self.snake_direction = [-1, 0]

    
    def move_left(self):
        if self.snake_direction != [0, 1]:
            self.snake_direction = [0, -1]

    
    def move_right(self):
        if self.snake_direction != [0, -1]:
            self.snake_direction = [0, 1]


    def place_egg(self):
        coords = [random.randint(1, 27), random.randint(1, 27)]
        if coords in self.snake_body_array:
            self.place_egg()
        else:
            self.egg_coords = coords

    
    def egg_eaten(self):
        if self.egg_coords == self.snake_body_array[0]:
            self.snake_body_array.append(self.snake_body_array[-1])
            self.score += 1
            if self.sleep_time < 0.01:
                self.sleep_time -= 0.04
            self.place_egg()

    
game = SnakeGame()
