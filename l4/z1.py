from time import sleep, time

def measure_time(func):
    def func_wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('Execution took', time() - start, 's')
        return result

    return func_wrapper

@measure_time
def test_func():
    sleep(3)
    return 1

print(test_func())

