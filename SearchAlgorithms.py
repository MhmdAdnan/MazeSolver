from queue import PriorityQueue


class Node:
    id = []  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    previousNode_s = None
    previousNode_g = None
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    edgeCost = None  # Represents the cost on the edge from any parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    heuristicFn = None  # Represents the value of heuristic function
    value = None
    parent = None

    def __init__(self, id, value):

        self.id = id
        self.value = value


        pass

    def Node_up(self, Maze2d):
        posx = 0
        posy = 0

        n = []
        for i in range(len(Maze2d)):
            for j in range(len(Maze2d[0])):
                n = [i, j]

                if (self.id == n):
                    posx = i
                    posy = j

        if (posx - 1 >= 0):
            if (Maze2d[posx - 1][posy] != '#'):
                n = [posx - 1, posy]
                return n

        pass

    def Node_down(self, Maze2d):
        posx = 0
        posy = 0

        n = []
        for i in range(len(Maze2d)):
            for j in range(len(Maze2d[0])):
                n = [i, j]

                if (self.id == n):
                    posx = i
                    posy = j

        if (posx + 1 <= len(Maze2d)-1):
            if (Maze2d[posx + 1][posy] != '#'):
                n = [posx + 1, posy]

                return n
        pass

    def Node_left(self, Maze2d):
        posx = 0
        posy = 0

        n = []
        for i in range(len(Maze2d)):
            for j in range(len(Maze2d[0])):
                n = [i, j]

                if (self.id == n):
                    posx = i
                    posy = j

        if (posy - 1 >= 0):
            if (Maze2d[posx][posy - 1] != '#'):
                n = [posx, posy - 1]
                return n

        pass

    def Node_right(self, Maze2d):
        posx = 0
        posy = 0

        n = []
        for i in range(len(Maze2d)):
            for j in range(len(Maze2d[0])):
                n = [i, j]

                if (self.id == n):
                    posx = i
                    posy = j

        if (posy + 1 <= len(Maze2d[0])-1):
            if (Maze2d[posx][posy + 1] != '#'):
                n = [posx, posy + 1]
                return n
        pass

    def searchfornodes(self, l_id, darr):
        for i in range(len(darr)):
            for j in range(len(darr[0])):
                if l_id == darr[i][j].id:
                    return darr[i][j]

    def get_all_MoveFor_Node(self, Maze2d, darr):
        FinalMove = []

        move = self.Node_up(Maze2d)
        if move != None:
            FinalMove.append(self.searchfornodes(move, darr))
        move = self.Node_down(Maze2d)
        if move != None:
            FinalMove.append(self.searchfornodes(move, darr))
        move = self.Node_left(Maze2d)
        if move != None:
            FinalMove.append(self.searchfornodes(move, darr))
        move = self.Node_right(Maze2d)
        if move != None:
            FinalMove.append(self.searchfornodes(move, darr))

        return FinalMove

    def get_all(self, node, m):
        Moves = []
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j].id[0] == node.id[0] and m[i][j].id[1] == node.id[1]:
                    if i != 0 and m[i - 1][j].value != '#':
                        Moves.append(m[i - 1][j])
                    if i != len(m) - 1 and m[i + 1][j].value != '#':
                        Moves.append(m[i + 1][j])
                    if j != 0 and m[i][j - 1].value != '#':
                        Moves.append(m[i][j - 1])
                    if j != len(m) - 1 and m[i][j + 1].value != '#':
                        Moves.append(m[i][j + 1])
        return Moves


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = 0  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)
    Maze2D = []
    NodeArr = []
    hOfN = []

    def __init__(self, mazeStr, heristicValue=None):
        self.path.clear()
        self.fullPath.clear()
        self.NodeArr.clear()
        self.Maze2D.clear()
        self.hOfN = heristicValue
        self.NodeArr = self.convert(mazeStr)
        pass

    def convert(self, mazeStr):
        NE = []
        row_maze = []
        for x in range(len(mazeStr)):
            if (mazeStr[x] != ',' and mazeStr[x] != ' '):
                row_maze.append(mazeStr[x])

            if (mazeStr[x] == ' '):
                self.Maze2D.append(row_maze)
                row_maze = []
        self.Maze2D.append(row_maze)

        counterx = 0
        for x in range(len(self.Maze2D)):
            row_maze_node = []
            countery = 0
            for i in range(len(self.Maze2D[0])):
                nid = [counterx, countery]
                n = Node(nid, self.Maze2D[x][i])

                row_maze_node.append(n)
                countery = countery + 1

            NE.append(row_maze_node)
            counterx = counterx + 1
        NE.append(row_maze_node)

        nn = []

        if (self.hOfN != None):

            c = 0
            row = []

            for mm in self.hOfN:

                row.append(mm)
                c += 1

                if c == len(self.Maze2D[0]):
                    c = 0

                    nn.append(row)

                    row = []

            for i in range(len(self.Maze2D)):
                for j in range(len(self.Maze2D[0])):
                    NE[i][j].hOfN = nn[i][j]

        return NE

    def get_the_first_Node(self):
        for i in range(len(self.NodeArr)):
            for j in range(len(self.NodeArr[0])):
                if (self.NodeArr[i][j].value == 'S'):
                    return self.NodeArr[i][j]

    def get_the_goal_Node(self):
        for i in range(len(self.NodeArr)):
            for j in range(len(self.NodeArr[0])):
                if (self.NodeArr[i][j].value == 'E'):
                    return self.NodeArr[i][j]

    def DLS(self):

        def recDLS(s, limit):
            self.path.append(s.id)
            self.fullPath.append(s.id)
            if s.value == 'E':
                return self.path, self.fullPath
            elif limit == 0:
                self.path.pop()
                return -1
            else:
                cutoff = False
                nodes = []
                nodes = Node.get_all(self, s, self.NodeArr)
                for child in nodes:
                 if child.id not in self.fullPath:
                    child.previousNode = s
                    res = recDLS(child, limit - 1)
                    if res == -1:
                        cutoff = True
                    elif res != -2:
                        return res
                self.path.pop()
                if cutoff:
                    return -1
                else:
                    return -2

        recDLS(self.get_the_first_Node(), 50)
        return self.path, self.fullPath

    def get_p_s(self,No):   #ms2la tanya path mn start
        arr = []
        while No != None:
             arr.append(No.id)
             No = No.previousNode_s

        return arr
    def get_p_g(self,No):   #ms2la tanya path mn goal
       arr = []
       No = No.previousNode_g
       while No!=None:
           arr.append(No.id)
           No = No.previousNode_g

       return arr



    def BDS(self):
        Q_of_start = []
        Q_of_Goal = []
        visited_s = []
        visited_g = []
        Q_of_start.append(self.NodeArr[0][0])
        Q_of_Goal.append(self.NodeArr[4][3])
        while len(Q_of_start) != 0 and len(Q_of_Goal) != 0:
            if len(Q_of_start) != 0:
                x = Q_of_start.pop(0)
                visited_s.append(x.id)
                if x == self.NodeArr[4][3].id or x in Q_of_Goal:

                    path1 = self.get_p_s(x)
                    path1.reverse()
                    self.path = path1+ self.get_p_g(x)
                    self.fullPath = visited_s + visited_g
                    return self.path,self.fullPath

                else:
                    list1 = x.get_all_MoveFor_Node(self.Maze2D, self.NodeArr)
                    for u in list1:
                        
                         if u.id not in visited_s:
                            u.previousNode_s = x
                            Q_of_start.append(u)

            if len(Q_of_Goal) != 0:
                y = Q_of_Goal.pop(0)
                visited_g.append(y.id)
                if y == self.NodeArr[0][0].id or y in Q_of_start:

                    path1 = self.get_p_s(y)
                    path1.reverse()
                    self.path = path1+self.get_p_g(y)
                    self.fullPath = visited_s + visited_g
                    return self.path , self.fullPath
                else:
                    list1 = y.get_all_MoveFor_Node(self.Maze2D, self.NodeArr)
                    for u in list1:
                        if u.id not in visited_g:
                            u.previousNode_g = y
                            Q_of_Goal.append(u)

        return -1

   
    def ret_node(self, id):
        return self.NodeArr[id[0]][id[1]]

    def getPath(self, id):
        node = self.ret_node(id)
        temp = node
        self.path.append(temp.id)
        while temp.id != self.get_the_first_Node().id:
            temp = temp.previousNode
            self.path.append(temp.id)
            self.totalCost += temp.hOfN

    def BFS(self):

        open_list = PriorityQueue()
        list_visited = []
        h = self.get_the_first_Node().hOfN
        no = self.get_the_first_Node()
        open_list.put((h, no.id))
        while open_list.empty() == False:
            n = open_list.get()
            list_visited.append(n[1])
            if n[1] == self.get_the_goal_Node().id:  # GOAL
                self.getPath(n[1])
                return self.path[::-1], list_visited, self.totalCost
            else:
                for a in self.ret_node(n[1]).get_all_MoveFor_Node(self.Maze2D, self.NodeArr):
                    if a.id not in list_visited:
                        temp_prev = self.ret_node(n[1])
                        temp_prev.id = n[1]
                        temp_prev.hOfN = n[0]
                        a.previousNode = temp_prev
                        open_list.put((a.hOfN, a.id))



def main():

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DLS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

        ########################################################################################
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BDS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')
    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.',
                                [0, 15, 2, 100, 60, 35, 30, 3
                                      , 100, 2, 15, 60, 100, 30, 2
                                      , 100, 2, 2, 2, 40, 30, 2, 2
                                      , 100, 100, 3, 15, 30, 100, 2
                                      , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.BFS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
    #######################################################################################


main()
