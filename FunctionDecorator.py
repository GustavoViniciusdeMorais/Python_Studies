import sys

def log_result(func):
    def inner(*args):
        res = func(*args)
        print("Sum of {} and {} is {}".format(args[0], args[1], res))
        return res
    return inner

@log_result
def sum(a, b):
    return a + b

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    sum(a, b)
except:
    print("You should pass two numbers to this program")