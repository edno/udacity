def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    return days_in_month[month_number-1]

# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))
