'''
- Leetcode URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solution2():
            """
            Traverse from top to down until q and q not got to same path
            
            - time complexity: O(h) where h is the height of BST
            - space complexity: O(1)
            """
            curr = root
            while curr:
                if curr.val < p.val and curr.val < q.val:
                    curr = curr.right
                elif curr.val > p.val and curr.val > q.val:
                    curr = curr.left
                else:
                    return curr
                
        def solution1():
            """
            To find the target node form the root and write down the node when traversing down.
            To compare with the node paths of p aand q, the first common node is what we want

            - time complexity: O(h)
            - space complexity: O(h)
            """
            def find(node):
                parents = []
                current = root
                while current.val != node.val:
                    parents.append(current)
                    if current.val <= node.val:
                        current = current.right
                    else:
                        current = current.left
                parents.append(node)
                return parents
            
            p_parents, q_parents = find(p), find(q)
            
            val_mapping = {}
            for i in p_parents:
                val_mapping[i.val] = True
            
            for j in q_parents[::-1]:
                if val_mapping.get(j.val):
                    return j
        
        return solution2()
    