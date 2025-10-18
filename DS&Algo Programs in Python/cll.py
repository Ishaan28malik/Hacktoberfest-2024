class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None
        self.preval = None

class CLinkedList:
    def __init__(self):
        self.headval = None

    def AtBeginning(self, newdata):
        if self.headval == None:
            NewNode = Node(newdata)
            self.headval = NewNode
        else:
            NewNode = Node(newdata)
            temp = self.headval
            while temp.nextval is not None:
                if temp.nextval == self.headval:
                    break
                temp = temp.nextval

            NewNode.preval = temp
            NewNode.nextval = self.headval
            self.headval.preval = NewNode
            self.headval = NewNode
            temp.nextval = self.headval

    def removeEnd(self):
        temp = self.headval
        if temp == None:
            return
        else:
            while temp.nextval is not None:
                if temp.nextval.nextval == self.headval:
                    break
                temp = temp.nextval
            temp.nextval = self.headval
            self.headval.preval = temp


    def listprint(self):
        temp = self.headval
        if temp == None:
            return
        else:
            while temp.nextval is not None:
                print(temp.dataval)
                if temp.nextval == self.headval:
                    break
                temp = temp.nextval
