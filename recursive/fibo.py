# 인자로 0 또는 양의 정수인 x 가 주어질 때, Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

# Fibonacci 순열은 아래와 같이 정의됩니다.
# F0 = 0
# F1 = 1
# Fn = Fn - 1 + Fn - 2, n >= 2

# 재귀함수 작성 연습을 의도한 것이므로, 재귀적 방법으로도 프로그래밍해 보고, 반복적 방법으로도 프로그래밍해 보시기 바랍니다.

#재귀로

def solution(a):
    if a==0:
        return 0 
    if a==1:
        return 1
    else:
        return(solution(a-1)+solution(a-2))

#반복문으로
def solution(a):
    answer=0
    fibo_1=0
    fibo_2=1
    for i in range(1,a):
        answer=fibo_1+fibo_2
        fibo_1=fibo_2
        fibo_2=answer
    if(a==1):
        return 1
    return answer