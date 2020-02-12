n = int(input())
bulb = list(map(int,input().split()))
#function return complex
def complex(n,bulb):
	temp = 0
	for x in range(n-1):
		if (bulb[x]%2 == 0) and (bulb[x+1]%2 != 0) and (bulb[x]!=0) and (bulb[x+1]!=0):
			temp+=1
		elif (bulb[x]%2 != 0) and (bulb[x+1]%2 == 0) and (bulb[x]!=0) and (bulb[x+1]!=0):
			temp+=1
	return temp;
#compare even or odd
def compareEvenOrOdd(num,even,odd):
	if num%2==0:
		even-=1
	else:
		odd-=1
	return even,odd;
#calculated complext
def cal_complex(temp1,temp2,dic,complexs,k):
	if temp1 - dic >=0:
		temp1 = temp1 -dic
	else:
		temp2=temp2-(dic-temp1)
		temp1=0
		complexs=complexs+k
	return temp1,temp2,complexs
#sorting value of all zero
def sorting(n,bulb):
	even= n//2
	odd=n-even
	dictsort={} # key: position, Value: sum of all zero
	specialodd=[] # situation spectial of one-odd
	specialeven=[] # situation spectial of one-even
	i=0
	complexs=complex(n,bulb)
	while i<n:
		if bulb[i]!=0 and i<n-1:
			if bulb[i+1]==0:
				dictsort[i]=0
				even,odd = compareEvenOrOdd(bulb[i],even,odd);
				j=i
				i+=1
				while i<n and bulb[i]==0:
					dictsort[j]+=1
					i+=1
			else:
				even,odd=compareEvenOrOdd(bulb[i],even,odd)
				i+=1
		elif bulb[i]!=0:
			even,odd = compareEvenOrOdd(bulb[i],even,odd);
			i+=1
		elif bulb[0]==0:
			dictsort[0]=1
			j=i
			i+=1
			while i<n and bulb[i]==0:
				dictsort[j]+=1
				i+=1
	#put on tree
	dictsort = sorted(dictsort.items(),key=lambda x: x[1]) #sorting dictionary of all zero
	if len(dictsort)>0 and dictsort[0][1]==n and n>1:
		print(1)
	elif n<=1:
		print(0)
	else:	
		for i in range(len(dictsort)):
			first=dictsort[i][0]
			last=dictsort[i][0]+dictsort[i][1]+1
			if bulb[first]!=0 and last<n:
			 	if bulb[first]%2==0 and bulb[last]%2==0:
			 		if even-dictsort[i][1]<0 and len(specialeven)>0:
			 			even,odd,complexs=cal_complex(even,odd,specialeven[0][1],complexs,1)
			 			specialeven.remove(specialeven[0])
			 		even,odd,complexs=cal_complex(even,odd,dictsort[i][1],complexs,2)
			 	elif bulb[first]%2!=0 and bulb[last]%2!=0:
			 		if odd-dictsort[i][1]<0 and len(specialodd)>0:
			 			odd,even,complexs=cal_complex(odd,even,specialodd[0][1],complexs,1)
			 			specialodd.remove(specialodd[0])
			 		odd,even,complexs=cal_complex(odd,even,dictsort[i][1],complexs,2)
			 	else:
			 		complexs=complexs+1
			else:
				if bulb[first]==0:
					if bulb[last-1]%2==0:
						specialeven.append(dictsort[i])
					else:
						specialodd.append(dictsort[i])
				else:
					if bulb[first]%2==0:
						specialeven.append(dictsort[i])
					else:
						specialodd.append(dictsort[i])
		for x in specialodd:
			odd,even,complexs=cal_complex(odd,even,x[1],complexs,1)
		for x in specialeven:
			even,odd,complexs=cal_complex(even,odd,x[1],complexs,1)
		print(complexs)
sorting(n,bulb)