# num = list(map(int, input("숫자 입력: ").split()))

# a=num

# print("정렬 전: ",a)

# def swap(x,y):
#     # temp =0
#     # temp = a[x]
#     # a[x] = a[y]
#     # a[y] = temp
#     a[x], a[y] = a[y], a[x]
#     return a[x], a[y]

# def bubblesort(a):
#     n = len(a)
#     for i in range(n-1):
#         for j in range(n-1):
#             if a[j] > a[j+1]:
#                 swap(j,j+1)
#                 swapped = True
#         if not swapped:
#             break
#     return a
            
# bubblesort(a)
# print("정렬 후: ", a)

# #1838번
# import sys
# size = int(sys.stdin.readline())
# num = list(map(int, input().split()))

# a=num

# def bubblesort(a):
#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1-i):
#             if a[j] > a[j+1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#                 swapped = True
#         if not swapped:
#             return i
#     return size

# print(bubblesort(a))

import sys	
size = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

not_sort_arr = {}
for i in range(size):
# for문 실행 후:
# not_sort_arr = {4: 0, 1: 1, 3: 2, 2: 3}
# 빈 딕셔너리에 해당 배열의 값의 위치를 매칭
    not_sort_arr[num[i]] = i

num.sort()
sort_arr = {}
for j in range(size):
    sort_arr[num[j]] = j

result = 0
for k in num:
    result = max(result, not_sort_arr[k] - sort_arr[k]) # 정렬 전과 후의 인덱스 차이 중 가장 큰 애가 찾는 값

print(result)