class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        res = []

        def dfs(node, path):
            if not node:
                return

            # Add current node's value to the path
            path += str(node.val)

            # If it's a leaf, save the path
            if not node.left and not node.right:
                res.append(path)
            else:
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return res
