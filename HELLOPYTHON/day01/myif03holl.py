import random
mine = input("홀/짝을 입력하세요")

rnd = random.random()

com = ""
if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

result = ""
if com == mine:
    result = "이김"
else:
    result = "짐"

print("com:"+com)
print("mine:"+mine)
print("result:"+result)
