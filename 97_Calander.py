import datetime
import time
"""
print(time.time())
#print(datetime.date(2019))
print(datetime.datetime.now())
dt=datetime.datetime.now()
print(type(dt))
print(dt.date())
print(dt.month)
print(dt.day)
print(dt.day+1)

print(datetime.datetime(2019,1,1))
"""
start_dt=datetime.datetime(2019,1,1)
end_dt=datetime.datetime(2019,12,31)
#print(dt.year)
#print(dt.strftime("%A"))
#print(start_dt.strftime("%A"))

"""
for i in range(start_dt.year,end_dt.year+1):
    print(i)
    
    for j in range(start_dt.month,end_dt.month+1):
        print(j)
#print(i)
#print(start_dt.year)
print("end_date_day:",end_dt.strftime("%A"))
print("end_dt_year:",end_dt.strftime("%C"))
print("end_dt_month:",end_dt.strftime("%B"))

order_dt=["%A","%B","%C"]
for [i,j,j] in order_dt:
    print("end_date_day:",end_dt.strftime(i))
    print("end_dt_month:",end_dt.strftime(j))
    print("end_dt_year:",end_dt.strftime(k))

#for i,j,k in zip()
"""
print(start_dt)
print(start_dt)
print(start_dt.day)
print(start_dt.month)
print(start_dt.year)
d=31
month={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
for year in range(start_dt.year,start_dt.year+1):
    print(year)
    for mon in range(start_dt.month,13):
        print("\n\n","------",month[mon].upper(),"------\n")
        print("\t".join(["Sun","Mon","Tue","Wed","Thu","Fry","Sat"]).upper(),"\n")
        if mon==2:
            d=28
        elif mon in (4,6,9,11):
            d=30
        else:
            d=31
        
        for day in range(1,d+1):
            #print(year)
            #print(mon)
            td=datetime.datetime(year,mon,day)#today -current day
            """
            if day%7==0:
                print("\n")
            """
            print("{:^4}".format(day),end="    ")
            
            if (td.strftime("%A")=='Saturday'):
                print("\n")

#print(start_dt.strftime("%A"))
            
         
    
