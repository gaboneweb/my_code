"""Perfect Maze using the rndomized recursive Depth-First-Search algorithm"""

# Create a maze using the depth-first algorithm described at
# https://scipython.com/blog/making-a-maze/
# Christian Hill, April 2017.
# Some of the code taken from here as well
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
        self._visited = False
        self.walls = {'N':True, 'S':True, 'E':True, 'W': True}
        self.x = x
        self.y = y
        self.g_n = 0
        self.h_n = 0
        self.f_n = self.g_n + self.h_n
        


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


    def is_visited(self):
        return self._visited


    def visit(self):
        self._visited = True

    def un_visit(self):
        self._visited = False

    def cal_fn(self):
        self.f_n = self.g_n + self.h_n
        

class Maze:
    def __init__(self,hieght,width) -> None:
        self.hieght = hieght
        self.width = width
        self.maze = []
        self.prev_visited = ListStack()
        self.num_visited = 0

    def __str__(self) -> str:
        """Return a string representation of the maze."""

        maze_rows = []
        for row in range(self.hieght):
            upper_wall = '+--'
            maze_row = []
            for col in range(self.width):
                if col == self.width - 1 and self.maze[row][col].walls['N'] :
                    maze_row.append(upper_wall + "+")
                elif self.maze[row][col].walls['N'] :
                    maze_row.append(upper_wall)
                else:
                    maze_row.append('+  +' if col == self.width-1 and not self.maze[row][col].walls['N']  else '+  ')
            maze_rows.append(''.join(maze_row))
            row_wall = '  |'
            maze_row = []
            for col in range(self.width):
                if col == 0:
                    maze_row.append(("|" if self.maze[row][col].walls['W'] else ' ') +   ("  |" if self.maze[row][col].walls['E'] else '   '))
                elif self.maze[row][col].walls['E']:
                    maze_row.append(row_wall)
                else:
                    maze_row.append('   ')
            maze_rows.append(''.join(maze_row))

        maze_rows.append('+--' * self.width + '+')

        return '\n'.join(maze_rows)


    def create_grid(self):
        """Create a height x width 2D list to hold all the cells
        """
        for i  in range(self.hieght):
            row = []
            for j in range(self.width):
                row.append(Cell(i,j))

            self.maze.append(row)


    def is_valid_pos(self, x, y):
        """Checks if the  x and y are a valid position in the maze.

        Args:
            x (int): The x(row) position of the current cell
            y (int): The y(column) position of the current cell

        Returns:
            bool: Returns True if x and y fall within the maze row and column,else returns False
        """
        x_valid = x >= 0 and x <= self.hieght -1
        y_valid = y >= 0 and y <= self.width -1

        return x_valid and y_valid


    def get_neighbors(self, current_cell):
        """Gets the position of  random neighbor that has not been visited.

        Args:
            x (int): The x(row) position of the current cell
            y (int): The y(column) position of the current cell

        Returns:
            tuple: The x(row) and y(column) of a neighbor that has not been visited.If all neighbors have
                    been visted,return an tuple containg string spaces
        """
        x, y = current_cell.x, current_cell.y

        pos_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        not_vis_neigbors = [(x,y) for x,y in pos_neighbors if self.is_valid_pos(x,y) and not self.maze[x][y].is_visited()]

        if len(not_vis_neigbors) > 0:
            x_, y_ = not_vis_neigbors[random.randint(0,len(not_vis_neigbors) - 1)]
            rand_neighbor = self.maze[x_][y_]
        else:
            rand_neighbor = None

        return rand_neighbor

    def make_path(self,current_cell):
        """"Recursively create a maze using the Depth-First-Search algorithm"""

        #Base case: Return if the number of visited cells equal the total number of cells
        if self.num_visited == (self.hieght * self.width):
            return

        current_cell.visit() 

        # Choose a random neighbouring cell and move to it.
        neighbor = self.get_neighbors(current_cell)
        
        if neighbor == None:
            if not self.prev_visited.is_empty():
                # We've reached a dead end: backtrack.
                new_curr_cell = self.prev_visited.pop()
                self.make_path(new_curr_cell)
        else:
            current_cell.break_wall(neighbor)
            self.prev_visited.push(current_cell)
            # Total number of visited cells during maze construction.
            self.num_visited += 1

            self.make_path(neighbor)


    def cell_at(self, x, y):
        """Return the Cell object at (y,x)."""

        return self.maze[y][x]     

    def write_svg(self, filename):
        """Write an SVG image of the maze to filename.
           This code is taken as it is from: https://scipython.com/blog/making-a-maze/"""

        aspect_ratio = self.width / self.hieght
        # Pad the maze all around by this amount.
        padding = 10
        # Height and width of the maze image (excluding padding), in pixels
        height = 500
        width = int(height * aspect_ratio)
        # Scaling factors mapping maze coordinates to image coordinates
        scy, scx = height / self.hieght, width / self.width

        def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
            """Write a single wall to the SVG image file handle f."""

            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
                  .format(ww_x1, ww_y1, ww_x2, ww_y2), file=ww_f)

        # Write the SVG image file for maze
        with open(filename, 'w') as f:
            # SVG preamble and styles.
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
                  .format(width + 2 * padding, height + 2 * padding,
                          -padding, -padding, width + 2 * padding, height + 2 * padding),
                  file=f)
            print('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line {', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)
            # Draw the "South" and "East" walls of each cell, if present (these
            # are the "North" and "West" walls of a neighbouring cell in
            # general, of course).
            for x in range(self.width):
                for y in range(self.hieght):
                    if self.cell_at(x, y).walls['S']:
                        x1, y1, x2, y2 = x * scx, (y + 1) * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
                    if self.cell_at(x, y).walls['E']:
                        x1, y1, x2, y2 = (x + 1) * scx, y * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
            # Draw the North and West maze border, which won't have been drawn
            # by the procedure above.
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
            print('</svg>', file=f)

    def reset(self):
        for row in self.maze:
            for cell in row:
                cell.un_visit()
    def get_h(self,curr, goal):

    
        h_x = curr.x - goal.x 
        h_y = curr.y - goal.y 

        return h_x + h_y


    def solve_maze(self,start, goal):
        self.reset()
        start.h_n = self.get_h(start,goal)
        start.cal_fn()
        def get_lowest_cost(start):
            pass
        
        
        pass

        

if __name__ == '__main__':


    hieght ,width=5,5 # random.randint(5,20), random.randint(5,20)
    start_h, start_w = random.randint(0,hieght - 1), random.randint(0,width - 1)

    maze = Maze(hieght,width)
    maze.create_grid()
    start_cell = maze.maze[start_h][start_w]
    maze.make_path(start_cell)

    print(maze)
    maze.write_svg('maze_mine.svg')

