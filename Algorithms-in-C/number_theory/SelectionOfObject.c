#include<stdio.h>
#include<math.h>

//====================================================
int max(int a, int b){
if(a>=b)
	return a;
else
	return b;
} 
//====================================================
int min(int a, int b){
if(a>=b)
	return b;
else
	return a;
}
//======================================================
int main(){
	long long int T,j,ans,x,y,n,r,l,m,a=1,b=1;
	int M=1000000007;
			printf("                          (n)!\n");
			printf("ENTER n AND r OF FORM ____________  \n");
			printf("                       (r)!(n-r)!\n\n\n");
			scanf("%lld %lld",&n,&r);


//------------------------------------------------------------
 			y=r;
 			x=n-r;

			l= min(x,y);
			m= max(x,y);
			a=1;
			b=1;

		for(j=1;j<=l;j++){
			a=((a%M)*(j%M))%M;
			b=((b%M)*((m+j)%M))%M;
		}

		ans=(b%M)/(a%M);

		printf("\n%lld\n", ans);
		
		

//-------------------------------------------------------------
			
				
				return 0;
			}
