# file = open('newfile.txt', 'r')

# f = file.readlines()

# newlist = []

# for line in f:
#     newlist.append(line.strip())

# file.close()

# print(newlist)

file = open('write.txt', 'w')

file.write('ghost\n')
file.write('I am learning how to write to a file')

file.close()

