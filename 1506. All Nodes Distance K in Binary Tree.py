# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of the tree
    @param target: the target
    @param K: the given K
    @return: All Nodes Distance K in Binary Tree
    """
    def distanceK(self, root, target, K):
        # Write your code here
        if K == 0:
            return [target.val]

        self.path = []
        self.find_path(root, target)
        # for node in self.path:
        #     print(node.val)

        self.ret = []
        for idx, node in enumerate(self.path):
            depth = K - idx
            self.depth_search(node, depth, target.val)
            # print(idx, self.ret)
        # print(self.ret)
        return self.ret

    def find_path(self, root, target):
        if root is None:
            return False
        if root.val == target.val:
            self.path.append(root)
            return True
        if self.find_path(root.left, target):
            self.path.append(root)
            return True
        if self.find_path(root.right, target):
            self.path.append(root)
            return True

    def depth_search(self, root, depth, target):
        if root is None:
            return
        if depth == 0:
            if root.val != target:
                self.ret.append(root.val)
            return
        if root.left not in self.path:
            self.depth_search(root.left, depth - 1, target)
        if root.right not in self.path:
            self.depth_search(root.right, depth - 1, target)

def make_tree(seq, idx):
    if idx >= len(seq) or seq[idx] == '#':
        return None
    # print(seq[idx])
    node = TreeNode(seq[idx])
    node.left = make_tree(seq, idx * 2 + 1)
    node.right = make_tree(seq, idx * 2 + 2)
    return node

if __name__ == '__main__':
    nodes = [3,5,1,6,2,0,8,'#','#',7,4]
    # nodes = [1,2,3,4]
    # nodes = [0, 2, 1, '#', '#', 3]
    root = make_tree(nodes, 0)
    ret = Solution().distanceK(root, root.left, 2)
    print(ret)