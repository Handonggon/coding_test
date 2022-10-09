from itertools import permutations
import re

def solution(expression):
    answer = []
    operator_list = []
    for i in expression : 
        if i in ['+','-','*'] :
            operator_list.append(i)
    operator_list = list(set(operator_list))
    operator_list = list(permutations(operator_list,len(operator_list)))
    expression = re.split('([+*-])',expression)
    
    """ operator_list = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')] """
    
    for operator in operator_list :
        post_stack = []
        operator_stack = []
        for i in expression :
            if i in operator :
                if len(operator_stack) == 0 :
                    operator_stack.append(i)
                else :
                    while (len(operator_stack) > 0 and 
                    operator.index(operator_stack[-1]) <= operator.index(i)) :
                        post_stack.append(operator_stack.pop())
                    operator_stack.append(i)
            else :
                post_stack.append(i)
        while len(operator_stack) != 0 :
            post_stack.append(operator_stack.pop())
        
        result = []
        for i in post_stack :
            if i in operator :
                temp = [result.pop(),i,result.pop()]
                temp.reverse()
                temp = ''.join(temp)
                result.append(str(eval(temp)))
            else :
                result.append(i)
        answer.append(abs(int(result[0])))
    
    return max(answer)
