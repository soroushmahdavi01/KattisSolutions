tries = int(input(""))
answer = 0
while tries > 0:
  x = input("")
  y = x[-1]
  base = x[0:-1]
  answer += int(base) ** int(y)
  tries -= 1

print(answer)
