ages = [5, 12, 18, 19, 7, 21]

def myFilter(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFilter, ages)

print("Adults ages: {}".format(adults))