class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None

class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False

class BST:
    def __init__(self, node):
        self.Root = node
        self.count = 1

    def FindNodeByKey(self, key):
        result = BSTFind()
        node = self.Root
        while node is not None:
            if node.NodeKey == key:
                result.Node = node
                result.NodeHasKey = True
                return result
            elif key < node.NodeKey:
                if node.LeftChild is None:
                    result.Node = node
                    result.ToLeft = True
                    return result
                else:
                    node = node.LeftChild
            elif key > node.NodeKey:
                if node.RightChild is None:
                    result.Node = node
                    return result
                else:
                    node = node.RightChild
        return result
    
    def AddKeyValue(self, key, val):
        node = self.FindNodeByKey(key)
        if node.NodeHasKey:
            return False
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
        elif node.ToLeft:
            node.Node.LeftChild = BSTNode(key, val, node.Node)
        else:
            node.Node.RightChild = BSTNode(key, val, node.Node)
        self.count += 1
        return True
    
    def FinMinMax(self, FromNode, FindMax):
        if self.Root is not None:
            if FindMax:
                while FromNode.RightChild is not None:
                    FromNode = FromNode.RightChild
            else:
                while FromNode.LeftChild is not None:
                    FromNode = FromNode.LeftChild
        return FromNode

    def FindPrePostNode(self, node):
        if node.RightChild is not None:
            return self.FinMinMax(node.RightChild, False)
        parent = node.Parent
        while parent is not None and node == parent.RightChild:
            node = parent
            parent = parent.Parent
        return parent
    
    def FindNewNode(self, node):
        new_node = None
        if node.LeftChild == None or node.RightChild == None:
            new_node = node
        else:
            new_node = self.FindPrePostNode(node)
        return new_node
    
    def FindNewChild(self, node):
        new_child = None
        if node.LeftChild != None:
            new_child = node.LeftChild
        else:
            new_child = node.RightChild
        return new_child
    
    def ConnectParentAndChild(self, new_node, new_child):
        if new_child != None:
            new_child.Parent = new_node.Parent
        if new_node.Parent == None:
            self.Root = new_child
        elif new_node == new_node.Parent.LeftChild:
            new_node.Parent.LeftChild = new_child
        else:
            new_node.Parent.RightChild = new_child
    
    def DeleteNodeByKey(self, key):
        node = self.FindNodeByKey(key).Node
        if node.NodeKey != key:
            return False
        new_node = self.FindNewNode(node)
        new_child = self.FindNewChild(new_node)
        self.ConnectParentAndChild(new_node, new_child)
        if new_node != node:
            node.NodeKey = new_node.NodeKey
            node.NodeValue = new_node.NodeValue
        self.count -= 1
        return True
    
    def Count(self):
        if self.count and self.Root is None:
            self.count -= 1
        return self.count
    
    def In_Order(self, nodes, root):
        if root is not None:
            self.In_Order(nodes, root.LeftChild)
            nodes.append(root)
            self.In_Order(nodes, root.RightChild)
        return nodes

    def Pre_Order(self, nodes, root):
        if root is not None:
            nodes.append(root)
            self.Pre_Order(nodes, root.LeftChild)
            self.Pre_Order(nodes, root.RightChild)
        return nodes

    def Post_Order(self, nodes, root):
        if root is not None:
            self.Post_Order(nodes, root.LeftChild)
            self.Post_Order(nodes, root.RightChild)
            nodes.append(root)
        return nodes

    def Deep_All_Nodes(self, p):
        if p == 0:
            return self.In_Order([], self.Root)
        elif p == 1:
            return self.Post_Order([], self.Root)
        elif p == 2:
            return self.Pre_Order([], self.Root)

    def Wide_All_Nodes(self):
        nodes = [self.Root]
        if self.Root is not None:
            for i in nodes:
                if i.LeftChild is not None:
                    nodes.append(i.LeftChild)
                if i.RightChild is not None:
                    nodes.append(i.RightChild)
        return nodes