from PIL import Image
#https://github.com/TrG-1999/programming/tree/master/ProgamDemo/DemoPython/Watermark_With_DWT
##function dwt haar wavelet transform
def dwt_horizontal(original,temp,heigh,width):
	mid=round(width/2)
	for y in range(heigh):
		pos=0
		for x in range(mid):
			rt,bt,gt=temp[x,y]
			ro1,bo1,go1=original[pos,y]
			ro2,bo2,go2=original[(pos+1),y]
			rt=(ro1+ro1)/2
			bt=(bo1+bo2)/2
			gt=(go1+go2)/2
			temp[x,y]=(round(rt),round(bt),round(gt))

			rt,bt,gt=temp[(x+mid),y]
			rt=(ro1-ro1)/2
			bt=(bo1-bo2)/2
			gt=(go1-go2)/2
			temp[(x+mid),y]=(round(rt),round(bt),round(gt))
			pos+=2	
def dwt_vertical(original,temp,heigh,width):
	mid=round(heigh/2)
	for x in range(width):
		pos=0
		for y in range(mid):
			rt,bt,gt=temp[x,y]
			ro1,bo1,go1=original[x,pos]
			ro2,bo2,go2=original[x,(pos+1)]
			rt=(ro1+ro1)/2
			bt=(bo1+bo2)/2
			gt=(go1+go2)/2
			temp[x,y]=(round(rt),round(bt),round(gt))
			
			rt,bt,gt=temp[x,(y+mid)]
			rt=(ro1-ro1)/2
			bt=(bo1-bo2)/2
			gt=(go1-go2)/2
			temp[x,(y+mid)]=(round(rt),round(bt),round(gt))
			pos+=2		
def dwt_haar(img,pixels,heigh,width):
	print("prossesing DWT image level 1 -",pixels[1,1])
	new_img = img.copy() #temp from img
	dwt_horizontal(pixels,new_img.load(),heigh,width)
	dwt_vertical(new_img.load(),img.load(),heigh,width)
	return img
##function Idwt haar wavelet transform
def idwt_vertical(original,temp,heigh,width):
	mid=int(heigh/2)
	y=0
	pos=0
	while(y<heigh):
		for x in range(width):
			rt,bt,gt=temp[x,y]
			ro1,bo1,go1=original[x,pos]
			ro2,bo2,go2=original[x,pos+mid]
			rt=ro1+ro2
			bt=bo1+bo2
			gt=go1+go2
			temp[x,y]=(rt,bt,gt)
			temp[x,y+1]=(ro1*2-rt,bo1*2-bt,go1*2-gt)
		pos+=1
		y+=2
def idwt_horizontal(original,temp,heigh,width):
	mid=int(width/2)
	x=0
	pos=0
	while(x<width):
		for y in range(heigh):
			rt,bt,gt=temp[x,y]
			ro1,bo1,go1=original[pos,y]
			ro2,bo2,go2=original[pos+mid,y]
			rt=ro1+ro2
			bt=bo1+bo2
			gt=go1+go2
			temp[x,y]=(rt,bt,gt)
			temp[x+1,y]=(ro1*2-rt,bo1*2-bt,go1*2-gt)
		pos+=1
		x+=2
def idwt_haar(img,pixels,heigh,width):
	print("prossesing I-DWT image level 1")
	new_img = img.copy()
	idwt_vertical(pixels,new_img.load(),heigh,width)
	idwt_horizontal(new_img.load(),img.load(),heigh,width)
	return img
