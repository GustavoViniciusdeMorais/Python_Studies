import urllib2

test = lambda a, b: a + b
request = lambda: urllib2.urlopen('https://www.google.com').read()
myLength = lambda value: len(value)

firstExample = test(2,6)
print("First example: {}".format(firstExample))

lenString = myLength('gustavo')
print("String length is {}".format(lenString))

secondExample = request()
print("Second example: {}".format(secondExample))