''' Maximum and minimum sums from two numbers with digit replacements '''

'''
   Only allowed to replace 5 with 6 and vice-versa

   Eg: x = 645, y = 666
   min = 545 + 555
   max = 646 + 666
'''

def replace_digit(x, from1, to):
    result = 0
    mul = 1

    while x % 10 > 0:
        remainder = x % 10

        if remainder == from1:
            result = result + to * mul
        else:
            result = result + remainder * mul
        
        mul *= 10
        x = int(x / 10)
    return result


def max_and_min(x, y):

    min_sum = replace_digit(x, 6, 5) + replace_digit(y, 6, 5)
    max_sum = replace_digit(x, 5, 6) + replace_digit(y, 5, 6)

    print 'Max:', max_sum
    print 'Min:', min_sum

max_and_min(5466, 4555)
