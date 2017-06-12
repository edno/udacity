def hours2days(period):
    days = period // 24
    hours = period % 24
    return days, hours


print(hours2days(39))
