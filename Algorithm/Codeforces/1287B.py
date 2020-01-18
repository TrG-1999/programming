n, k = map(int, input().split())
string=[]
strtmp={}
result=0
for i in range(n):
	tmp=input()
	string.append(tmp)
	# strtmp[tmp]=i
SET=set(string)
if n >=3:
	x=0
	while x<n-1:
		y=x+1
		while y<n:
			temp=""
			for i in range(k):
				if string[x][i]==string[y][i]:
					temp+=string[x][i]
				else:
					temp+=chr(236-(ord(string[x][i])+ord(string[y][i])))
			if temp in SET:
			# if strtmp.get(temp) and strtmp[temp]>x and strtmp[temp]>y:
				result+=1
			y+=1
		x+=1
# print(result)
print(result//3)
