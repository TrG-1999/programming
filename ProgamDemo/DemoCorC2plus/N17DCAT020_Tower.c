#include<stdio.h>
#include<conio.h>
#include<string.h>
#include "dohoa.h"
typedef struct
{
	int block[10];//kich thuoc cua dia
	int color[10];//mau sac cua dia
	int i[10];//vi tri cua dia trong thap
   	int cot;//Trung tam cua thap
   	int n;//so dia
   
}Thap;
void Moveup(int i,int cot,int block,int color,int *speed);
void Movedown(int j,int cot,int block,int color,int *speed,int i);
void Moveright(int i,int cot,int block,int color,int *speed);
void Moveleft(int i,int cot,int block,int color,int *speed);
void layout();
void inspeed();
void Tower(int n ,Thap* a,Thap* b,Thap* c,int *speed);
void Tower(int n ,Thap* a,Thap* b,Thap* c,int *speed){
	int temp,temp1;
    if(n==1){
        if(a->cot < c->cot)
        {
        	temp= a->n;
        	temp1= c->n;
        	Moveup(a->i[temp],a->cot,a->block[temp],a->color[temp],speed);
        	Moveright(a->cot,c->cot,a->block[temp],a->color[temp],speed);
        	Movedown(14-temp1,c->cot,a->block[temp],a->color[temp],speed,2);
        	temp1++;
        	c->n=temp1;
        	c->i[temp1]=15-temp1;
        	c->block[temp1]=a->block[temp];
        	c->color[temp1]=a->color[temp];
        	a->n=temp-1;
		}else if(a->cot > c->cot)
		{
			temp= a->n;
        	temp1= c->n;
        	Moveup(a->i[temp],a->cot,a->block[temp],a->color[temp],speed);
        	Moveleft(a->cot,c->cot,a->block[temp],a->color[temp],speed);
        	Movedown(14-temp1,c->cot,a->block[temp],a->color[temp],speed,2);
        	temp1++;
        	c->n=temp1;
        	c->i[temp1]=15-temp1;
        	c->block[temp1]=a->block[temp];
        	c->color[temp1]=a->color[temp];
        	a->n=temp-1;
		}
        return;
    }
    Tower(n-1,a,c,b,speed);
    Tower(1,a,b,c,speed);
    Tower(n-1,b,a,c,speed);
    }
//Design By: LE TRUONG GIANG    D17CQAT01    N17DCAT020
void Moveup(int i,int cot,int block,int color,int *speed)//(vitri dia trong cot,cot chua dia,khoi dia,color,speed).
{
	int xoa=cot,key;
		cot=cot-block/2;
	while(i>2 && !kbhit())
	{	
		spacecolor(cot,i-1,block,color);
		deletebk(cot,i,block);
		spacecolor(xoa,i,1,255);//to lai trung tam cot
		if(i==3)
		{
			spacecolor(xoa,i,1,15);
		}
		Sleep(*speed);
		i--;
	}
	if(kbhit())
	{
		key=getch();
			if(key==224)
	{
		key=getch();
		if(key==72)
		{
			*speed = *speed - 15;
			inspeed(*speed);
			if(*speed < 15){
				*speed=15;
				inspeed(*speed);
			}
			Moveup(i,xoa,block,color,speed);
		}else if(key==80){
			*speed = *speed + 15;
			inspeed(*speed);
			if(*speed > 90){
				*speed=90;
				inspeed(*speed);
			}
			Moveup(i,xoa,block,color,speed);
		}else{Moveup(i,xoa,block,color,speed);}
	}else{
			Moveup(i,xoa,block,color,speed);
		}
	}

}

void Movedown(int j,int cot,int block,int color,int *speed,int i)//(vi tri xuong cua dia,cot chua dia,block,color,speed,roi)
{
	int xoa=cot,key;
	cot=cot-block/2;
	while((i<j) && !kbhit())
	{
		spacecolor(cot,i+1,block,color);
		deletebk(cot,i,block);
		spacecolor(xoa,i,1,255);//to lai trung tam cot1
		if(i<=3)
		{
			spacecolor(xoa,i,1,15);
		}
		i++;
		Sleep(*speed);
	}
	if(kbhit())
	{
		key=getch();
			if(key==224)
	{
		key=getch();
		if(key==72)
		{
			*speed = *speed - 15;
			inspeed(*speed);
			if(*speed < 15){
				*speed=15;
				inspeed(*speed);
			}
			Movedown(j,xoa,block,color,speed,i);
		}else if(key==80){
			*speed = *speed + 15;
			inspeed(*speed);
			if(*speed > 90){
				*speed=90;
				inspeed(*speed);
			}
			Movedown(j,xoa,block,color,speed,i);
		}else{Movedown(j,xoa,block,color,speed,i);}
	}else{
			Movedown(j,xoa,block,color,speed,i);
		}
	}
}

