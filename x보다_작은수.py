result = list(map(int, input().split()))
#print(result)

num1= result[0]
num2= result[1]

arr = list(map(int, input().split()))
#print(arr)
a = len(arr)

#print(a)

for i in arr:
    if(i<num2):
        print(i, end=" ")