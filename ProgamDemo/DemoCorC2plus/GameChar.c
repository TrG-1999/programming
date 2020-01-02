#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>
void gotoxy(int x, int y);
void layout();
int gamechar(int *speed,int i,int x);
int speedchar(char key,int speed);
void playgame();

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

void playgame()
{
	int human=0,android=0,speed=200,x;
	srand(time(NULL));
	while(human<10 && android<10 && (human+android <26))
	{
		x = rand()%26;
		if(gamechar(&speed,0,x)==1)
		{
			human++;
			gotoxy(0,23);
			printf("Nguoi Duoc %d core",human);
		}else{
			android++;
			gotoxy(0,24);
			printf("May Duoc %d core",android);
		}
		
	}
	if(human > android)
	{
		gotoxy(26,10);
		printf("BAN THANG");
	}else{
		gotoxy(21,10);
		printf("May THANG ---- Ban Thua");
	}
	gotoxy(0,25);
}

void layout()
{
	
	for(char i='A';i<='Z';i++)
	{
		printf(" %c",i);	
	}
	gotoxy(0,20);
	for(char i='A';i<='Z';i++)
		{
			printf("--");	
		}
	gotoxy(0,22);
		printf("--Bang Diem--");
	gotoxy(0,23);
		printf("Ban Duoc 0 core");
	gotoxy(0,24);
		printf("May Duoc 0 core");
	gotoxy(26,22);
		printf("Speed:Easy");	
}
//Design By: LE TRUONG GIANG    D17CQAT01    N17DCAT020
int gamechar(int *speed,int i,int x)
{
	char c = x+'A',C = x+'a';
	if(i!= 0)
	{
		gotoxy(x*2,0);
		printf("  ");
	}
	while(i<20 && !kbhit())
	{
		gotoxy(x*2,i);
		printf("  ");
		gotoxy(x*2,i+1);
		printf(" %c",c);
		Sleep(*speed);
		i++;
	}
	gotoxy(x*2,i);
	printf("  ");
	gotoxy(x*2,0);
	printf(" %c",c);

		if(i<20)
		{
			char check=getch();
			
			if(check==-32)
			{
				*speed=speedchar(check,*speed);
				gotoxy(32,22);
				printf("           ");
				gotoxy(32,22);
				if(*speed==200){
					printf("Easy");
				}else if(*speed==150)
				{
					printf("Normal");
				}else if(*speed==100)
				{
					printf("Hard");
				}else{
					printf("Very Hard");
				}
				gamechar(speed,i,x);
			}else{
				if(check== c || check== C)
				{
					return 1;
				} else { return 0; }
			}
		}else{
		gotoxy(x*2,20);
		printf("--");
		return 0;
	}
}
//Design By: LE TRUONG GIANG    D17CQAT01    N17DCAT020
int speedchar(char key,int speed)
{
	if(key==-32)
	{
		key=getch();
		if(key==72)
		{	
			if(speed>=100){
				speed=speed-50;
				return speed;
			}else{
				return speed;
			}
		}else if( key==80)
		{	
			if(speed<=150){
				speed=speed+50;
				return speed;
			}else{
				return speed;
			}	
		}else{
			return speed;
		}			
	}else{
		return speed;
	}	
}

int main()
{
	int key;	
	layout();
	do{
		gotoxy(0,26);
		printf("Design By: LE TRUONG GIANG \n \t   D17CQAT01 \n \t   N17DCAT020");
		gotoxy(15,10);
		printf("_Nhan Enter De Bat Dau Game_");
		gotoxy(15,11);
		printf("     (Nhan Esc De thoat)");
		key=getch();
		if(key==13)
		{
			system("cls");
			layout();	
			playgame();
			Sleep(4000);
		}
		
	}while(key != 27);
	return 0;
}