void Moveright(int i,int cot,int block,int color,int *speed)//(cot bat dau,cot den,khoi dia,color,speed)
{
	int key;
	i=i-block/2;
	while((i<cot-block/2+1) && !kbhit())	
	{
		spacecolor(i,2,block,color);
		deletebk(i-1,2,1);
		Sleep(*speed);
		i++;
	}
	if(kbhit())
	{
		key=getch();
			if(key==224)
	{
		key=getch();
		if(key==72)
		{
			*speed = *speed - 15;
			inspeed(*speed);
			if(*speed < 15){
				*speed=15;
				inspeed(*speed);
			}
			Moveright(i+block/2,cot,block,color,speed);
		}else if(key==80){
			*speed = *speed + 15;
			inspeed(*speed);
			if(*speed > 90){
				*speed=90;
				inspeed(*speed);
			}
			Moveright(i+block/2,cot,block,color,speed);
		}else{Moveright(i+block/2,cot,block,color,speed);}
	}else{
			Moveright(i+block/2,cot,block,color,speed);
		}
	}
}

void Moveleft(int i,int cot,int block,int color,int *speed)//(cot bat dau,cot den,block,color,speed)
{
	int key;
	cot=cot-block;
	i=i-block/2;
	while((i>cot+block/2) && !kbhit())
	{
		spacecolor(i,2,block,color);
		deletebk(i+block,2,block);
		Sleep(*speed);
		i--;
	}
	if(kbhit())
	{
		key=getch();
			if(key==224)
	{
		key=getch();
		if(key==72)
		{
			*speed = *speed - 15;
			inspeed(*speed);
			if(*speed < 15){
				*speed=15;
				inspeed(*speed);
			}
			Moveleft(i + block/2,cot+block,block,color,speed);
		}else if(key==80){
			*speed = *speed + 15;
			inspeed(*speed);
			if(*speed > 90){
				*speed=90;
				inspeed(*speed);
			}
			Moveleft(i + block/2,cot+block,block,color,speed);
		}else{Moveleft(i + block/2,cot+block,block,color,speed);}
	}else{
			Moveleft(i + block/2,cot+block,block,color,speed);
		}
	}
}
void inspeed(int speed){
	setcolor(15);
	gotoxy(10,18);
	printf("               ");
	gotoxy(10,18);
	if(speed==90 || speed==15)
	{
		printf("Speed: Limit");
	}else{
		printf("Speed: %d ",speed);
	}
}

void layout()
{	
//	int a=20,b=51,c=82;
	spacecolor(10,15,21,255);
    spacecolor(41,15,21,255);
    spacecolor(72,15,21,255);
    for(int i=4;i<15;i++)
    {
    	spacecolor(20,i,1,255);
    	spacecolor(51,i,1,255);
    	spacecolor(82,i,1,255);
	}
	setcolor(15);
	gotoxy(2,20);
	printf("Design By: LE TRUONG GIANG \n \t   D17CQAT01 \n \t   N17DCAT020");
}
int main(){
	Thap A,B,C;
	int n,temp,a=20,colors=239,block=3,speed=60;
	A.cot=20;A.n=0;//cot: trung tam cot; n:so dia chua trong cot
	B.cot=51;B.n=0;//i:vi tri dia trong cot; block:Kich thuoc dia;color;
	C.cot=82;C.n=0;
	do{
    	printf("Nhap n So Dia ( 1<= n <=9 ): ");
    	scanf("%d",&n);
    }while(n<=0 || n>=10);
    system("cls");
    A.n=n;
    temp=n;
    layout();
    inspeed(speed);
	for(int i=15-n;i<15;i++)
    {
    	A.i[temp]=i;
    	A.block[temp]=block;
    	A.color[temp]=colors;
    	spacecolor(--a,i,block,colors);
    	temp--;
    	block+=2;
    	colors-=16;
	}
	setcolor(15);
	gotoxy(51,17);
	printf("Nhan Phim Bat Ki De Bat Dau");
	getch();
	gotoxy(51,17);
	printf("                           ");
	Tower(n,&A,&B,&C,&speed);
    getch();	
	setcolor(15);
	gotoxy(51,22);
    return 0;
}




