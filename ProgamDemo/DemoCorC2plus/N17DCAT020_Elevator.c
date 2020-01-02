#include <stdio.h>
#include <conio.h>
#include "dohoa.h"
#define MAX 10
typedef struct
{
	int n;
	int node[MAX];
}ds;
typedef struct
{
	int array[MAX];
	int font;
	int rear;
	int n;
}queue;
ds input;
int end;
//Design By: LE TRUONG GIANG    D17CQAT01    N17DCAT020
//funtion of ds
void innumber(ds number);//in thu tu nguoi vao ra man hinh
void del(ds* num,int vitri);//xoa theo vi tri
void deldata(ds* num,int data);//xoa theo data
int searchnum(ds number,int data);//data co trong danh sach khong
//------------------------------
//funtion of queue
int isEmpty(queue x);
int isFull(queue x);
int ispeek(queue x);
void insertqueue(queue* x,int data);//them phan tu vao hang doi
int takequeue(queue* x);//Lay phan tu ra khoi hang doi
//--------------------------------------------
//funtion of graphic
void layout();
void startup(queue* elevator,int *nowfloor);//thang may di len
void startdown(queue* elevator,int *nowfloor);//thang may di xuong
void closedoor(int floor);//dong cua thang may
void opendoor(int floor);//mo cua thang may
void start(queue* elevator,int *nowfloor);//Khoi dong thang may
//-----------------------------------------------------

int searchnum(ds number,int data)
{
	for(int i=0;i<number.n;i++)
	{
		if(number.node[i]==data){ return 1; }
	}
	return 0;
}

void innumber(ds number)
{
	gotoxy(40,7);
	setcolor(15);
	printf("Nguoi vao thuoc tang:");
	gotoxy(40,8);
	setcolor(15);
	for(int i=0;i<10;i++)
	{
		printf("  ");
	}
	gotoxy(40,8);
	for(int i=0;i<number.n;i++)
	{
		printf("%d ",number.node[i]);
	}
}
void del(ds* num,int vitri)
{
	if(vitri<0 || vitri >= num->n || num->n==0)
	{
		printf("Danh sach empty - Hoac vi tri khong hop le \n");
	}else{
		for(int i=vitri;i< num->n-1;i++)
		{
			num->node[i]=num->node[i+1];
		}
		num->n--;
	}
}
void deldata(ds* num,int data)
{
	for(int i=0;i<(num->n);i++)
	{
		if(data==num->node[i])
		{
			del(num,i);
		}
	}
}
void layout()
{
	int temp=1;
	for(int i=0;i<11;i++)
	{
		spacecolor(1,temp,11,255);
		spacecolor(1,temp+1,1,255);
		spacecolor(1,temp+2,1,255);
		spacecolor(11,temp+1,1,255);
		spacecolor(11,temp+2,1,255);
		//door Elevator
		spacecolor(2,temp+1,9,127);
		spacecolor(2,temp+2,9,127);
		spacecolor(6,temp+1,1,143);
		spacecolor(6,temp+2,1,143);	
		temp=temp+3;
		setcolor(15);
		gotoxy(14,temp-1);
		printf("<-Tang %d ",9-i);
	}
	spacecolor(0,temp-1,26,111);
	spacecolor(0,temp-2,26,111);
	setcolor(15);
	gotoxy(2,35);
	printf("SV: LE TRUONG GIANG \n \t   D17CQAT01 \n \t   N17DCAT020");
}
void closedoor(int floor)
{
	for(int i=0;i<4;i++)
	{
		Sleep(560);
		spacecolor(2+i,29-floor*3,1,127);
		spacecolor(2+i,30-floor*3,1,127);
		spacecolor(10-i,29-floor*3,1,127);
		spacecolor(10-i,30-floor*3,1,127);
		spacecolor(3+i,29-floor*3,1,143);
		spacecolor(3+i,30-floor*3,1,143);
		spacecolor(9-i,29-floor*3,1,143);
		spacecolor(9-i,30-floor*3,1,143);
	}
	gotoxy(14,30-floor*3);
	setcolor(15);
	printf("<-Tang %d ",floor);
}
void opendoor(int floor)
{	
	int temp=1;
	for(int i=0;i<4;i++)
	{
		Sleep(560);
		deletebk(6-i,29-floor*3,temp);
		deletebk(6-i,30-floor*3,temp);
		spacecolor(5-i,29-floor*3,1,143);
		spacecolor(5-i,30-floor*3,1,143);
		spacecolor(7+i,29-floor*3,1,143);
		spacecolor(7+i,30-floor*3,1,143);
		temp=temp+2;
	}
}
int isEmpty(queue x){
   return x.n == 0;
}

