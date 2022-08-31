cpuinfo = input()
cpuinfosplit = cpuinfo.split(' ')

height = cpuinfosplit[0]
base = cpuinfosplit[1]

print((int(height) * int(base)) / 2)