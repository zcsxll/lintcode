# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        while root: #指针副本可以被修改
            if root.left is not None: #如果有左子树
                zcs = root.left
                while zcs.right is not None: #就找到左子树“最右侧”的节点A
                    zcs = zcs.right
                zcs.right = root.right #然后把左子树插到右子树之前，如下图第一次处理后
                root.right = root.left
                root.left = None
            root = root.right

"""
原始树：
     1
    / \ 
   2   5
  / \   \ 
 3   4   6
第一次处理后：
     1
      \ 
       2
      / \		
     3   4
          \ 
           5
            \ 
             6
"""

def make_tree(seq, idx):
    if idx >= len(seq) or seq[idx] == '#':
        return None
    node = TreeNode(seq[idx])
    node.left = make_tree(seq, idx * 2 + 1)
    node.right = make_tree(seq, idx * 2 + 2)
    return node

if __name__ == "__main__":
    root = make_tree([1, 2, 5, 3, 4, '#', 6], 0)
    # print_tree(root)
    Solution().flatten(root)
