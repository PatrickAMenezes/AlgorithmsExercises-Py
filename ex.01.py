numdays = int(input('Number of worked days in a month: '))
# 8 is the number of hours worked by day and 25 is the gain per hour
gainperday = 25*8
salary = numdays*gainperday
print('The employee has worked {} days in the last month.'
      .format(numdays))
print('The value that he will receive is R${:.2f}.'.format((salary)))
