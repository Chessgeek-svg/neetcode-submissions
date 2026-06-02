class Treenode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = Treenode(key, val)
            return None
        
        curr = self.root
        while curr:
            if key > curr.key:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Treenode(key, val)
                    return None
            elif curr.key > key:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Treenode(key, val)
                    return None
            else:
                curr.val = val
                return None

    def get(self, key: int) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.val
        
        return -1



    def getMin(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr: Treenode, key: int) -> Treenode:
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                temp = curr.right
                while temp.left:
                    temp = temp.left
                curr.key = temp.key
                curr.val = temp.val
                curr.right = self.removeHelper(curr.right, temp.key)
        return curr



    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorder(self.root, res)
        return res
    
    def inorder(self, root: Treenode, res: List[int]):
        if not root:
            return None

        self.inorder(root.left, res)
        res.append(root.key)
        self.inorder(root.right, res)
    



