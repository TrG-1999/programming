n = input()
lens=[]
string=[]
kq=[]
for i in range(int(n)):
	lens.append(input())
	string.append(input())
	kq.append(0)
for i in range(int(n)):
	temp,flag=0,0
	for k in range(int(lens[i])):
		if string[i][k]=='A':
			if temp>kq[i] and flag>0:
				kq[i]=temp
			flag+=1
			temp=0	
		else:
			temp+=1
	if temp>kq[i] and flag>=1:
		kq[i]=temp

for i in range(int(n)):
	print(kq[i])