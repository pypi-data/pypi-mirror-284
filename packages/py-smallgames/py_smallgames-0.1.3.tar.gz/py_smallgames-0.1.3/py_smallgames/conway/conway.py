"""
康威生命游戏（Conway's Game of Life）是一种由英国数学家约翰·康威在1970年发明的细胞自动机。这个游戏使用一个二维的网格，每个
格子可以是“活”或者“死”状态。每个格子的状态根据周围格子的状态进行更新，遵循以下规则：

如果一个活细胞周围有少于两个活细胞，它将因为“孤独”而死去。
如果一个活细胞周围有两个或三个活细胞，它将保持活状态。
如果一个活细胞周围有超过三个活细胞，它将因为“拥挤”而死去。
如果一个死细胞周围正好有三个活细胞，它将变成活细胞。

使用pygame库设计康威生命游戏的基本步骤如下：

初始化pygame：设置屏幕大小和颜色。
定义游戏参数：包括网格大小、细胞大小、更新速度等。
创建网格：随机生成初始状态的网格。
更新逻辑：根据康威生命游戏的规则更新网格状态。
绘制网格：将更新后的网格绘制到屏幕上。
事件处理：处理用户输入，如暂停、重启等。
"""

import numpy as np
import pygame as pg

# 初始化pg
pg.init()

# 设置屏幕大小
sw, sh = 800, 600
screen = pg.display.set_mode((sw, sh))

# 定义网格参数
nx, ny = 60, 80
size = sw // nx


class Cells:
    def __init__(self):
        self.cells = np.random.choice((0, 1), (nx, ny))
        print(self.cells.shape)

    def update_logic(self):
        new_cells = np.zeros((nx, ny))
        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                total = 0
                for r in range(max(0, row - 1), min(len(self.cells), row + 2)):
                    for c in range(max(0, col - 1), min(len(self.cells[0]), col + 2)):
                        if (r != row or c != col) and self.cells[r][c] == 1:
                            total += 1
                if self.cells[row][col] == 1 and (total == 2 or total == 3):
                    new_cells[row][col] = 1
                elif self.cells[row][col] == 0 and total == 3:
                    new_cells[row][col] = 1
                else:
                    new_cells[row][col] = 0
        self.cells = new_cells

    def draw(self, surface: pg.Surface):
        surface.fill('black')
        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                if self.cells[row][col] == 1:
                    pg.draw.rect(surface, 'green', (col * size, row * size, size, size))
                pg.draw.rect(surface, 'white', (col * size, row * size, size, size), 1)


# 主循环
running = True
clock = pg.time.Clock()
cells = Cells()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    cells.update_logic()
    cells.draw(screen)
    pg.display.flip()
    clock.tick(10)  # 控制更新速度

pg.quit()
