def is_prime(number):
    if number > 1:
        for i in range(2, number//2 + 1):
            if number % i == 0:
                print('Число', number, 'составное')
                break
            else:
                print('Число', number, 'простое')
        else:
            print('Число', number, 'составное')
is_prime(73)