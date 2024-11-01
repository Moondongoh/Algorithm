Num = int(input())

if (Num%4 ==0 and(Num%400 ==0 or Num%100 !=0)):
    print("1")
else:
    print("0")