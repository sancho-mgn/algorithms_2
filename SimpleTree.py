class SimpleTreeNode:
    
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []

class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, Parent_Node, New_Child):
        if Parent_Node is not None:
            Parent_Node.Children.append(New_Child)
            New_Child.Parent = Parent_Node
        else:
            self.Root = New_Child

    def DeleteNode(self, Node_to_Delete):
        if Node_to_Delete.Parent is not None:
            Node_to_Delete.Parent.Children.remove(Node_to_Delete)
    
    def GetAllNodes(self):
        nodes = []
        if self.Root is not None:
            nodes = [self.Root]
            for node in self.Root.Children:
                subtree = SimpleTree(node).GetAllNodes()
                for i in subtree:
                    nodes.append(i)
        return nodes

    def FindNodesByValue(self, val):
        nodes = []
        if self.Root is not None:
            if self.Root.NodeValue == val:
                nodes = [self.Root]
            for node in self.Root.Children:
                subtree = SimpleTree(node).FindNodesByValue(val)
                for i in subtree:
                    if i.NodeValue == val:
                        nodes.append(i)
        return nodes
    
    def MoveNode(self, Original_Node, New_Parent):
        if Original_Node.Parent is not None:
            self.DeleteNode(Original_Node)
            Original_Node.Parent = New_Parent
            New_Parent.Children.append(Original_Node)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        count = 0
        for i in self.GetAllNodes():
            if not len(i.Children):
                count += 1
        return count
    
    def NodeLevel(self, node):
        lvl = 0
        while node.Parent is not None:
            node = node.Parent
            lvl += 1
        return lvl
 
    def SubTreeSize(self, node):
        count = 1
        for child in node.Children:
            count += self.SubTreeSize(child)
        return count
    
    def FindEvenTrees(self, node, result):
        for child in node.Children:
            size = self.SubTreeSize(child)
            if size % 2 == 0:
                result.append(child.Parent)
                result.append(child)
            self.FindEvenTrees(child, result)
        return result

    def EvenTrees(self):
        return self.FindEvenTrees(self.Root, [])