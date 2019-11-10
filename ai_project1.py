# -*- coding: utf-8 -*-
"""
Created By Gafurul (Rafi) Islam Kazi

For any recruiters looking through this,
    please note that this version is neither finished nor optimized.
"""
import sys

class state():
    def __init__(self,mode,nums_arr,depth,parent=None,movement=None):
        self.depth = depth
        self.movement=movement
        self.f = -1
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
            self.board=dict(nums_arr)

    def __eq__(self,other): # __eq__ is designed to check 
        if other==None:
            return False
        alt = self.alternate()
        arr = self.returnArray()
        oArr = other.returnArray()
        altArr = alt.returnArray()
        if oArr==arr or oArr==altArr:
            return True
        return False
    
    def returnArray(self): # This was primarily used for debugging
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
                "twelve":   12,
                "thirteen": 13,
                "fourteen": 14}
        for key in self.board:
            coord=self.board.get(key)
            pos = (coord[1])*4+(coord[0])
            retArr[pos] = switchCase.get(key)
        return retArr
    
    def oneUp(self):
        newState = state(1,self.board,self.depth+1,self,"U1")
        coords = newState.board.get("blankOne")
        if coords[1]==0:
            return None
        else:
            new_coords = [coords[0],coords[1] - 1]
            for key in newState.board:
                if newState.board[key] == new_coords:
                    newState.board[key] = coords
                    newState.board["blankOne"] = new_coords
                    return newState
    
    def oneRight(self):
        newState = state(1,self.board,self.depth+1,self,"R1")
        coords = newState.board.get("blankOne")
        if coords[0]==3:
            return None
        else:
            new_coords = [coords[0]+1,coords[1]]
            for key in newState.board:
                if newState.board[key] == new_coords:
                    newState.board[key] = coords
                    newState.board["blankOne"] = new_coords
                    return newState
    
    def oneDown(self):
        newState = state(1,self.board,self.depth+1,self,"D1")
        coords = newState.board.get("blankOne")
        if coords[1]==3:
            return None
        else:
            new_coords = [coords[0],coords[1] + 1]
            for key in newState.board:
                if newState.board[key] == new_coords:
                    newState.board[key] = coords
                    newState.board["blankOne"] = new_coords
                    return newState
    
    def oneLeft(self):
        newState = state(1,self.board,self.depth+1,self,"L1")
        coords = newState.board.get("blankOne")
        if coords[0]==0:
            return None
        else:
            new_coords = [coords[0] - 1,coords[1]]
            for key in newState.board:
                if newState.board[key] == new_coords:
                    newState.board[key] = coords
                    newState.board["blankOne"] = new_coords
                    return newState
    
    def twoUp(self):
        newState = state(1,self.board,self.depth+1,self,"U2")
        coords = newState.board.get("blankTwo")
        if coords[0]==0:
            return None
        else:
            new_coords = [coords[0],coords[1] - 1]
            for key in newState.board:
                if newState.board[key] == new_coords:
                    newState.board[key] = coords
                    newState.board["blankTwo"] = new_coords
                    return newState
    
    def twoRight(self):
        newState = state(1,self.board,self.depth+1,self,"R2")
        coords = newState.board.get("blankTwo")
        if coords[0]==3:
            return None
        else:
            new_coords = [coords[0] + 1,coords[1]]
            for key in newState.board:
                if newState.board[key] == new_coords:
                    newState.board[key] = coords
                    newState.board["blankTwo"] = new_coords
                    return newState
    
    def twoDown(self):
        newState = state(1,self.board,self.depth+1,self,"D2")
        coords = newState.board.get("blankTwo")
        if coords[0]==0:
            return None
        else:
            new_coords = [coords[0],coords[1] + 1]
            for key in newState.board:
                if newState.board[key] == new_coords:
                    newState.board[key] = coords
                    newState.board["blankTwo"] = new_coords
                    return newState
    
    def twoLeft(self):
        newState = state(1,self.board,self.depth+1,self,"L2")
        coords = newState.board.get("blankTwo")
        if coords[0]==0:
            return None
        else:
            new_coords = [coords[0] - 1,coords[1]]
            for key in newState.board:
                if newState.board[key] == new_coords:
                    newState.board[key] = coords
                    newState.board["blankTwo"] = new_coords
                    return newState
        
    def alternate(self): # This returns a version of the state where blankOne & blankTwo are swapped
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
        return self.f
    
    def expand_node(self):
        self.childStates=[
            self.oneUp(),
            self.oneRight(),
            self.oneDown(),
            self.oneLeft(),
            self.twoUp(),
            self.twoRight(),
            self.twoDown(),
            self.twoLeft()
        ]

