#입력으로 주어지는 리스트 x 의 첫 원소와 마지막 원소의 합을 리턴하는 함수 solution() 을 완성하세요.

def solution(x):
    answer = 0
    leng=len(x)
    for i in x:
        if i == x[0]:
            answer +=i
        elif i == x[leng-1]:
            answer +=i
            
    return answer 