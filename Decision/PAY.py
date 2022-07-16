'''
pay calculator
'''

work_hours = int(input("Enter total work hours= "))
hourly_wage = int(input("Enter regular hourly wage= "))
total_pay = work_hours*hourly_wage 
extra_hours = work_hours-40 
if work_hours<=40:
    print('Total pay without overtime =',total_pay)
elif work_hours>40 and work_hours<=60:
    extra_pay = (hourly_wage*40)+(1.5*hourly_wage*extra_hours) #extrapay >40
    print('Total pay with overtime but less them 60 hours=',extra_pay)
elif work_hours>60:
    extra_pays =(hourly_wage*40)+(2*hourly_wage*extra_hours) #extrapay >60
    print('Total pay  with extra time but more then 60 hours=',extra_pays)