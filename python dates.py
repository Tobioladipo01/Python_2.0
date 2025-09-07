import datetime

x= datetime.datetime.now()
print(x)
print(x.year)
print(x.minute)
print(x.strftime("%d/%m/%Y"))  #this lets you choose the arrangment of your date or time
print (x.strftime("%A"))  #Tells you the day

y=datetime.datetime(2025, 8, 3)
print(y)

z=datetime.date.today()
print(z)

a= datetime.time(4, 56, 8)
print(a)
