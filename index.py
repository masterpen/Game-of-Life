import turtle
import random
import time


grid_size = int(input("Enter the size of the grid (e.g., grid_size for a grid_sizexgrid_size grid): "))

def drawScreenBorders():


    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-grid_size*10,grid_size*10)  # 设置起始位置
    pen.pendown()

    for i in range(4):
        pen.forward(grid_size*20)  # 根据边界大小前进
        pen.right(90)


def initializeTheCells():
    for i in range(grid_size):
        cells.append([])
        for j in range(grid_size):
            newCell = turtle.Turtle()
            newCell.penup()
            newCell.shape("square")
            newCell.shapesize(stretch_wid=0.9, stretch_len=0.9)
            cells[i].append(newCell)
            rand = random.randint(0, 1)
            newCell.state = rand
            newCell.lifespan = 0  # 初始化 lifespan 属性
            if rand == 0:  # state 0 for being dead
                newCell.color("gray50")  # color white for being dead
            else: 
                newCell.color("gray0")  # color black for being alive

                      
def showTheUniverse():
    start_pos = (grid_size * 10) - 10  # 计算起始位置
    ycor = start_pos

    for i in range(grid_size):
        xcor = 0-start_pos
        for j in range(grid_size):
            cells[i][j].goto(xcor, ycor)
            xcor += 20  # 每个细胞的宽度
        ycor -= 20  # 每个细胞的高度




def esc():
    global stop
    stop = True

def getNeighbors(i, j):
    neighborsamount = 0
    if boundaryCondition==1:
         
        if i - 1 >= 0:
            neighborsamount += cells[i-1][j].state
            if j - 1 >= 0:
                neighborsamount += cells[i-1][j-1].state
            if j + 1 < grid_size:
                neighborsamount += cells[i-1][j+1].state
        if j - 1 >= 0:
            neighborsamount += cells[i][j-1].state
        if j + 1 < grid_size:
            neighborsamount += cells[i][j+1].state
        if i + 1 < grid_size:
            neighborsamount += cells[i+1][j].state
            if j - 1 >= 0:
                neighborsamount += cells[i+1][j-1].state
            if j + 1 < grid_size:
                neighborsamount += cells[i+1][j+1].state

    elif boundaryCondition == 2:
        # 处理周期性边界条件
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue  # 跳过细胞自身
                ni, nj = (i + di) % grid_size, (j + dj) % grid_size  # 确保索引在范围内
                neighborsamount += cells[ni][nj].state
    return neighborsamount

def updateCells():
    global cells
    new_cells = [[0] * grid_size for _ in range(grid_size)]

    # 首先计算出所有细胞的新状态
    for i in range(grid_size):
        for j in range(grid_size):
            count = getNeighbors(i, j)

            if cells[i][j].state == 1 and (count < 2 or count > 3):
                new_cells[i][j] = 0
            elif cells[i][j].state == 0 and count == 3:
                new_cells[i][j] = 1
            elif cells[i][j].state == 1 and ( count == 2 or count == 3):
                new_cells[i][j] = 1

    # 然后更新细胞的状态、寿命和颜色
    for i in range(grid_size):
        for j in range(grid_size):
            cells[i][j].state = new_cells[i][j]

            if cells[i][j].state == 1:
                # 如果细胞是活的，增加存活轮数并更新颜色
                cells[i][j].lifespan = 0
                cells[i][j].color(getGradientColor(cells[i][j].lifespan))
            else:
                # 如果细胞是死的，重置存活轮数并更新颜色
                cells[i][j].lifespan += 1
                cells[i][j].color(getGradientColor(cells[i][j].lifespan))  # 死细胞的颜色


def getGradientColor(lifespan):
    # 假设游戏每进行一轮，细胞颜色淡化一级
    if lifespan == 0:
        return "gray0"  # 活细胞的颜色
    else:
        # 死细胞颜色从 "gray50" 到 "gray100"
        color_value = 50 + min(50, (lifespan - 1)*10)  # 防止超过 "gray100"
        return f"gray{color_value}"




boundaryCondition = int(input("Choose the Boundary Condition? \nEnter 1 for Constant or 2 for Periodic: "))
print("Press ESC to exit")

wn = turtle.Screen()
wn.setup(width = grid_size*20, height = grid_size*20)
wn.title("Life Game")
wn.tracer(0)

wn.listen()
wn.onkeypress(esc, "Escape") #Press ESC to exit


stop = False 
cells = []
drawScreenBorders() #Already done for you
initializeTheCells() #Already done for you
showTheUniverse() #Already done for you


while not stop:
    wn.update()
    updateCells()
    time.sleep(0.01)

