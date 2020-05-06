from PIL import Image
##function dwt harr wavelet transform
def dwt_horizontal(original,temp,heigh,width):
	mid=round(width/2)
	for y in range(heigh):
		pos=0
		for x in range(mid):
			# temp[x,y]=round((original[pos,y]+original[(pos+1),y])/2)
			rt,gt,bt=temp[x,y]
			ro1,go1,bo1=original[pos,y]
			ro2,go2,bo2=original[(pos+1),y]
			rt=(ro1+ro1)/2
			gt=(go1+go2)/2
			bt=(bo1+bo2)/2
			temp[x,y]=(round(rt),round(gt),round(bt),0)
			# temp[(x+mid),y]=round((original[pos,y]-original[(pos+1),y])/2)
			rt,gt,bt=temp[(x+mid),y]
			rt=(ro1-ro1)/2
			gt=(go1-go2)/2
			bt=(bo1-bo2)/2
			temp[(x+mid),y]=(round(rt),round(gt),round(bt),0)
			pos+=2	
def dwt_vertical(original,temp,heigh,width):
	mid=round(heigh/2)
	for x in range(width):
		pos=0
		for y in range(mid):
			# temp[x,y]=round((original[x,pos]+original[x,(pos+1)])/2)
			rt,gt,bt=temp[x,y]
			ro1,go1,bo1=original[x,pos]
			ro2,go2,bo2=original[x,(pos+1)]
			rt=(ro1+ro1)/2
			gt=(go1+go2)/2
			bt=(bo1+bo2)/2
			temp[x,y]=(round(rt),round(gt),round(bt),0)
			# temp[x,(y+mid)]=round((original[x,pos]-original[x,(pos+1)])/2)
			rt,gt,bt=temp[x,(y+mid)]
			rt=(ro1-ro1)/2
			gt=(go1-go2)/2
			bt=(bo1-bo2)/2
			temp[x,(y+mid)]=(round(rt),round(gt),round(bt),0)
			pos+=2		
def dwt_haar(img,pixels,heigh,width):
	print(pixels[1,1])
	new_img = img.copy() #temp from img
	dwt_horizontal(pixels,new_img.load(),heigh,width)
	dwt_vertical(new_img.load(),img.load(),heigh,width)
	return img
##function Idwt harr wavelet transform
def idwt_vertical(original,temp,heigh,width):
	mid=int(heigh/2)
	y=0
	pos=0
	while(y<heigh):
		for x in range(width):
			# temp[x,y]=int((original[x,pos]+original[x,pos+mid])/2)
			rt,gt,bt=temp[x,y]
			ro1,go1,bo1=original[x,pos]
			ro2,go2,bo2=original[x,pos+mid]
			rt=ro1+ro2
			gt=go1+go2
			bt=bo1+bo2
			temp[x,y]=(rt,gt,bt)
			# temp[x,y+1]=original[x,pos]-temp[x,y]
			temp[x,y+1]=(ro1*2-rt,go1*2-gt,bo1*2-bt)
		pos+=1
		y+=2
def idwt_horizontal(original,temp,heigh,width):
	mid=int(width/2)
	x=0
	pos=0
	while(x<width):
		for y in range(heigh):
			# temp[x,y]=int((original[pos,y]+original[pos+mid,y])/2)
			rt,gt,bt=temp[x,y]
			ro1,go1,bo1=original[pos,y]
			ro2,go2,bo2=original[pos+mid,y]
			rt=ro1+ro2
			gt=go1+go2
			bt=bo1+bo2
			temp[x,y]=(rt,gt,bt)
			# temp[x+1,y]=original[pos,y]-[x,y]
			temp[x+1,y]=(ro1*2-rt,go1*2-gt,bo1*2-bt)
		pos+=1
		x+=2
def idwt_harr(img,pixels,heigh,width):
	#DWT level 1
	new_img = img.copy()
	idwt_vertical(pixels,new_img.load(),heigh,width)
	idwt_horizontal(new_img.load(),img.load(),heigh,width)
	print(pixels[1,1])
	return img
##Running
img = Image.open('Lena-convert.png')
#convert DWT
img=dwt_haar(img,img.load(),img.size[1],img.size[0])
img.save('Lena-convert-Dwt.png')
#invert DWT
img=idwt_harr(img,img.load(),img.size[1],img.size[0])
img.show()
