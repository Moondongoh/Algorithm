# ==========================================1003
# zero_c = 0
# one_c = 0


# def fibonacci(n):
#     if n == 0:
#         global zero_c
#         zero_c += 1
#         return 0
#     elif n == 1:
#         global one_c
#         one_c += 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# list_n = []
# x = int(input())

# for i in range(x):
#     n = int(input())
#     list_n.append(n)

# for i in range(len(list_n)):
#     fibonacci(list_n[i])
#     print(zero_c, one_c)
#     zero_c = 0
#     one_c = 0

# ==========================================1152

# x = str(input())

# count = 0

# r = x.split()
# for i in range(len(x.split())):
#     count += 1

# print(count)

# ==========================================2577
# list_x = [0] * 3
# for i in range(3):
#     list_x[i] = int(input())


# def calc(list_x):
#     result = list_x[0] * list_x[1] * list_x[2]
#     return str(result)


# for i in range(10):
#     print(calc(list_x).count(str(i)))
# ==========================================11720
# x = int(input())
# y = str(input())

# sum_x = 0
# for i in range(x):
#     sum_x += int(y[i])

# print(sum_x)
# ==========================================2562
# list_x = [0] * 9
# max_x = 0
# max_index = 0
# for i in range(9):
#     list_x[i] = int(input())
#     if list_x[i] > max_x:
#         max_x = list_x[i]
#         max_index = i
# print(max_x)
# print(max_index + 1)
# ==========================================10818
# x = int(input())
# list_x = list(map(int, input().split()))

# # for i in range(len(list_x)):
# #     print(list_x[i])
# print(min(list_x), max(list_x))
# ==========================================2920
# x = list(map(int, input().split()))
# if x == [1, 2, 3, 4, 5, 6, 7, 8]:
#     print("ascending")
# elif x == [8, 7, 6, 5, 4, 3, 2, 1]:
#     print("descending")
# else:
#     print("mixed")
# ==========================================8958
# x = int(input())

# for _ in range(x):
#     a = input().strip()
#     count = 0
#     sum = 0
#     for i in a:
#         if i == "O":
#             count += 1
#             sum += count
#         else:
#             count = 0
#     print(sum)
# ==========================================2675
x = int(input())

outs = []
for _ in range(x):
    a, s = input().split()
    a = int(a)
    outs.append("".join(ch * a for ch in s))

print("\n".join(outs))
