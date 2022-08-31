number_of_temps = int(input(""))
temps_input = input("")
temps_string = temps_input.split()
x = 0
for i in temps_string:
    if int(i) < 0:
        x += 1
print(x)