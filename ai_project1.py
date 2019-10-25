# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class state():
    def __init__(self,mode,nums_arr,depth,parent=None):
        self.depth = depth
        self.f = 0
        self.parent = parent
        coord_x=0
        coord_y=0
        blankOneFound=0
        self.board={}
        self.childStates=None
        if mode == 0:
            for elem in nums_arr:
                if coord_x>3:
                    coord_x=0
                    coord_y+=1
                if elem=="1":
                    self.board["one"]=[coord_x,coord_y]
                elif elem=="2":
                    self.board["two"]=[coord_x,coord_y]
                elif elem=="3":
                    self.board["three"]=[coord_x,coord_y]
                elif elem=="4":
                    self.board["four"]=[coord_x,coord_y]
                elif elem=="5":
                    self.board["five"]=[coord_x,coord_y]
                elif elem=="6":
                    self.board["six"]=[coord_x,coord_y]
                elif elem=="7":
                    self.board["seven"]=[coord_x,coord_y]
                elif elem=="8":
                    self.board["eight"]=[coord_x,coord_y]
                elif elem=="9":
                    self.board["nine"]=[coord_x,coord_y]
                elif elem=="10":
                    self.board["ten"]=[coord_x,coord_y]
                elif elem=="11":
                    self.board["eleven"]=[coord_x,coord_y]
                elif elem=="12":
                    self.board["twelve"]=[coord_x,coord_y]
                elif elem=="13":
                    self.board["thirteen"]=[coord_x,coord_y]
                elif elem=="14":
                    self.board["fourteen"]=[coord_x,coord_y]
                elif elem=="0" and blankOneFound:
                    self.board["blankTwo"]=[coord_x,coord_y]
                elif elem=="0":
                    self.board["blankOne"]=[coord_x,coord_y]
                    blankOneFound=1
                coord_x+=1
        elif mode==1:
            self.board=nums_arr

    def __eq__(self,other):
        alt = self.alternate()
        if self.board == other.board or alt.board == other.board:
            return True
        return False
    
    def returnArray(self):
        retArr=[None]*16
        switchCase = {
                "blankOne": 0,
                "blankTwo": 0,
                "one":      1,
                "two":      2,
                "three":    3,
                "four":     4,
                "five":     5,
                "six":      6,
                "seven":    7,
                "eight":    8,
                "nine":     9,
                "ten":      10,
                "eleven":   11,
                "twevle":   12,
                "thirteen": 13,
                "fourteen": 14}
        for key in self.board:
            pos = (self.board[key][1]+1)*4+(self.board[key][0]+1) - 1
            retArr.insert(switchCase.get(key),pos)
        return retArr
    
    def oneUp(self):
        newState = state(1,self.board,self.depth+1,self)
        if newState.board["blankOne"][1]>0:
            new_coord = newState.board["blankOne"]
            new_coord[1] -= 1
            for key in newState.board:
                if newState.board[key] == new_coord:
                    newState.board[key][1] +=1
                    newState.board["blankOne"] = new_coord
                    return newState
        else:
            return None
    
    def oneRight(self):
        newState = state(1,self.board,self.depth+1,self)
        if newState.board["blankOne"][0]<3:
            new_coord = newState.board["blankOne"]
            new_coord[0] += 1
            for key in newState.board:
                if newState.board[key] == new_coord:
                    newState.board[key][0] -=1
                    newState.board["blankOne"] = new_coord
                    return newState
        else:
            return None
    
    def oneDown(self):
        newState = state(1,self.board,self.depth+1,self)
        if newState.board["blankOne"][1]<3:
            new_coord = newState.board["blankOne"]
            new_coord[1] += 1
            for key in newState.board:
                if newState.board[key] == new_coord:
                    newState.board[key][1] -=1
                    newState.board["blankOne"] = new_coord
                    return newState
        else:
            return None
    
    def oneLeft(self):
        newState = state(1,self.board,self.depth+1,self)
        if newState.board["blankOne"][0]>0:
            new_coord = newState.board["blankOne"]
            new_coord[0] -= 1
            for key in newState.board:
                if newState.board[key] == new_coord:
                    newState.board[key][0] +=1
                    newState.board["blankOne"] = new_coord
                    return newState
        else:
            return None
    
    def twoUp(self):
        newState = state(1,self.board,self.depth+1,self)
        if newState.board["blankTwo"][1]>0:
            new_coord = newState.board["blankTwo"]
            new_coord[1] -= 1
            for key in newState.board:
                if newState.board[key] == new_coord:
                    newState.board[key][1] +=1
                    newState.board["blankTwo"] = new_coord
                    return newState
        else:
            return None
    
    def twoRight(self):
        newState = state(1,self.board,self.depth+1,self)
        if newState.board["blankTwo"][0]>3:
            new_coord = newState.board["blankTwo"]
            new_coord[0] += 1
            for key in newState.board:
                if newState.board[key] == new_coord:
                    newState.board[key][0] -=1
                    newState.board["blankTwo"] = new_coord
                    return newState
        else:
            return None
    
    def twoDown(self):
        newState = state(1,self.board,self.depth+1,self)
        if newState.board["blankTwo"][1]<3:
            new_coord = newState.board["blankTwo"]
            new_coord[1] += 1
            for key in newState.board:
                if newState.board[key] == new_coord:
                    newState.board[key][1] -=1
                    newState.board["blankTwo"] = new_coord
                    return newState
        else:
            return None
    
    def twoLeft(self):
        newState = state(1,self.board,self.depth+1,self)
        if newState.board["blankTwo"][0]>0:
            new_coord = newState.board["blankTwo"]
            new_coord[0] -= 1
            for key in newState.board:
                if newState.board[key] == new_coord:
                    newState.board[key][0] +=1
                    newState.board["blankTwo"] = new_coord
                    return newState
        else:
            return None
        
    def alternate(self):
        newState = state(1,self.board,self.depth)
        blank_coord = newState.board.get("blankOne")
        newState.board["blankOne"] = newState.board.get("blankTwo")
        newState.board["blankTwo"] = blank_coord
        return newState
    
    def calc_fn(self,goal):
        h = 0
        for key in self.board:
            if key!="blankOne" and key!="blankTwo":
                h+=abs(self.board[key][0]-goal.board[key][0])+abs(self.board[key][1]-goal.board[key][1])
        self.f = self.depth + h
    
    def expand_node(self):
        self.childStates={
                self.oneUp():"U1",
                self.oneRight():"R1",
                self.oneDown():"D1",
                self.oneLeft():"L1",
                self.twoUp():"U2",
                self.twoRight():"R2",
                self.twoDown():"D2",
                self.twoLeft():"L2"
            }

