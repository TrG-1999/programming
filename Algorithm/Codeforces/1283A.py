n=input()
for i in range(int(n)):
	h,m=map(int,input().split())
	print((23-h)*60+(60-m))