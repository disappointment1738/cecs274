from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        """
        If the key does not exist in this BinarySearchTree,
        adds a new node with given key and value, in the correct position.
        Returns True if the key-value pair was added to the tree, False otherwise.
        """
        # create new node with given key and val
        new = self.Node(key, value)
        # find the node that will be the parent of the new node
        parent = self._find_last(key)
        # make the new node the child of the parent
        child = self._add_child(parent, new)
        return child

    def find(self, key: object) -> object:
        """
        returns the value corresponding to the given key if the key
        exists in the BinarySearchTree, None otherwise
        """
        node = self._find_eq(key) # helper method
        if node is None: # since node is empty, it's empty
            return None
        return node.v

    def remove(self, key: object):
        """
        removes the node with given key if it exists in this BinarySearchTree.
        Returns the value corresponding to the removed key, if the key was in the tree.
        If given key does not exist in the tree, ValueError is raised.
        """
        # finds the matching key
        u = self._find_eq(key)
        if u is None:
            raise ValueError
        value = u.v # value corresponding to key
        self._remove_node(u) # helper method
        return value

    def _find_eq(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key,
        None otherwise.
        """
        # let current be the root
        current = self.r
        # visit the nodes in the tree
        while current is not None:
            # visit left child
            if key < current.k:
                current = current.left
            # visit right child
            elif key > current.k:
                current = current.right
            # return current since it's in the current node
            else:
                return current
        # there is no matching key
        return None

    def _find_last(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key, if it exists.
        Otherwise, returns the node that would have been the parent of the node
        with the given key, if it existed
        """
        current = self.r
        parent = None
        while current is not None:
            parent = current
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return parent # b/c key wasn't found in while loop

    # 3 for BookStore.py, Project 5
    def findKeyOrSmallest(self, key: object) -> BinaryTree.Node:
        """
        Method returns the node containing the given key if it exists.
        Otherwise, it returns the node with the smallest key greater than the given key.
        """
        current = self.r # current become the root
        small = None
        while current is not None:
            if key < current.k:
                small = current
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return small

    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        """
        helper method; adds node u as the child of node p, assuming node p has at most 1 child
        """
        # check the precondition: if p is nil, make u the root
        if p is None:
            self.r = u
        # determine the positioning of u
        else:
            # make u the left child
            if u.k < p.k:
                p.left = u
            # make u the right child
            elif u.k > p.k:
                p.right = u
            # cannot add since the key exists
            else:
                return False
            # set p as parent of u
            u.parent = p
        # increment num of nodes by 1
        self.n += 1
        return True

    def _splice(self, u: BinaryTree.Node):
        """
        helper method; links the parent of given node u to the child
        of node u, assuming u has at most one child
        """
        # initialize a child to be u's child
        if u.left is not None:
            child = u.left
        else:
            child = u.right

        # if u is root, make child the root and make p parent of u <- nil
        if u is self.r:
            self.r = child
            p = None
        else:
            # make p parent of u
            p = u.parent
            # check if u is child of p (left and right)
            if p.left == u:
                p.left = child # make child the left child 
            else: 
                p.right = child # make child the right child

        # assign p to child.parent
        if child is not None:
            child.parent = p # set p as child's parent
        # decrement num of nodes by 1
        self.n -= 1

    def _remove_node(self, u: BinaryTree.Node):
        # if u only has 0 or 1 child, use _splice(u)
        if u.left is None or u.right is None:
            self._splice(u)
        else: 
            w = u.right # this is largest key after u.k
            # find the node w with the next largest key
            while w.left is not None:
                w = w.left
            # replace
            u.k = w.k
            u.v = w.v
            self._splice(w) # helper method

    def clear(self):
        """
        empties this BinarySearchTree
        """
        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w