    #include<stdio.h>
    #include<conio.h>
    int main()
    {
    	int x,n,v,cost=0;
    	scanf("%d",&n);
    	scanf("%d",&v);
    	if((n-1)<=v)
		{
    		cost=n-1;
		}else{
    		cost=v;
    		for(x=2;x<=n;x++)
	    	{
	            if((n-x) <= v)
	            {
	                cost=cost+x;
	                break;
	            }else{
	                cost=cost+x;
	    		}
	    	}
		}
    	printf("%d",cost);
    	return 0;
    }
