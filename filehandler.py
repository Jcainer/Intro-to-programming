file = open("mark-grades.txt", "r" )
lines = file.readlines()
for line in lines:
    print(line)
file.close()
