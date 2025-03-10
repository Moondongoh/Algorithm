class jss:
    def __init__(self):
        self.name = input("이름을 입력하세요: ")
        self.age = input("나이를 입력하세요: ")
    def show(self):
        print(f"이름: {self.name}, 나이: {self.age}")

jss1 = jss()
jss1.show()

class jss2(jss):
    def __init__(self):
        super().__init__() #jss를 의미 name, age을 갖고옴
        self.gender = input("성별을 입력하세요: ")
    def show(self):
        print(f"이름: {self.name}, 성별: {self.gender} 나이: {self.age}")

a = jss2()
a.show()