# a= int(input())

# def repeat(a):
#     if a == 1 or a ==0:
#         return 1
#     else:
#         return a * repeat(a-1)

# print(repeat(a))

## A+B-3
# # for문 안에 값은 return 하지 않으면 값을 초기화함.
# a= int(input())
# Num1 = []
# Num2 = []

# for i in range(a):
#     x, y = map(int, input().split())
#     Num1.append(x)
#     Num2.append(y)

# for i in range(a):
#     print(Num1[i] + Num2[i])

# # A+B-5
# Num1 = []
# Num2 = []

# a = 0
# b = 0
# cnt =0
# def app():
#     global a,b,cnt
#     a,b = map(int, input().split())
#     while a !=0 and b !=0:
#         Num1.append(a)
#         Num2.append(b)
#         cnt += 1
#         a, b = map(int, input().split())
#     return cnt
    
# app()

# #print(cnt)
# for i in range(cnt):
#     print(Num1[i] + Num2[i])

# # 구구단
# a = int(input())
# i = 1
# while i < 10:
#     print(f'{a} * {i} = {a*i}')
#     i += 1

## 순차 별 찍기
# a = int(input())

# for i in range(1, a+1):
#     print("*" * i)

# A+B-4

# while True:
#      try:
#          a,b =map(int, input().split())
#          print(a+b)
#      except:
#          break

# import sys

# a = int(input())
# for i in range(a):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)