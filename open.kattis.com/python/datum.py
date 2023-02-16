import datetime

d,m = input().split()
ss = "%.2d-%.2d-%d" % (int(d),int(m), 2009)
dt = datetime.datetime.strptime(ss, "%d-%m-%Y")
print(dt.strftime("%A"))
