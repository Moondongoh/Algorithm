## 
# cnt =0
# a = int(input())

# arr = list(map(int, input().split()))  # 한 줄로 입력받아 정수 리스트로 변환

# b = int(input())

# for i in range(a):
#     if(arr[i] == b):
#         cnt +=1
# print(cnt)

# arr = list(map(int, input().split()))  # 한 줄로 입력받아 정수 리스트로 변환

## 배열에서 숫자 찾아 제거하고 출력
# list = []

# for i in range(30):
#     list.append(i+1)
    
# #print(list)

# for i in range(28):
#     s=int(input())
#     list.remove(s)

# print(list[0])
# print(list[1])

# 행렬 덧셈

# a,b = map(int, input().split())

# print(a,b)

# arr = []

# for i in range(a):
#     arr.append([])
#     x = int(input().split())
#     arr[i].append(x)
#     for j in range(b-1):
#         y = int(input().split())
#         arr[i].append(y)

# print(arr)

## 행렬 덧셈
# a, b = map(int, input().split())

# arr1 = [[0] * b for _ in range(a)]
# arr2 = [[0] * b for _ in range(a)]
# result = [[0] * b for _ in range(a)]

# for i in range(a):
#     row_values = list(map(int, input().split()))
#     for j in range(b):
#         arr1[i][j] = row_values[j]

# for i in range(a):
#     row_values = list(map(int, input().split()))
#     for j in range(b):
#         arr2[i][j] = row_values[j]

# for i in range(a):
#     for j in range(b):
#         result[i][j] = arr1[i][j] + arr2[i][j]


# for i in range(a):
#     for j in range(b):
#         print(result[i][j], end=" ") 

#function

def cal(a,b):
    sum = 0
    #a,b = map(int, input().split())
    sum = (a+b)*(a-b)
    return sum

a,b = map(int, input().split())
print(cal(a,b))