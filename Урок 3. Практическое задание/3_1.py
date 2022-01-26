from datetime import datetime

def timer(time_func):
    def test_time():
        start = datetime.now()
        result = time_func()
        print(datetime.now() - start)
        return result
    return test_time

@timer
def spisok():
    l = []
    for i in range(1, 10000):
        if i**2 % 2 == 0:
            l.append(i)
    return l


@timer
def dic():
    d = {}
    for i in range(1, 10000):
        if i % 2 == 0:
            d[i] = i**2
    return d



l = spisok()      # 0:00:00.003000
d = dic()         # 0:00:00.003001

# пример может быть не удачный получился, но по факту
# словарь обрабатывается медленее за счет того что когда добавляется
# информация, необходимо посчитать хеш, а всписок просто добавляется
# например в конец