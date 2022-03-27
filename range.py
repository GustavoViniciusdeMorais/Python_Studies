
def example():
    for i in range(1, 10):
        mydict = {}
        var = "variable_{}".format(i)
        mydict[var] = i * 10
        print(mydict['variable_'+str(i)])

example()