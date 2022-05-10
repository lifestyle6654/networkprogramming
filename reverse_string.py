# 인덱스를 이용하여 문자열의 문자를 역순으로 만들기

# 변수 초기화 부분 
outStr = ""
count, i = 0, 0

# 메인 코드 부분
inStr = input("Type string : ")
count = len(inStr)

for i in range(0, count):
    outStr += inStr[count - (i + 1)] # 마지막 문자부터 추출하여 저장
print("Reversed string: %s" % outStr)
