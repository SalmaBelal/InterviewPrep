
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
