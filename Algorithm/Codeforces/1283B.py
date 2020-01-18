t=input()
for i in range(int(t)):
	n,k=map(int,input().split())
	if n%k >0:
		if n%k > k//2:
			print(k//2+(n//k)*k)
		else:
			print(n%k+(n//k)*k)
	else:
		print(n)