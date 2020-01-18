n = input()
string = input()
x=0
y=0
for i in range(int(n)):
	if string[i] == 'L':
		x-=1
	else:
		y+=1
print(x*(-1)+y+1)