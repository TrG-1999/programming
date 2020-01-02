#include<windows.h>

void gotoxy(int x,int y);
void setcolor(int x);
void deletebk(int x,int y,int size);//xoa khoi dia
void spacecolor(int x,int y,int size,int color);//in khoi dia mau
void bkconsole(int heigh,int width,int color);// set color backgroud console
//Design By: LE TRUONG GIANG    D17CQAT01    N17DCAT020

void gotoxy(int x,int y)
{
	static HANDLE h = NULL;
	if(!h)
	{
		h = GetStdHandle(STD_OUTPUT_HANDLE);
	}
	COORD c = {x, y};
	SetConsoleCursorPosition(h,c);
}

void setcolor(int x)
{  
	HANDLE hConsoleColor;
    hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsoleColor, x);
}

void deletebk(int x,int y,int size)
{
	gotoxy(x,y);
	for(int i=0;i<size;i++)
	{	
		setcolor(0);
		printf(" ");
	}
		
}

void spacecolor(int x,int y,int size,int color)
{
	gotoxy(x,y);
	for(int i=0;i<size;i++)
	{	
		setcolor(color);//31 -------- 255  ( 1 color distance 16)
		printf(" ");
	}
}
void bkconsole(int heigh,int width,int color)
{	
	int i=0;
	for( ;i<heigh;i++)
	{
		spacecolor(0,i,width,color);
	}
}

void hoanvi(int *a,int *b)
{
	int temp= *a;
	*a = *b;
	*b = temp;
}
