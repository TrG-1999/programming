import numpy as np
def dwt_horizontal(matrix,heigh,width):
	compu=matrix.copy()
	mid=int(width/2)
	for y in range(heigh):
		pos=0
		for x in range(mid):
			compu[y][x]=(matrix[y][pos]+matrix[y][pos+1])
			compu[y][x+mid]=(matrix[y][pos]-matrix[y][pos+1])
			pos+=2			
	return compu
def dwt_vertical(matrix,heigh,width):
	compu=matrix.copy()
	mid=int(heigh/2)
	for x in range(width):
		pos=0
		for y in range(mid):
			compu[y][x]=(matrix[pos][x]+matrix[pos+1][x])
			compu[y+mid][x]=(matrix[pos][x]-matrix[pos+1][x])
			pos+=2
	return compu
def idwt_vertical(matrix,heigh,width):
	compu=matrix.copy()
	mid=int(heigh/2)
	y=0
	pos=0
	while(y<heigh):
		for x in range(width):
			compu[y][x]=int((matrix[pos][x]+matrix[pos+mid][x])/2)
			compu[y+1][x]=matrix[pos][x]-compu[y][x]
		pos+=1
		y+=2
	return compu
def idwt_horizontal(matrix,heigh,width):
	compu=matrix.copy()
	mid=int(width/2)
	x=0
	pos=0
	while(x<width):
		for y in range(heigh):
			compu[y][x]=int((matrix[y][pos]+matrix[y][pos+mid])/2)
			compu[y][x+1]=matrix[y][pos]-compu[y][x]
		pos+=1
		x+=2
	return compu
	
matrix=np.array([[20,21,32,65],[12,43,45,55],[32,17,53,34],[23,12,32,21]])
# print(dwt_horizontal(matrix,4,4))
#invert DWT
result=dwt_vertical(dwt_horizontal(matrix,4,4),4,4)
print(result)
#convert DWT
print(idwt_horizontal(idwt_vertical(result,4,4),4,4))