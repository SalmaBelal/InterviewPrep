
# Sure, here's a simple example of a recursive backtracking algorithm to generate all possible permutations of a given string. This will contain duplicates

def permute(string):
    def permuteHelper(string, permutation, permutations):
        
        if len(string) == 1:
            permutation += string
            permutations.append(permutation)
            return
            
        for i in range(len(string)):
            permuteHelper(string[:i] + string[i+1:], permutation + string[i], permutations)
        
    all_permutations = []
    permuteHelper(string, "", all_permutations)
    print(all_permutations)
    
permute("abc")


#This wont contain duplicates



def permute(string):
    def permuteHelper(string, permutation, permutations):
        
        if len(string) == 1:
            permutation += string
            permutations.add(permutation)
            return
            
        for i in range(len(string)):
            permuteHelper(string[:i] + string[i+1:], permutation + string[i], permutations)
        
    all_permutations = set({})
    permuteHelper(string, "", all_permutations)
    print(all_permutations)
    
permute("abc")


#not using string...list of lists
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        result = []
        
        def helper(arr):
            if len(arr) == 0:
                result.append(permutation.copy())

            for i in range(len(arr)):
                permutation.append(arr[i])
                helper(arr[:i] + arr[i+1:])
                permutation.pop()

        helper(nums)

        return result
    
#another way of not using string instead list of lists

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1 :
            return [nums[:]]

        result = []
        for i in range(len(nums)): 
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n) 

        return result

