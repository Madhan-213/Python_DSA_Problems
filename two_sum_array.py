class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target

    def show(self):
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.target == self.target:
                    return [i, j]


# object creation
num = Solution()

# input
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 12

# method call
num.twoSum(arr, target)
result = num.show()

print(result)
