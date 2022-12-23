"""Perfect Maze using the rndomized recursive Depth-First-Search algorithm"""
import random

class Empty(RuntimeError):
    pass

class ListStack:
    def __init__(self):
        self.data = []


    def __len__(self):

        return len(self.data)


    def is_empty(self):
        return len(self.data) == 0


    def push(self,e):

        self.data.append(e)


    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")

        return self.data.pop()


    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")

        return self.data[-1]

class Cell:
    def __init__(self,x,y):
        self.visited = False
        self.walls = {'N':True, 'S':True, 'E':True, 'W': True}
        self.x = x
        self.y = y
        self.value = '#'
        


    def __str__(self) -> str:
        return self.value
    def break_wall(self,neighbor):
        if self.x == neighbor.x:
            if neighbor.y > self.y:
                self.walls['E'] = False
                neighbor.walls['W'] = False

            else:
                self.walls['W'] = False
                neighbor.walls['E'] = False


        elif self.y == neighbor.y:
            if neighbor.x > self.x:
                self.walls['S'] = False
                neighbor.walls['N'] = False

            else:
                self.walls['N'] = False
                neighbor.walls['S'] = False


    def is_visted(self):
        return self.visited


    def visit(self):
        self.visited = True

class Maze:
    def __init__(self,width,hieght) -> None:
        self.hieght = hieght
        self.width = width
        self.maze = []
        self.prev_visited = ListStack()
        self.num_visited = 0

    def __str__(self) -> str:
        """Return a (crude) string representation of the maze."""

        maze_rows = ['-' * self.hieght * 2]
        for y in range(self.width):
            maze_row = ['|']
            for x in range(self.hieght):
                if self.maze[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.hieght):
                if self.maze[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def print_maze(self):
        for row in range(self.hieght):
            upper_wall = '+--'
            for col in range(self.width):
                if col == self.width - 1 and self.maze[row][col].walls['N'] :
                    print(upper_wall + "+",end='')
                elif self.maze[row][col].walls['N'] :
                    print(upper_wall,end='')
                else:
                    print('+  +' if col == self.width-1 and not self.maze[row][col].walls['N']  else '+  ', end = '')

            print()
            row_wall = '  |'
            
            for col in range(self.width):
                if col == 0:
                    print(("|" if self.maze[row][col].walls['W'] else ' ') +   ("  |" if self.maze[row][col].walls['E'] else '   '),end='')
                elif self.maze[row][col].walls['E']:
                    print(row_wall,end='')
                else:
                    print('   ',end='')


            print()

        print('+--' * self.width + '+')




    def create_grid(self):

        for i  in range(self.hieght):
            row = []
            for j in range(self.width):
                row.append(Cell(i,j))

            self.maze.append(row)
    def is_valid_pos(self, x, y):
        x_valid = x >= 0 and x <= self.hieght -1
        y_valid = y >= 0 and y <= self.width -1

        return x_valid and y_valid
    def get_neighbors(self, x, y):

        pos_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        neighbors = [(x,y) for x,y in pos_neighbors if self.is_valid_pos(x,y)]
        not_vis_neigbors = [(x,y) for x,y in neighbors if self.maze[x][y].visited == False]
        if len(not_vis_neigbors) > 0:
            rand_neighbor = not_vis_neigbors[random.randint(0,len(not_vis_neigbors) - 1)]
        else:
            rand_neighbor = ' ', ' '

        return rand_neighbor

    def make_path(self, x, y):
        if self.num_visited == (self.hieght * self.width):
            return

        self.maze[x][y].visited = True
        self.maze[x][y].value = 'C'
        x_neighbor, y_neighbor = self.get_neighbors(x,y)
        # print(x_neighbor,y_neighbor)
        if x_neighbor == ' ' or y_neighbor == ' ':
            if not self.prev_visited.is_empty():
                x_back,y_back = self.prev_visited.pop()
                self.make_path(x_back, y_back)
        else:
            self.maze[x_neighbor][y_neighbor].value = 'C'
            self.maze[x][y].break_wall(self.maze[x_neighbor][y_neighbor])
            self.prev_visited.push((x,y))
            self.num_visited += 1

            self.make_path(x_neighbor,y_neighbor)
        
        


    def print_grid(self):

        for row in self.maze:
            for col in row:
                print(col, end = ' ')

            print()

    



if __name__ == '__main__':


    hieght = 20
    width = 20
    start_h = random.randint(0,hieght - 1)
    start_w = random.randint(0,hieght - 1)
    
    maze = Maze(hieght,width)
    maze.create_grid()
    # maze.print_maze()

    maze.make_path(start_h,start_w)

    maze.print_maze()

