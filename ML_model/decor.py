def validate(func):
  def decorated_func(number1, number2):
    if number1 < 0:
      number1 = 0

    if number2 < 0:
      number2 = 0

    return func(number1, number2)

  return decorated_func

@validate
def safe_sum(number1, number2):
  return (number1 + number2)

print(safe_sum(5, 10))
print(safe_sum(-5, 10))

def safe_exec(func):
  def decorated_func(*args):
    try:
        return func(*args)
    except:
      print("Oops, something went wrong")

  return decorated_func

@safe_exec
def safe_divide(number1, number2):
  return (number1 / number2)

safe_divide(10, 5)
safe_divide(10, 0)



import time

def log(func):
  def decorated_func(*args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    func_name = func.__name__
    print(f"[INFO] Function {func_name} executed in {execution_time}")

  return decorated_func

def factorial(number):
  if number == 1:
    return 1

  return (number * factorial(number - 1))

@log
def logged_factorial(number):
  return factorial(number)

logged_factorial(100)