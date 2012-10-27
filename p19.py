#
# You are given the following information, but you may prefer to do some research for yourself.

# - 1 Jan 1900 was a Monday.
# - Thirty days has September,
# - April, June and November.
# - All the rest have thirty-one,
# - Saving February alone,
# - Which has twenty-eight, rain or shine.
# - And on leap years, twenty-nine.
# = A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Performance : 44.6 ms

def nextSunday():
    # 6 jan 1901 was the first  sunday in this century
    day = 6
    month = 1
    year = 1901
    # Could be made faster if we used an array. But not really a concern
    mDays = {
            1 : 31,     2 : 28,     3 : 31,
            4 : 30,     5 : 31,     6 : 30,
            7 : 31,     8 : 31,     9 : 30,
            10 : 31,    11 : 30,    12 : 31
             }
    count = 0

    while(year < 2001):
        if(day > mDays[month]):
                month += 1
                if(month == 13):
                    year += 1
                    if year == 2001 : break # Quick Fix (Just to get out of the loop correctly)
                    
                    month = 1

                    # if leap year
                    if((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)):
                        mDays[2] = 29
                    else:
                        mDays[2] = 28

                tmp = month - 1
                if tmp == 0 : tmp = 12 # Special case when (month-1) is zero. i.e january - 1 = December
                day = day % mDays[tmp] # mDays[previous month]. i.e (month - 1).

                # E.g 30 % 30 would return 0 but it should be 1st of next month
                if day == 0 : day += 1

        
        #print "{}/{}/{}\n".format(day, month, year)
        if day == 1 : 
            count += 1
            #print '----------------------'

        day += 7

    return count

def init():
    print nextSunday()

if __name__ == "__main__":
    init()