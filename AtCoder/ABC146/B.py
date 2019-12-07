n=int(input())
s=input()
max_code=ord('Z')
converted = ''

for item in s:
    code = ord(item)
    code += n
    if code > max_code:
        code -= 26
    converted = converted + chr(code)

print(converted)

