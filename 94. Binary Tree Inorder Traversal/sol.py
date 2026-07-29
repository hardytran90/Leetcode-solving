from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []
        node = root
        while node or stack:
            # Go as far left as possible, stacking nodes along the way.
            while node:
                stack.append(node)
                node = node.left
            # Visit the node, then move into its right subtree.
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Dựng cây từ list level-order (kiểu LeetCode) thành đối tượng TreeNode."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root

if __name__ == "__main__":
    solution = Solution()

    root = build_tree([1, None, 2, 3])
    result1 = solution.inorderTraversal(root)
    print(result1)
