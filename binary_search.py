# Ben Jordan
# 5/14/21 Binary Search refresher

def binsearch(minimum, maximum, num):
    '''Find a target number between two boundaries consistently in the least amount of steps possible'''
    # check for invalid input
    if minimum >= maximum:
        return 'The minimum must be less than the maximum boundary'
    if num <= minimum or num >= maximum:
        return 'The target number does not fall within the specified boundaries.'
    # start counter
    count = 1
    # start list of jumps
    hops = [maximum]
    while True:
        # cut min max in half
        # floor
        check = ((maximum - minimum) // 2) + minimum
        # add the check to the hop
        hops.append(check)
        if check == num:
            # format readout
            return 'The number was {0}\nThe search took {1} tries.\n{2}'.format(check, count, ' -> '.join([str(x) for x in hops]))
        elif check > num:
            # must be in lower half
            maximum = check
        else:
            # must be in upper half
            minimum = check
        # increment counter
        count += 1

print(binsearch(0, 100, 6))
# 100 > 50 > 25 > 12 > 6 (4 steps)
