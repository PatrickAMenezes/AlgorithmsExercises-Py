numcigday = int(input('Number of cigarettes smoked per day: '))
yearssmoked = int(input('Amount of time, in years, that you smoke: '))
# The smoker loses 0.006 days per cigarette
smokeddays = yearssmoked*365
totalcigsmoked = numcigday*smokeddays
lifetimelost = totalcigsmoked*0.006
print('you smoked for {} days and has lost {} days of life'.format(totalcigsmoked, lifetimelost))
