class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

class MazeSolver:
    def __init__(self, f):
        self.maze = []
        with open(f, 'r') as myfile:
            while True:
                line = myfile.readline().rstrip('\n')
                if not line:
                    break
                self.maze.append([ch for ch in line])
        self.stack = Stack()

    def getMaze(self):
        x, y = -1, -1
        gx, gy = -1, -1
        walls = []
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'O':
                    x, y = i, j
                if self.maze[i][j] == 'G':
                    gx, gy = i, j
                if self.maze[i][j] == '#':
                    walls.append((i, j))
        return (x, y), (gx, gy), walls

    def findPath(self):

        x, y = -1, -1
        gx, gy = -1, -1
        # print(maze[1])

        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'O':
                    x, y = i, j
                if self.maze[i][j] == 'G':
                    gx, gy = i, j

        post = []
        could_stack = Stack()
        while True:

            could = False
            post.append((x, y))

            if self.maze[x][y] == 'G':
                break

            if self.maze[x + 1][y] and self.maze[x + 1][y] != '#':
                if (x + 1, y) not in post:
                    could_stack.push((x + 1, y))
                    could = True
            if self.maze[x][y + 1] and self.maze[x][y + 1] != '#':
                if (x, y + 1) not in post:
                    could_stack.push((x, y + 1))
                    could = True
            if x - 1 > 0 and self.maze[x - 1][y] and self.maze[x - 1][y] != '#':
                if (x - 1, y) not in post:
                    could_stack.push((x - 1, y))
                    could = True
            if y - 1 > 0 and self.maze[x][y - 1] and self.maze[x][y - 1] != '#':
                if (x, y - 1) not in post:
                    could_stack.push((x, y - 1))
                    could = True

            if could:
                self.stack.push((x, y))
                (x, y) = could_stack.pop()
            else:
                (x, y) = self.stack.pop()
            yield (x, y)
        for item in self.stack.items:
            self.maze[item[0]][item[1]] = 'O'

        self.stack.push((gx, gy))

    def printMaze(self):
        for line in self.maze:
            print('')
            for ch in line:
                print(ch, end='')
        print("\n\n")

    def printPath(self):
        # start = str(stack.items[0])
        goal = str(self.stack.items[-1])
        for item in self.stack.items[:-1]:
            print(item, '->', end=' ')
        print('Goal : ' + goal)

    def getPath(self):
        for item in self.stack.items[:-1]:
            yield item

solver = MazeSolver('mazeTest3.txt')
print(solver.getMaze())
# solver.findPath()
# solver.printMaze()
# solver.printPath()
# maze = readMaze('mazeTest3.txt')
# s = Stack()
# printMaze(findPath(maze, s))
# printPath(s)
