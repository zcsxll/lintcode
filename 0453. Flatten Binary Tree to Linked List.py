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
        while root:
            if root.left is not None:
                zcs = root.left
                while zcs.right is not None:
                    zcs = zcs.right
                zcs.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

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
