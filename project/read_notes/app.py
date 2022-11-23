with open('C:/Users/Karol/Desktop/excel-python/project/read_notes/arquivo.txt') as f:
    content = f.readlines()

content = [x.strip('\n') for x in content]

print(content)

for line in content:
    print(line)