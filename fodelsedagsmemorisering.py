friends = int(input())
birthday = {}
while friends > 0:
        userinput= input()
        userinput = userinput.split()
        if userinput[2] in birthday:
            if int(birthday[userinput[2]][1]) < int(userinput[1]):
                birthday[userinput[2]] = (userinput[0] , userinput[1])
        else:
            birthday[userinput[2]] = (userinput[0], userinput[1])
        friends -=1
print(len(birthday))
lol = []
for i in birthday:
    lol.append(birthday[i][0])
lol.sort()
for i in lol:
    print(i)