text = input('Напишите текст: ')
with open('user_input.txt', 'w') as file:
    file.write(text)
    #заменить "w" на "a"