def main():
    initial_state_arr = []
    final_state_arr = []
    nodesGenerated = 1
    inFile = open("inputFile.txt",'w')
    inLines = inFile.readlines()
    for i in range(4):
        splitLine = inLines[i].split(" ")
        for char in splitLine:
            initial_state_arr.append(char)
    for j in range(6,10):
        splitLine = inLines[i].split(" ")
        for char in splitLine:
            final_state_arr.append(char)
    print(initial_state_arr)
    explored=[]
    frontier=[state(0,initial_state_arr,0)]
    goal_state = state(0,final_state_arr,0)
    
    while 1:
        if len(frontier)==0: # If no nodes left to explore, terminate program
            print("No solution found")
            inFile.close()
            exit(1)
        curr_node = frontier.pop()
        if curr_node==goal_state: # If goal state reached, write to file and terminate program
            # Replace this with a parent system
            inFile.write("\n"+curr_node.depth)
            inFile.write("\n")
            inFile.write("\n"+nodesGenerated)
            inFile.write("\n")
            path = []
            fpath = []
            path_cursor = curr_node
            while path_cursor.parent != None:
                fpath.insert(0,path_cursor.f)
                child = path_cursor
                path_cursor = path_cursor.parent
                path.insert(0,path_cursor.childStates.get(child))
            fpath.insert(0,path_cursor.f)
            for elem in path:
                inFile.write(elem+" ")
            inFile.write("\n")
            for elem in fpath:
                inFile.write(elem+" ")
            inFile.write("\n")
            inFile.close()
            print("Solution Found!")
            exit(1)
        explored.append(curr_node)
        explored.append(curr_node.alternate()) # Empty spaces on the board are not abstracted. Alternate version of each state, where positions of empty spaces are swapped are saved to explored as well
        curr_node.expand_node()
        nodesGenerated+=8
        
        # Modify this to account for childStates being a dict
        for i in range(len(curr_node.childStates)): # Iterate through current node's child states
            if curr_node.childStates[i] != None:
                if curr_node.childStates[i] not in explored and curr_node.childStates[i] not in frontier:
                    curr_node.childStates[i].calc_fn(goal_state)
                    # This section places newly discovered nodes into its priority position
                    # Priority is defined by f(n), where f(n)=g(n)+h(n) & g(n)=depth & h(n) is Manhattan distances of numbered tiles to goal positions.
                    j = len(frontier)-1
                    if j==-1:
                        frontier.insert(0,curr_node.childStates[i])
                    else:
                        while curr_node.childStates[i].f>frontier[j]:
                            j-=1
                        frontier.insert(j,curr_node.childStates[i])