import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(func):
  def speed_test():
    start = time.time()
    func()
    end = time.time()
    time_taken = end - start
    print (f'{func.__name__} took {time_taken}')
  return speed_test

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()

slow_function()