"""
// Time Complexity : O(n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
Given below
"""
class Solution:
    def calculate(self, s: str) -> int:
        """
        32 * 5 + 6 / 4 - 5 * 6           stk = [160,1,-30]  = 131
                             |
        num = 0
        sign = '*'
        
        
        Most important thing to tackle is ensuring operator preference
        Update
        Idea is to process only when we have a sign * or / already occured while processing the string, since we cannot operate on + or - due to lower precedence
        Algo
            Initial configuration -> sign = +, num = 0
            Iterate over the string
                - if char is digit
                    Update the num  -> num = num * 10 + digit
                - if char is not digit and it's not blank  or it's one but last char
                    - sign = +  -> push num o stack
                    - sign = - -> push -num to stack
                    - sign = * -> push (stk.pop() * num) to stack
                    - sign = / -> push (stk.pop() / num) to stack
                    - Update the sign = ch
                - reset num to 0
            Empty sth stack by adding all elements in it
        """
        stk = []
        #str_num = lambda x:int(x)
        i = 0
        num = 0
        sign = '+'
        while i < len(s):
            #if s[i] in ['+','-','*','/']:
            if s[i].isdigit():
                num = num *10 + int(s[i])
                
            if (s[i] != ' ' and not s[i].isdigit()) or i == len(s) - 1:
                if sign == '+':
                    #i +=1
                    stk.append(num)
                elif sign == '-':
                    #i +=1
                    stk.append(-num)
                elif sign == '*':
                    #i +=1
                    stk.append(stk.pop() * num)
                elif sign == '/':
                    #i +=1
                    stk.append(stk.pop() // num)
                sign = s[i]
                num = 0
            
            i+=1
        
        return sum(stk)