#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n=0,max=0,p=0;
    
    scanf("%d",&n);
    int *w=(int *)malloc(sizeof(int)*n);
     
    for(int i=0;i<n;i++){
        scanf("%d%d",(w+i),&p);
        p--;
        if(p>=0) 
            w[i]+=w[p];
        
        if(max<w[i])
            max=w[i];        
    }
    printf("%d",max);
}