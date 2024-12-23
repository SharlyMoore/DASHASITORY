class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

for i in range(12):
    k = Counter()

print('Количество экземпляров:', Counter.count)