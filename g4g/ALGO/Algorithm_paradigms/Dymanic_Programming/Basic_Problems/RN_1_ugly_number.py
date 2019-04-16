''' Ugly numbers '''

'''
   Ugly numbers are numbers whose only prime factors are 2, 3 and 5.
   The sequence: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15 ... shows the first 11
   ugly numbers. By convention, 1 is included
'''

'''
   To check if a number is ugly, divide the number by greatest divisible powers
   of 2, 3, and 5. If the number becomes 1, then it is an ugly number.
   eg: 300.
   Greatest divisible power of 2 is 4, after dividing 300 by 4 , we get 75.
   Greatest divisible power of 3 is 3, after dividing 75 by 3 , we get 25.
   Greatest divisible power of 5 is 25, after dividing 25 by 25 , we get 1.
'''

# Method 1
# Loop for all positive numbers until ugly count is smaller than n, if integer
# is ugly, increment count by 1

def max_divide(a, b):
    while a % b == 0:
        a = a /b
    return a

def is_ugly(n):
    n = max_divide(n, 2)
    n = max_divide(n, 3)
    n = max_divide(n, 5)
    return 1 if n == 1 else  0

def nth_ugly_number(n):
    i = 1
    count = 1
    while n > count:
        i += 1
        if is_ugly(i):
            count += 1
    return i

print '150th ugly no is', nth_ugly_number(150)


# METHOD 2: DYNAMIC PROGRAMMING
'''
   1) Declare an array for ugly number. ugly[n]
   2) Initialize first ugly no: ugly[0] = 1
   3) Initialize three array index, i2, i3, i5 = 0
   4) Initialize 3 choices for the next ugly number:
        next_multiple_of_2 = ugly[i2]*2
        next_multiple_of_3 = ugly[i3]*3
        next_multiple_of_5 = ugly[i5]*3
   5) Now loop to fill all ugly number till 150.
   Now go in a loop to fill all ugly numbers till 150:
    For (i = 1; i < 150; i++ ) 
    {
        /* These small steps are not optimized for good 
        readability. Will optimize them in C program */
        next_ugly_no  = Min(next_mulitple_of_2,
                            next_mulitple_of_3,
                            next_mulitple_of_5); 

        ugly[i] =  next_ugly_no       

        if (next_ugly_no  == next_mulitple_of_2) 
        {             
            i2 = i2 + 1;        
            next_mulitple_of_2 = ugly[i2]*2;
        } 
        if (next_ugly_no  == next_mulitple_of_3) 
        {             
            i3 = i3 + 1;        
            next_mulitple_of_3 = ugly[i3]*3;
        }            
        if (next_ugly_no  == next_mulitple_of_5)
        {    
            i5 = i5 + 1;        
            next_mulitple_of_5 = ugly[i5]*5;
        } 
        
    }/* end of for loop */ 
    6.return next_ugly_no
'''

def nth_ugly_number_DP(n):
    ugly = [0] * n

    ugly[0] = 1

    i2 = i3 = i5 = 0

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, n):
        ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        print 'I is', i
        if ugly[i] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
            print 'next_multiple_of_2', next_multiple_of_2
        if ugly[i] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
            print 'next_multiple_of_3', next_multiple_of_3
        if ugly[i] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
            print 'next_multiple_of_5', next_multiple_of_5
        print ugly
        print '-----------'

nth_ugly_number_DP(11)