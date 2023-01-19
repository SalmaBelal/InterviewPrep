#Have the function PlusMinus(num) read the num parameter being passed which will be a combination of 1 or more single digits, and determine if it's possible to separate the digits with either a plus or minus sign to get the final expression to equal zero. For example: if num is 35132 then it's possible to separate the digits the following way, 3 - 5 + 1 + 3 - 2, and this expression equals zero. Your program should return a string of the signs you used, so for this example your program should return -++-. If it's not possible to get the digit expression to equal zero, return the string not possible. If there are multiple ways to get the final expression to equal zero, choose the one that contains more minus characters. For example: if num is 26712 your program should return -+-- and not +-+-. Sample Test Cases: Input: 199 Output: not possible Input: 26712 Output: -+--


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
        
        
        s2 = plusMinusRec(arr[1:], total - arr[0])
        if s2 != 'not possible':
            return '-' + s2
            
        s1 = plusMinusRec(arr[1:], total + arr[0])
        if s1 != 'not possible':
            return '+' + s1
            
        return'not possible'
            
    return plusMinusRec(arr[1:], arr[0])
 

print(plusMinus(26712))
