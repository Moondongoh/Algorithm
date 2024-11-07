## 아스키 코드 변환
# print(ord(input()))

## 길이 파악
# Input = input()

# length = len(Input)

# print(length)

# # 대문자는 소문자로 소문자는 대문자로
# Input = input()

# swap = Input.swapcase()
# print(swap)

# # 학점 부여
# Input = input()

# if(Input=='A+'):
#     print("4.5")
# elif(Input =='A0'):
#     print("4.0")
# elif(Input =='A-'):
#     print("3.7")
# elif(Input =='B+'):
#     print("3.3")
# elif(Input =='B0'):
#     print("3.0")
# elif(Input =='B-'):
#     print("2.7")
# elif(Input =='C+'):
#     print("2.3")
# elif(Input =='C0'):
#     print("2.0")
# elif(Input =='C-'):
#     print("1.7")
# elif(Input =='D+'):
#     print("1.3")
# elif(Input =='D0'):
#     print("1.0")
# elif(Input =='D-'):
#     print("0.7")
# elif(Input =='F'):
#     print("0.0")

# # 학점 부여
# grades = {
#     'A+': '4.3',
#     'A0': '4.0',
#     'A-': '3.7',
#     'B+': '3.3',
#     'B0': '3.0',
#     'B-': '2.7',
#     'C+': '2.3',
#     'C0': '2.0',
#     'C-': '1.7',
#     'D+': '1.3',
#     'D0': '1.0',
#     'D-': '0.7',
#     'F': '0.0'
# }

# Input = input()

# print(grades[Input])

# dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7',
#        'B+':'3.3', 'B0':'3.0', 'B-':'2.7',
#        'C+':'2.3', 'C0':'2.0', 'C-':'1.7',
#        'D+':'1.3', 'D0':'1.0', 'D-':'0.7',
#        'F':'0.0'}
# grade = input()
# print(dic[grade])

##
# S = input()

# num = int(input())
# print(S[num-1])

# 문자열 작성 그대로 출력
# while True:
#     try:
#         String = input()
#         print(String)
#         if String == "":
#             break
#     except EOFError:
#         break


# for i in range(int(input())):
#     s = input()
#     print(s[0]+s[-1])