#Given an integer array nums that may contain duplicates, return all possible subsets(the power set). The solution set must not contain duplicate subsets. Return the solution in any order.


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        subsets = []
        subset = []

        def helper(i):

            if i == len(nums):
                subsets.append(subset.copy())
                return

            subset.append(nums[i])
            helper(i+1)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i = i+1

            helper(i+1)

        helper(0)
        return subsets
