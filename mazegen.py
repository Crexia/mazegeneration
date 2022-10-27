
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import pygame
import random

class Maze():
    def __init__(self,n,m) -> None:
        self.n = n
        self.m = m
        self.grid = np.ones((n,m))
        self.unvisited = [((i*2)+1,(j*2)+1) for i in range(int((self.n -1 )/ 2)) for j in range(int((self.m-1)/2))]
        self.player = random.choice(self.unvisited)

    def get_initial_pos(self):
        return random.choice(self.unvisited)
    
    def gen_Prim(self):
        pass

    def gen_Kruskal(self):
        pass

    def gen_it_dfs(self):
        pass

    def gen_recursive(self):
        self.unvisited = [((i*2)+1,(j*2)+1) for i in range(int((self.n -1 )/ 2)) for j in range(int((self.m-1)/2))]
        animation = []

        def rec(cur):
            x,y = cur[0],cur[1]
            self.unvisited.remove(cur)   
            self.grid[y][x] = 0
            animation.append(self.grid.copy())

            if len(self.unvisited) == 0:
                return self.grid

            neighbors = __get_neighbours_rec(x,y)
            while len(neighbors) != 0:
                cell = neighbors.pop()
                if cell in self.unvisited:
                    self.grid[int((y + cell[1])/2),int((x + cell[0])/2)] = 0
                    rec(cell)
        
        def __get_neighbours_rec(x,y):
            return set([(max(x-2,0),y),(x,max(y-2,0)),(x,min(y+2,self.m)),(min(x+2,self.n),y)])

        return rec(random.choice(my_maze.unvisited)),animation

    

    def gen_DFS(self):
        pass
        
    def draw_maze_matplot(self,grid):
        plt.matshow(grid, cmap='Greys', interpolation='nearest')
        plt.show()  
    
    def animate_maze(self,size,generator,speed):
        pygame.init()
        screen=pygame.display.set_mode(size)

        result, animation = generator()
        for step in animation:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            game_grid = (1- step.T) * 255
            surf = pygame.surfarray.make_surface(game_grid)
            surf = pygame.transform.scale(surf, size)
            screen.blit(surf,(0,0))
            pygame.display.flip()
            time.sleep(1/speed)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

    def play_maze(self,size):
        pygame.init()
        screen=pygame.display.set_mode(size)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.grid[self.player[1]-1,self.player[0]] == 0:
                        self.player = (self.player[0],self.player[1]-1)
                    if event.key == pygame.K_DOWN and self.grid[self.player[1]+1,self.player[0]] == 0:
                        self.player = (self.player[0],self.player[1]+1)
                    if event.key == pygame.K_RIGHT and self.grid[self.player[1],self.player[0]+1] == 0:
                        self.player = (self.player[0]+1,self.player[1])
                    if event.key == pygame.K_LEFT and self.grid[self.player[1],self.player[0]-1] == 0:
                        self.player = (self.player[0]-1,self.player[1])

            game_grid = (1- self.grid.T) * 255

            surf = pygame.surfarray.make_surface(game_grid)
            surf = pygame.transform.scale(surf, size)

            rx = (size[0] / self.m)
            ry = (size[1] / self.n)

            player_obj = pygame.Rect(self.player[0] * rx ,self.player[1] * ry ,rx,ry)

            screen.blit(surf,(0,0))
            pygame.draw.rect(screen,(255,0,0),player_obj)

            pygame.display.flip()

my_maze = Maze(49,49)
# grid = my_maze.gen_recursive()
my_maze.animate_maze((490,490),my_maze.gen_recursive,100)
# my_maze.draw_maze_matplot(my_maze.grid)
# my_maze.play_maze((490,490))


