    #include<stdio.h>
    #include<conio.h>
    int main()
    {
    	int x,y,z,a,b,c,temp;
    	scanf("%d",&x);
    	scanf("%d",&y);
    	scanf("%d",&z);
    	scanf("%d",&a);
    	scanf("%d",&b);
    	scanf("%d",&c);
    	if((a-x) >=0)
    	{
    		temp=a-x;
    		if((a-x+b-y)>= 0)
    		{
    			if((a-x+b-y+c-z)>=0)
    			{
    				printf("YES");
    			}else{
    				printf("NO");
    			}
    		}else{
    			printf("NO");
    		}
    	}else{
    		printf("NO");
    	}
    	return 0;
    }
