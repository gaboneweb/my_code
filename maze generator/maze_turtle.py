import turtle
from maze_imp import *

screen = turtle.getscreen()

robot = turtle.Turtle()
robot.shape("turtle")
robot.color('green')
robot.speed(0)

def draw_maze(maze):
    row_ = 0
    col_ = 0
    global robot
    start_x,start_y = -200, 200
    robot.penup()
    robot.goto(start_x,start_y)
    robot.pendown()


    for row in maze:
        row_ += 1
        col_ = 0
        for col in row:
            col_ += 1
            if col.walls['N']:
                robot.forward(25)
            else:
                robot.penup()
                robot.forward(25)
                robot.pendown()
    
        robot.penup()
        start_y -= 25
        robot.goto(start_x,start_y)
        robot.pendown()
    
    start_y = 200
    robot.penup()
    robot.goto(start_x,start_y)
    robot.pendown()
    robot.setheading(270)

    for row in maze:
        for col in row:

            if col.walls['W']:
                robot.forward(25)
            else:
                robot.penup()
                robot.forward(25)
                robot.pendown()
            robot.penup()
            start_x += 25
            robot.goto(start_x,start_y)
            robot.pendown()
        
        robot.penup()
        start_x = -200
        start_y -= 25
        robot.goto(start_x,start_y)
        robot.pendown()

    robot.left(90)
    robot.forward(col_*25)
    robot.left(90)
    robot.forward(row_*25)


    



if __name__ == '__main__':
    maze = Maze(20,20)
    maze.create_grid()
    # draw_maze(maze.maze)

    maze.make_path(0,0)
    print(maze)

    draw_maze(maze.maze)
    maze.write_svg('maze_t.svg')

    exit = input("Do you want to exit(yes/no)?")

    while exit == 'no':
        com = 1 + 1
        exit = input("Do you want to exit(yes/no)?")

