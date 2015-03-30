ls = [1, 2, 5, 4, 25, 7, 84, 67, 25, 24, 32, 13, 24, 25, 32, 34]

def last_odd(list_num):
    result = ''
    list_two = []
    print 'Before Odd Removed'
    print list_num
    print '-----------------------------------------------------------'
    for take, num in reversed(list(enumerate(list_num))):
        if num % 2 == 1:
            list_num.pop(take)
            result += str(num)
            print 'Last Odd - ' + str(result)
            print 'After Last Odd Removed'
            print list_num
            print '-------------------------------------------------------'
            quit()

last_odd(ls)