from itertools import permutations #배열만들기위해 이터툴 알맞는거 불러옴
def prime(n):
    for i in range(2,n//2):
        if n%i == 0 and n!=i:
            return False
    if n == 0 or n == 1 or n == 4: #처리하기 까다로운 0과1과4는 예외로 처리
        return False
    
    return True

def solution(numbers):
    list_n=[] #배열이 ('1','3','4') 이런식으로되어있어서 '134' 로 만들고 집어넣을 리스트
    for j in range(len(numbers),1,-1):
        number = list(permutations(numbers,j))
        for i in number:
            list_n.append("".join(i))
            
    list_a = []  #list_n에서 소수인걸 옮겨넣기위한 리스트
    for i in list_n:
        if prime(int(i)):
            list_a.append(int(i))
            
    for i in numbers: #permutations가 튜플형태로 뱉어내서 한자리 숫자는 처리하기 어려워서 한자리숫자는 따로 처리
        if prime(int(i)):
            list_a.append(int(i))
    answer = list(set(list_a)) #중복되는 값은 set으로 처리
    return len(answer)