# https://github.com/AllThingsSmitty/functions-and-scope-in-javascript

file = open('C:\Users\Jobhunt\Desktop\js closure.txt', 'r')
readlines = file.readlines()

for fileName in readlines:
    # print(fileName)
    fileName = fileName.strip('\n')
    file = open(fileName, 'w')
    file.write('')
    file.close()

