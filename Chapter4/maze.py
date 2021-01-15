class Maze:
    def __init__(self, maze_file_name):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_flie = open(maze_file_name, 'r')
        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list = []
                col = 0
                for ch in line[:-1]:
                    row_list.qppend(ch)
                    if ch == 'S':
                        self.start_row = rows_in_maze
                        self.start_col = col
                    col = col + 1
                rows_in_maze = rows_in_maze + 1
                self.maze_list.append(row_list)
                columns_in_maze = len(row_list)
            self.rows_in_maze = rows_in_maze
            self.columns_in_mazr = columns_in_maze
            self.x_translate = -columns_in_maze / 2
            self.y_translate = rows_in_maze /2
            self.t = Turtle(shape = 'turtle')
            setup(width = 600, height = 600)
            setworldcoordinates((- (columns_in_maze - 1) / 2 -.5, 
            - rows_in_maze -1) /2 -0.5,
            (columns_in_maze - 1) /2 + .5,
            (rows_in_maze - 1) /2 +.5)

def draw_maze(self):
    for y in range(self.rows_in_maze):
        for x in range(self.columns_in_maze):
            if self.maze_list[y][x] == OBSTACLE:
                self.draw_centered_box( x + self.x_translate,
                -y + self.y_translate, 'tan')
    self.t.color('black', 'blue')

def draw_centered_box(self, x, y, color):
    tracer(0)
    self.t.up()
    self.t.goto(x - 0.5, y - 0.5)
    self.t.color('black', color)
    self.t.setheading(90)
    self.t.down()
    self.t.begin_fill()
    for i in range(4):
        self.t.forward(1)
        self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)

def move_turtle(self, x, y):
    self.t.up()
    self.t.setheading(self.t.toward(x + self.xtransalte,
    - y + self.y_translate))
    self.t.goto(x + self.x_translate, -y + self.y_translate)

def drop_bread_crumb(self, color):
    self.t.dot(color)

def update_position(self, row, col, val = None):
    if val:
        self.maze_list[row][col] = val
    self.move_turtle(col, row)

    if val == PART_OF_PATH:
        color = 'green'
    elif val == OBSTACLE:
        color = 'red'
    elif val == TRIED:
        color = 'black'
    elif val == DEAD_END:
        color = 'red'
        else:
            color = None
    if color:
        self.drop_bread_crumb(color)


def is_exit(self, row, col):
    return (row == 0 or row == self.rows_in_maze -1 or col == 0 or col == self.columns_in_maze -1 )


def __getitem__(self, idx):
    return self.maze_list[idx]

