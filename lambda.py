import urllib2

test = lambda a, b: a + b
request = lambda: urllib2.urlopen('https://www.google.com').read()

firstExample = test(2,6)
print("First example: {}".format(firstExample))

secondExample = request()
print("Second example: {}".format(secondExample))