"""
Currently considering using LinkedLists instead of normal lists to improve efficiency
"""
#class LinkedList():
#    class Node():
#        def __init__(self,value=None,prev=None,nex=None):
#            self.value=value
#            self.prev=prev
#            self.next=nex
#            
#    def __init__(self,head=None):
#        self.head=Node(head)
#        self.tail=self.head
#    
#    def insert(self,index,value):
#        newNode=Node(value)
#        cursor=self.head
#        if index==0:
#            newNode.next=self.head
#            self.head.prev=newNode
#            self.head=newNode
#        else:
#            for i in range(index):
#                cursor=cursor.next
#            prev=cursor.prev
#            nex=cursor
#            newNode.prev=prev
#            newNode.next=nex
#            prev.next=newNode
#            nex.prev=newNode
#    
#    def returnArray(self):
#        retArr=[]
#        cursor=self.head
#        while cursor!=None:
#            retArr.append(cursor.value)
#            cursor=cursor.next
#        return retArr


initial_state_arr = []
final_state_arr = []
nodesGenerated = 1
inFile = open("Input3.txt",'r')
inLines = inFile.readlines()
outLines = inLines
#print(inLines)
for i in range(9):
    if i<4:
        stripLine = inLines[i].strip()
        splitLine = stripLine.split(" ")
        for char in splitLine:
            initial_state_arr.append(char)
    if i>4:
        stripLine = inLines[i].strip()
        splitLine = stripLine.split(" ")
        for char in splitLine:
            final_state_arr.append(char)
#print(initial_state_arr)
inFile.close()
explored=[]
frontier=[state(0,initial_state_arr,0)]
goal_state = state(0,final_state_arr,0)
frontier[0].calc_fn(goal_state)

while 1:
#    if len(explored)%10==0:
    for ch in frontier:
        print(len(frontier),len(explored),ch.returnArray(),ch.f,ch.movement)
    
    
    
    if len(frontier)==0: # If no nodes left to explore, terminate program
        print("No solution found")
        sys.exit(0)
    curr_node = frontier.pop()
#    print(curr_node.returnArray())
    if curr_node==goal_state: # If goal state reached, write to file and terminate program
        print("Solution Found!")
        #sys.exit()
        outFile = open("Output3.txt",'w')
        for line in outLines:
            outFile.write(line)
        outFile.write("\n"+str(curr_node.depth))
        outFile.write("\n"+str(nodesGenerated))
        outFile.write("\n")
        path = []
        fpath = []
        path_cursor = curr_node
        while path_cursor.parent != None:
            fpath.insert(0,path_cursor.f)
            child = path_cursor
            path_cursor = path_cursor.parent
            for ch in path_cursor.childStates:
                if ch==child:
                    path.insert(0,ch.movement)
        fpath.insert(0,path_cursor.f)
        for elem in path:
            outFile.write(elem+" ")
        outFile.write("\n")
        for elem in fpath:
            outFile.write(str(elem)+" ")
        outFile.write("\n")
        outFile.close()
        sys.exit()
    explored.append(curr_node)
    curr_node.expand_node()
    for ch in curr_node.childStates:
        if ch!=None:
            nodesGenerated+=1
    
#    print("Original: ",curr_node.returnArray(),"\n")
#     
#    for ch in curr_node.childStates:
#        if ch==None:
#            print("None\n")
#        else:
#            print(ch.movement,": ",ch.returnArray())
#            print(ch==goal_state,"\n")
        

    for child in curr_node.childStates: # Iterate through current node's child states
        if child != None:
            flag = True
            #print("\n")
            #If this childState already exists in explored or the frontier, no further action will be taken
            #In a more advanced system, it would check if the version of the state stored in explored or frontier, however, with this type of problem, it is not necessary to check, because the childState would never have a lower f(n) than the version already in explored or frontier.
            #Short for lists were used instead of "if child in lst" because I could not find if this method would use the __eq__ function that I made.
            
            for elem in explored:
                if elem == child:
                    flag = False
            for elem in frontier:
                if elem == child:
                    flag = False
            
            if flag:
                child.calc_fn(goal_state)
                
                # This section places newly discovered nodes into its priority position
                # Priority is defined by f(n), where f(n)=g(n)+h(n) & g(n)=depth & h(n) is Manhattan distances of numbered tiles to goal positions.
                j = 0
                while j<len(frontier) and flag:
                   # print(xcu,j,child.f,frontier[j].f,child.f>=frontier[j].f)
                    if child.f>frontier[j].f:
                        frontier.insert(j,child)
                        flag = False
                    j+=1
                if flag:
                    frontier.append(child)
                
                
#    for ch in frontier:
#        print(ch.returnArray(),ch.f)
#    sys.exit()