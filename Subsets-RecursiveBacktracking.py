# Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.


    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []

        def subset_helper(i):
            if i >= len(nums):
                subsets.append(subset.copy())
                return
            
            subset.append(nums[i])
            subset_helper(i+1)

            subset.pop()
            subset_helper(i+1)

        subset_helper(0)

        return subsets
