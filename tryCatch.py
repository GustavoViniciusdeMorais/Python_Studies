def math(a, b, operand):
    result = eval("{} {} {}".format(a, operand, b))
    return result

try:
    a = raw_input('a: ')
    b = raw_input('b: ')
    operand = raw_input('operand: ')
    result = math(a, b, operand)
    print("Result: {}".format(result))
except:
    print("Some error has ocorred")