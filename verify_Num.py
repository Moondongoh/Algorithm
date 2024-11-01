Num = input()

words = Num.split()
#print(words)
length = len(words)
#print(length)

result = 0
for i in words:
    result += int(i) ** 2

print(result%10)
# a = []
# for i in str(Num):
#     a.append(i)
# length = len(a)

# result = 0
# for i in Num:
#     result += int(i) ** 2

# print(result%10)