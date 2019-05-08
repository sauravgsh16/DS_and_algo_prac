def timeConversion(s):
    #
    # Write your code here.
    #
    dur = s[-2]
    split = s.split(':')
    if dur.lower() == 'p':
        if int(split[0]) != 12:
            split[0] = str(int(split[0]) + 12)
    else:
        if split[0] == '12':
            split[0] = '00'
    newTime = ':'.join(split[:-1])
    newTime += ':'
    for i in split[-1]:
        if not i.isalpha():
            newTime += i
    print newTime


timeConversion('01:05:45PM')
