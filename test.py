"""
if curr == p or q, return the current node
if both left and right -> the current is lca so return
if left, return left val
if right, return right val
if none, return none
need helper function to not input p and q
"""


def lca(root, p, q):
    def dfs(node):
        if not node:
            return None

        if node == q or node == p:
            return node.val

        left = dfs(node.left)
        right = dfs(node.right)

        if left and right:
            return node.val
        return left or right

    return dfs(root)
