"""getLeafCount(node)
1) If node is NULL then return 0.
2) Else If left and right child nodes are NULL return 1.
3) Else recursively calculate leaf count of the tree using below formula.
    Leaf count of a tree = Leaf count of left subtree + Leaf count of right subtree"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        pass
    def InsertData(self, data):
        if self.data:
            #compare new value with the parent node => left branch / right branch
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.InsertData(data)
            elif data >= self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.InsertData(data)
        else:
            self.data = data

def getLeafCount(node):
    if node is None:
        return 0
    if (node.left is None and node.right is None):
        return 1
    return getLeafCount(node.left) + getLeafCount(node.right)


n = int(input())
dataList = []
for i in range(n):
    dataList.append(int(input()))
root = Node(dataList[0])
for d in range(1, len(dataList)):
    root.InsertData(dataList[d])

print(getLeafCount(root))