int isFull(queue x){
   return x.n == MAX;
}
int ispeek(queue x)
{
	if(!isEmpty(x)){
		return x.array[x.font];
	}
}
void insertqueue(queue* x,int data)
{
	if(!isFull(*x))
	{
		if(x->rear==MAX-1)// 0->MAX-1
		{
			x->rear=-1;
		}
		x->rear++;
		x->array[x->rear]=data;
		x->n++;
	}
}
int takequeue(queue* x)
{
	int data;
	if(!isEmpty(*x))
	{
		data=x->array[x->font];
		x->font++;
		if(x->font==MAX)
		{
			x->font=0;
		}
		x->n--;
		return data;
	}else{
		printf("\n Hang doi empty \n");
	}

}
void upsort(ds* sort)
{
	for(int i=0;i<(sort->n)-1;i++)
	{
		for(int j=i+1;j<(sort->n);j++)
		{
			if(sort->node[i]>sort->node[j])
			{
				hoanvi(&sort->node[i],&sort->node[j]);	
			}
		}
	}
}
void startup(queue* elevator,int *nowfloor)
{
	int temp;
	ds sort;	
	while(!kbhit())
	{
		(*nowfloor)++;
		gotoxy(14,30-(*nowfloor)*3);
		setcolor(207);
		printf("<-Tang %d ",(*nowfloor));
		if(ispeek(*elevator)==(*nowfloor))
		{

			opendoor(*nowfloor);
			deldata(&input,takequeue(elevator));
			innumber(input);
			if(isEmpty(*elevator) && end!=(*nowfloor))//gia tri cuoi cua queue luon di toi end
			{
				insertqueue(elevator,end);
			}
			closedoor(*nowfloor);
			if(kbhit()) break;
			break;	
		}
		Sleep(1160);
		setcolor(15);
		gotoxy(14,30-(*nowfloor)*3);
		printf("<-Tang %d ",(*nowfloor));
	}
	if(kbhit())
	{
		temp=getch();
		temp=temp-'0';
		if(temp < 10 && temp>-1 && !isFull(*elevator))
		{
			if(!searchnum(input,temp) && temp!=end) //Chong SPAM....
			{	
				insertqueue(elevator,temp);
				if(input.n!=MAX)
				{
					input.node[input.n]=temp;
					input.n++;
				}
				innumber(input);
				//sort de chon duong toi uu nhat
				sort.n=0;
				while(elevator->n){
					sort.node[sort.n]=takequeue(elevator);
					sort.n++;
				}
				if(!searchnum(sort,end)){
					sort.node[sort.n]=end;
					sort.n++;
				} 
				upsort(&sort);
				for(int i=0;i<sort.n;i++)
				{
					if(sort.node[i]>(*nowfloor))
					{
						insertqueue(elevator,sort.node[i]);
					}
				}
				for(int i=(sort.n)-1;i>=0;i--)
				{
					if(sort.node[i]<=(*nowfloor))
					{
						insertqueue(elevator,sort.node[i]);
					}
				}
				//--------------------------------------
			}	
		}
	}
}
void startdown(queue* elevator,int *nowfloor)
{
	int temp;
	ds sort;	
	while(!kbhit())
	{
		(*nowfloor)--;
		gotoxy(14,30-(*nowfloor)*3);
		setcolor(207);
		printf("<-Tang %d ",(*nowfloor));
		if(ispeek(*elevator)==(*nowfloor))
		{
			opendoor(*nowfloor);
			deldata(&input,takequeue(elevator));
			innumber(input);
			if(isEmpty(*elevator) && end!=(*nowfloor))//gia tri cuoi cua queue luon di toi end
			{
				insertqueue(elevator,end);
			}
			closedoor(*nowfloor);
			if(kbhit()) break;
			break;	
		}
		Sleep(1160);
		setcolor(15);
		gotoxy(14,30-(*nowfloor)*3);
		printf("<-Tang %d ",(*nowfloor));
	}
	if(kbhit())
	{
		temp=getch();
		temp=temp-'0';
		if(temp < 10 && temp>-1 && !isFull(*elevator))
		{
			if(!searchnum(input,temp) && temp!=end ) //Chong SPAM....
			{	
				insertqueue(elevator,temp);
				if(input.n!=MAX)
				{
					input.node[input.n]=temp;
					input.n++;
				}
				innumber(input);
				//sort de chon duong toi uu nhat
				sort.n=0;
				while(elevator->n){
					sort.node[sort.n]=takequeue(elevator);
					sort.n++;
				}
				if(!searchnum(sort,end)){
					sort.node[sort.n]=end;
					sort.n++;
				}
				upsort(&sort);
				for(int i=(sort.n)-1;i>=0;i--)
				{
					if(sort.node[i]<(*nowfloor))
					{
						insertqueue(elevator,sort.node[i]);
					}
				}
				for(int i=0;i<sort.n;i++)
				{
					if(sort.node[i]>=(*nowfloor))
					{
						insertqueue(elevator,sort.node[i]);
					}
				}
				//--------------------------------------
			}
		}
	}
}
void start(queue* elevator,int *nowfloor)
{
	closedoor(*nowfloor);
	while(elevator->n)
	{	
		if(ispeek(*elevator) > (*nowfloor))
		{	
			startup(elevator,nowfloor);	
		}else if(ispeek(*elevator) < (*nowfloor))
		{
			startdown(elevator,nowfloor);
		}else if(ispeek(*elevator)==(*nowfloor))
		{
			takequeue(elevator);//ngan loop khi nhap = nowfloor(ve cuoi)
		}
		
	}
}
int main()
{
	int nowfloor=0,submit=0;
	queue elevator;
	input.n=0;
	elevator.n=0;
	elevator.font=0;
	elevator.rear=-1;
	layout();
	do{
		opendoor(nowfloor);
		do{
			gotoxy(40,5);
			setcolor(15);
			printf("Nhap tang moi nguoi muon toi (1-9)");
			gotoxy(40,6);
			printf("                ");
			gotoxy(40,6);
			scanf("%d",&submit);
		}while(submit<0 || submit>9);
		end=submit;
		insertqueue(&elevator,submit);
		start(&elevator,&nowfloor);
		gotoxy(0,37);
		setcolor(15);
		printf("\n");
	}while(1);	
}

