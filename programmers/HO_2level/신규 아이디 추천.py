def solution(new_id):
    
    ava = 'abcdefghijklmnopqrstuvwxyz1234567890-_.'
    ans = ''
    new_id = new_id.lower()
    for i in range(len(new_id)):
        if new_id[i] in ava:
            if new_id[i] == '.':
                if ans != '':
                    if ans[-1] == '.': continue
                    else: ans += new_id[i]
                else: ans += new_id[i]
            else:
                ans += new_id[i]
    
    if ans[0] == '.':
        ans = ans.replace('.', '', 1)
    if len(ans) >= 1 and ans[-1] == '.':
        ans = ans.rstrip(".")
        
    if ans == '':
        ans += 'a'
        
    if len(ans) >= 16:
        ans = ans[0:15]
        if ans[-1] == '.': 
            ans = ans.rstrip(".")
        
    if len(ans) == 2:
        ans += ans[-1]
    elif len(ans) == 1:
        ans += ans[-1]
        ans += ans[-1]
        
    return ans