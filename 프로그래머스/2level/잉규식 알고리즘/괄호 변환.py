def recursion(p) :
    if p == '' :
        return ''
    else :
        string_u = ''
        for i in range(len(p)) :
            string_u += p[i]
            if string_u.count('(') == string_u.count(')') :
                break
        string_v = p[i+1:]
        temp_string = ''
        for i in string_u :
            if i == ')' and len(temp_string) > 0 :
                temp_string = temp_string[1:]
            else :
                temp_string += i
        if len(temp_string) > 0 :
            result = '('
            result += recursion(string_v)
            result += ')'
            string_u = string_u[1:-1]
            reverse_u = ''
            for element in string_u :
                if element == '(' :
                    reverse_u += ')'
                else :
                    reverse_u += '('
            result += reverse_u
            return result
        else :
            return string_u + recursion(string_v)
            
def solution(p):
    return recursion(p)