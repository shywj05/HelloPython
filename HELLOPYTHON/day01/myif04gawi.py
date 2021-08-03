import random
mine = input("가위/바위/보 입력하세요")

rnd = random.random()

com = ""
if rnd > 0.3:
    com = "가위"
elif rnd > 0.6:
    com = "바위"
else:
    com = "보"

result = ""


if com == mine:
    result = "비김"
elif com =="바위" and mine=="보" or com =="가위" and mine=="바위" or com =="보" and mine=="가위":
    result = "이김"
else:
    result = "짐"
    

print("com:"+com)
print("mine:"+mine)
print("result:"+result)