##embedding 1 domain
# def embedding(img,mark,a1=0.015,a2=0.015,a3=0.015):
# 	original=img.load()
# 	watermark=mark.load()
# 	##embedding domain LL
# 	for y in range(mark.size[1]):
# 		for x in range(mark.size[0]):
# 			# original[x,y]=original[x,y]+a*watermark[x,y]
# 			ro,go,bo=original[x,y]
# 			rw,gw,bw=watermark[x,y]
# 			original[x,y]=(round(ro+a1*rw),round(go+a2*gw),round(bo+a3*bw))
# 	return img
##emdedding 4 domain
def embedding(original,watermark,a1,a2,a3):
	#pixel-----------
	new_img=original.copy()
	temp=new_img.load()
	goc=original.load()
	water=watermark.load()
	widthOriginal=original.size[0]
	heightOriginal=original.size[1]
	widthWater=watermark.size[0]
	heightWater=watermark.size[1]
	#mid---------------------------------
	midWidth=round(widthOriginal/2)
	midHeight=round(heightOriginal/2)
	midWidthWater=round(widthWater/2)
	midHeightWater=round(heightWater/2)
	#------------------------------------
	for y in range(heightWater):
		for x in range(widthWater):
			if(x<midWidthWater and y<midHeightWater):
				r1,g1,b1=goc[x,y]
				r2,g2,b2=water[x,y]
				rt=(r1+a1*r2)
				gt=(g1+a2*g2)
				bt=(b1+a3*b2)
				temp[x,y]=(round(rt),round(gt),round(bt))
			if(x >= midWidthWater and y < midHeightWater):
				a=(x+(midWidth-midWidthWater))
				r1,g1,b1=goc[a,y]
				r2,g2,b2=water[x,y]
				rt=(r1+a1*r2)
				gt=(g1+a2*g2)
				bt=(b1+a3*b2)
				temp[a,y]=(round(rt),round(gt),round(bt))
			if(y >= midHeightWater and x < midWidthWater):
				b=(y+(midHeight-midHeightWater))
				r1,g1,b1=goc[x,b]
				r2,g2,b2=water[x,y]
				rt=(r1+a1*r2)
				gt=(g1+a2*g2)
				bt=(b1+a3*b2)
				temp[x,b]=(round(rt),round(gt),round(bt))
			if(x>=midWidthWater and y>= midHeightWater):
				a=(x+(midWidth-midWidthWater))
				b=(y+(midHeight-midHeightWater))
				r1,g1,b1=goc[a,b]
				r2,g2,b2=water[x,y]
				rt=(r1+a1*r2)
				gt=(g1+a2*g2)
				bt=(b1+a3*b2)
				temp[a,b]=(round(rt),round(gt),round(bt))
	return new_img
##exacting 1 domain
# def exacting(img,marked,mark,a1,a2,a3):
# 	original = img.load()
# 	watermarked = marked.load()
# 	watermark = mark.load()
# 	##exacting domain LL
# 	for y in range(mark.size[1]):
# 		for x in range(mark.size[0]):
# 			# watermark[x,y]=(watermarked[x,y]-original[x,y])/2
# 			ro,go,bo=original[x,y]
# 			rw,gw,bw=watermarked[x,y]
# 			watermark[x,y]=(round((rw-ro)/a1),round((gw-go)/a2),round((bw-bo)/a3))
# 	return mark
##exacting 4 doamin
def exacting(img,watermark,watermarkedImage,a1,a2,a3):
	#pixel-----------
	goc=img.load()
	new_watermark=watermark.copy()
	water=new_watermark.load()
	watermarked=watermarkedImage.load()
	#width height----------------------
	width=img.size[0]
	height=img.size[1]
	widthWater=watermark.size[0]
	heightWater=watermark.size[1]
	#mid---------------------------------
	midWidth=round(width/2)
	midHeight=round(height/2)
	midWidthWater=round(widthWater/2)
	midHeightWater=round(heightWater/2)
	#------------------------------------
	for y in range(height):
		for x in range(width):
			if(x<midWidthWater and y< midHeightWater):
				r1,g1,b1=goc[x,y]
				rt,gt,bt=watermarked[x,y]				
				r2=(rt-r1)/a1
				g2=(gt-g1)/a2
				b2=(bt-b1)/a3
				water[x,y]=(round(abs(r2)),round(abs(g2)),round(abs(b2)))
			if(x >= midWidth and y < midHeight):
				if((x-(midWidth-midWidthWater)) < widthWater and y < midHeightWater):
					r1,g1,b1=goc[x,y]
					rt,gt,bt=watermarked[x,y]		
					r2=(rt-r1)/a1
					g2=(gt-g1)/a2
					b2=(bt-b1)/a3
					water[(x-(midWidth-midWidthWater)),y]=(round(abs(r2)),round(abs(g2)),round(abs(b2)))
			if(y >= midHeight and x < midWidth):
				if((y-(midHeight-midHeightWater))<heightWater and x <widthWater):
					r1,g1,b1=goc[x,y]
					rt,gt,bt=watermarked[x,y]		
					r2=(rt-r1)/a1
					g2=(gt-g1)/a2
					b2=(bt-b1)/a3
					water[x,(y-(midHeight-midHeightWater))]=(round(abs(r2)),round(abs(g2)),round(abs(b2)))
			if(x>=midWidth and y>= midHeight):
				if( (x-(midWidth-midWidthWater)) < widthWater and (y-(midHeight-midHeightWater)) < heightWater ):
					r1,g1,b1=goc[x,y]
					rt,gt,bt=watermarked[x,y]		
					r2=(rt-r1)/a1
					g2=(gt-g1)/a2
					b2=(bt-b1)/a3
					water[(x-(midWidth-midWidthWater)),(y-(midHeight-midHeightWater))]=(round(abs(r2)),round(abs(g2)),round(abs(b2)))
	return new_watermark