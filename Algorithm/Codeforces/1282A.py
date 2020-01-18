t=input()
for _ in range(int(t)):
	a,b,c,r=map(int,input().split())
	maxx=max(a,b)
	minn=min(a,b)
	if((c-r>=maxx) and (c+r>=maxx)) or ((c+r<=minn) and (c-r<=minn)):
		print(maxx-minn)
	else:
		if (c-r)>minn:
			minn=(c-r)-minn
		else:
			minn=0
		if maxx>(c+r):
			maxx=maxx-(c+r)
		else:
			maxx=0
		print(minn+maxx)	