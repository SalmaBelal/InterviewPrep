#Have the function PlusMinus(num) read the num parameter being passed which will be a combination of 1 or more single digits, and determine if it's possible to separate the digits with either a plus or minus sign to get the final expression to equal zero. For example: if num is 35132 then it's possible to separate the digits the following way, 3 - 5 + 1 + 3 - 2, and this expression equals zero. Your program should return a string of the signs you used, so for this example your program should return -++-. If it's not possible to get the digit expression to equal zero, return the string not possible. If there are multiple ways to get the final expression to equal zero, choose the one that contains more minus characters. For example: if num is 26712 your program should return -+-- and not +-+-. Sample Test Cases: Input: 199 Output: not possible Input: 26712 Output: -+--


#plan/pseudo code
#define plusminus and have it take the int number
    #split num into array of ints
    #if array length is less than 2 return not possible
    
    #define recursive funtion that takes an array and the total sum so far
        # base case would be when array length is 1
            #if total + arr[0] == 0 return '+'
            #elif do the same for minus 
            #else return 'not possible'
            
        #now for the recursive calls
        
        #define a variable that calls the reursive function with parameters arr[1:] and the total sum - arr[0]
        #s2 = recursivefunction(arr[1:], totalsum - arr[0])
        #if s2 != not possible, return the string - in addition to the string that s2 returns
        
        # do the same but for +
        
        #if both s1 and s2 return not possible then return not possible. this is where the backtracking happenss
    

    
    
    
    
def plusMinus(num):
    arr = list(map(lambda x: int(x), list(str(num))))
    
    if(len(arr) < 2):
        return 'not possible'
  
    def plusMinusRec(arr, total):
        if len(arr) == 1 :
            if arr[0] + total == 0:
                return '+'
            elif arr[0] - total == 0:
                return '-'
            else:
                return 'not possible'
        
        #if we have more than one solution, where this is placed decides whether we return - results first 
        s2 = plusMinusRec(arr[1:], total - arr[0])
        if s2 != 'not possible':
            return '-' + s2
            
        s1 = plusMinusRec(arr[1:], total + arr[0])
        if s1 != 'not possible':
            return '+' + s1
            
        return'not possible'
            
    return plusMinusRec(arr[1:], arr[0])
 

print(plusMinus(26712))
