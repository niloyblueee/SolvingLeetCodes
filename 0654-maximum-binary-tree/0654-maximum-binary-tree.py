class Solution:

    def constructMaximumBinaryTree(self, nums):
        return self.real_construct(nums, 0, len(nums) - 1)

    def real_construct(self, nums, left, right):
        if left > right:
            return None

        max_val = max(nums[left:right+1])
        idx = nums.index(max_val, left, right+1)  # get index in the correct slice
        root = TreeNode(max_val)
        root.left = self.real_construct(nums, left, idx - 1)
        root.right = self.real_construct(nums, idx + 1, right)
        return root