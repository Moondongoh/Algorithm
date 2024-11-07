# # 정답 ㅇ but 시간초과
# r = int(input())
# cnt = 0
# cnt2 =0
# def fib(a):
#     global cnt
#     global cnt2
#     if a == 0 :
#         #print("0")
#         cnt +=1
#         return cnt
#     elif a == 1:
#         #print("1")
#         cnt2 +=1
#         return cnt2
#     else:
#         return fib(a-1) + fib(a-2)

# for i in range(r):
#     a = int(input())
#     fib(a)
#     print(cnt, cnt2)
#     cnt=0
#     cnt2=0
    
r = int(input())
cnt = 0  # fib(0) 호출 횟수
cnt2 = 0 # fib(1) 호출 횟수
memo = {0: (1, 0), 1: (0, 1)}  # (fib(0) 호출 횟수, fib(1) 호출 횟수)

def fib(a):
    global cnt, cnt2
    if a in memo:
        # 메모이제이션에 저장된 호출 횟수를 반환
        return memo[a]
    # 예를 들어서 fib(5)를 구한다고 할때
    # f(5)=f(4)+f(3)으로 바뀌고
    # f(4)=f(3)+f(2)
    # f(3)=f(2)+f(1)
    # f(2)=f(1)+f(0)
    
    # 우리는 f(2)는 1과 0이 한번씩
    # f(3)은 f(2)의 값과 f(1)즉 1이 2번 0이 한번 나오는걸 알 수 있다.
    # 바로 밑에 계산을 통해서 해당 f()의 값의 0과 1이 몇번 나오는지를 파악하고
    # cnt_from_0과_1을 이용해 총 몇번 나온지를 합산해서 메모이제이션에 저장 후 계속 호출해 저장된 값을 사용한다.
    
    cnt_from_0_a_minus_1, cnt_from_1_a_minus_1 = fib(a-1) # 각 f(0) f(1)의 갯수 파악
    cnt_from_0_a_minus_2, cnt_from_1_a_minus_2 = fib(a-2)
    
    cnt_from_0 = cnt_from_0_a_minus_1 + cnt_from_0_a_minus_2
    cnt_from_1 = cnt_from_1_a_minus_1 + cnt_from_1_a_minus_2
    
    # 메모이제이션에 저장
    memo[a] = (cnt_from_0, cnt_from_1)
    return memo[a]

for i in range(r):
    a = int(input())
    cnt, cnt2 = fib(a)
    print(cnt, cnt2)
    cnt = 0
    cnt2 = 0