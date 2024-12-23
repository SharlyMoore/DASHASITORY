def read_file(example):
    try:
        with open(example, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Файл не найден.")

read_file('example.txt')