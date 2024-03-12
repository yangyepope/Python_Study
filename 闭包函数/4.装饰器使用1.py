import time





def run_decorator(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()

        print("during", end_time - start_time)

    return inner


@run_decorator
def run():
    time.sleep(5)
    print("OK")
