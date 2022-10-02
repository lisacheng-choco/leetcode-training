from email.errors import ObsoleteHeaderDefect
from typing_extensions import Self


class BSTNode(object):
    def __init__(self, parent, k) -> None:
        """ Creates a node

        Args:
            parent: The node's parent
            k: The node's key
        """
        self.k = k
        self.parent = parent
        self.left = None
        self.right = None

    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width
    def __str__(self):
        return '\n'.join(self._str()[0])

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this 
        node.
        
        Args:
            k: The key of the node we want to find.
        
        Returns:
            The node with key k.
        """
        if k == self.key:
            return self
        
        if k < self.key:
            if self.key.left is None:
                return None
            return self.left.find(k)
        
        if k > self.key:
            if self.key.right is None:
                return None
            return self.right.find(k)
        
    def find_min(self):
        """Finds the node with the minimum key in the subtree rooted at this 
        node.
        
        Returns:
            The node with the minimum key.
        """
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr
    
    def next_larger(self):
        """Returns the node with the next larger key (the successor) in the BST.
        """
        # case 1: If node's right child exist
        if self.right is not None:
            return self.right.find_min()
        
        # case 2: If node's right child doesn't exist
        curr = self
        while curr.parent is not None and curr == curr.parent.right:
            curr = self.parent
        return curr.parent
    
    def insert(self, node):
        """Inserts a node into the subtree rooted at this node.
        
        Args:
            node: The node to be inserted.
        """
        if node.k < self.k:
            if self.left is not None:
                self.left.insert(node)
            else:
                node.parent = self
                self.left = node
        else:
            if self.right is not None:
                self.right.insert(node)
            else:
                node.parent = self
                self.right = node

    def delete(self):
        """Deletes and returns this node from the BST.
        case 1: if node has no child
        case 2: if node has 1 child
        case 3: if node has 2 children
        """
        # case 1, 2
        if self.left is None or self.left is None:
            
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        # case 3
        else:
            s = self.next_larger()
            s.k, self.k = self.k, s.k
            return s.delete()



        # case 3


