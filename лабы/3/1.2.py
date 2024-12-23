file = open('example.txt', 'r')
while True:
    content = file.readline()
    if not content:
        break
    print(content)
file.close()