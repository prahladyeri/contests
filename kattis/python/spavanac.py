import sys, datetime

for input in sys.stdin:
	ar = input.split()
	h,m = int(ar[0]),int(ar[1])
	dd = datetime.datetime(2010, 12, 27, h, m, 0)
	rr = dd - datetime.timedelta(minutes=45)
	print("%d %d" % (rr.hour,rr.minute))
