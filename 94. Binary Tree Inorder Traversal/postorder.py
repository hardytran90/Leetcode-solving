from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative: duyệt theo Gốc -> Phải -> Trái rồi đảo ngược
        # sẽ ra đúng Trái -> Phải -> Gốc (postorder).
        result: List[int] = []
        
        # Tránh trường hợp nếu input = [] thì stack = [None] => sẽ gây lỗi AttributeError vì NoneType không có .left hay .right
        if not root:
            return result
        
        stack: List[TreeNode] = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Đẩy trái trước, phải sau => khi pop sẽ lấy phải trước.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        result.reverse()
        return result

    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []

        def visit(node: Optional[TreeNode]) -> None:
            if not node:
                return
            visit(node.left)
            visit(node.right)
            result.append(node.val)

        visit(root)
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

    tests = [
        [1, None, 2, 3],
        [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9],
    ]
    for vals in tests:
        root = build_tree(vals)
        print(solution.postorderTraversal(root))
