str = "My name is seungwoo sung"
reverse = ""

# 문자열의 문자수를 출력하라
str_len = len(str)
print(str_len)

# 문자열을 10번 반복한 문자열을 출력하라
for i in range(0, 10):
    print(str)

# 문자열의 첫 번쨰 문자를 출력하라
print(str[0])

# 문자열에서 처음 4문자를 출력하라
print(str[0:4])

# 문자열에서 마지막 4문자를 출력하라
print(str[-4:])

# 문자열의 문자를 거꾸로 출력하라
for i in range(str_len):
    reverse += str[str_len - (i + 1)]

print(reverse)

print(str[1 : (str_len - 1)])

# 문자를 모두 대문자로 변경하여 출력하라
print(str.upper())

# 문자를 모두 소문자로 변경하여 출력하라
print(str.lower())

# 문자열에서 'a'를 'e'로 대체하여 출력하라
print(str.replace('a', 'e'))