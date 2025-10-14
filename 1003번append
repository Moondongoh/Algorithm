"""
결국 이문제는 0이랑 1갯수만 파악하면됌.
그래서 초기 리스트를 만들고 append를 이용해서 1의 마지막을 0에 넣고 0의 -2와 -1번째를 더해 1에 마지막에 넣는식으로
이러면 재귀식으로
zero_c = 0
one_c = 0


def fibonacci(n):
    if n == 0:
        global zero_c
        zero_c += 1
        return 0
    elif n == 1:
        global one_c
        one_c += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


list_n = []
x = int(input())

for i in range(x):
    n = int(input())
    list_n.append(n)

for i in range(len(list_n)):
    fibonacci(list_n[i])
    print(zero_c, one_c)
    zero_c = 0
    one_c = 0
이렇게 구현 안하고 빠르게 파악 가능함.
"""

list_n = []
t = int(input())

for i in range(t):
    n = int(input())
    list_n.append(n)

for n in list_n:
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    if n > 1:
        for i in range(n - 1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2] + cnt_1[-1])

    print(cnt_0[n], cnt_1[n])
