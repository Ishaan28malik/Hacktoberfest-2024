//============================================================================
// Name        : polynomial.cpp
// Author      : Rishi Mundada
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
class polynomial;
class term{
int c,e;
public:
term(){
c = 0;
e = 0;
}
friend class polynomial;
friend void operator >>(istream &in,polynomial p);
friend void operator <<(ostream &out,polynomial p);
};

class polynomial{
	int n;
	term *p;
public:
    polynomial(){
        cout<<"Enter total no. of terms\n";
        cin>>n;
       // n = no;
		p = new term[n];
	}
    polynomial(int no){
    n = no;
    p = new term[n];
    for(int i = 0;i<n;i++){
        p[i].c = 0;
        p[i].e = 0;
    }
    }
	void getInput(){
		cout<<"Enter the coefficient and the exponent\n";
		for(int i = 0; i<n ; i++){
			cin>>p[i].c;
			cin>>p[i].e;
		}
	}
	void showOutput(){
		cout<<"The polynomial is:\n";
		for(int i = 0;i<n;i++){
            if(i!=(n-1))
			cout<<p[i].c<<"x^"<<p[i].e<<" + ";
            else
            cout<<p[i].c<<"x^"<<p[i].e<<endl;
			}
	}
	int eval(int x){
        int val = 0;
		for(int  i=0;i<n;i++)
		{
            val = val + ((p[i].c)*(power(x,p[i].e)));
		}
		return val;

	}
    int getExp(int x){return p[x].e;}
    int getCoef(int x){return p[x].c;}
    void putcoef(int x,int tot, int exp){
        p[x].c=tot;
        p[x].e=exp;
    }

    int calcnoterms(polynomial p2){
        int c=0,i=0,j=0;
        while(i<n && j<p2.n){
            if(p[i].e>p2.getExp(j)){c++;
            i++;
            }
            else if(p[i].e<p2.getExp(j)){
            c++;
            j++;
            }
            else{
            c++;
            i++;
            j++;
            }
        }
        if(i<n){
            c = c + (n - i);
        }
        if(j<p2.n){
            c = c + (p2.n - j);
        }
        return c;
    }

    void add(polynomial p1){
        int cal = calcnoterms(p1);
        polynomial temp(cal);
       int i=0,j=0,k=0;
       while(i<n && j<p1.n)
       {
           if(p[i].e>p1.getExp(j))
           {
               temp.putcoef(k,p[i].c,p[i].e);
               k++;
               i++;
           }
           else if(p[i].e<p1.getExp(j))
           {
                temp.putcoef(k,p1.getCoef(j),p1.getExp(j));
                j++;
                k++;
           }
           else{
           int v;
           v=p[i].c + p1.getCoef(j);
           temp.putcoef(k,v,p[i].e);
           k++;
           j++;
           i++;
           }
       }
       while(i<n){
           temp.putcoef(k,p[i].c,p[i].e);
           i++;
           k++;
       }
       while(j<p1.n){
        temp.putcoef(k,p1.getCoef(j),p1.getExp(j));
        j++;
        k++;
       }
       cout<<"The addition is : ";
       temp.showOutput();
     //return temp;
    }

    int power(int m,int n){
        int p = 1;
        for(int i = 0; i<n; i++)
        {p = p * m;  }
        return p;
        }

    void multiply(polynomial p1){
        int noTerms = (n*p1.n);
        polynomial temp(noTerms);
        int c = 0,i=0,j=0,t=0,exp,flag;
        while(j<p1.n){
        for(i=0;i<n;i++){
            exp = p[i].e + p1.getExp(j);
           // cout<<"Expo is "<<exp<<endl;
            for(int k = 0 ; k<noTerms;k++){
               // cout<<"In first if \n";
                flag = 0;
                int m = temp.getExp(k);
                 // cout<<"val of m "<<m<<endl;
                if(m == exp){
                   // cout<<"In 2 If \n";
                    int v = (temp.getCoef(k) + (p[i].c * p1.getCoef(j)));
                    temp.putcoef(k,v,exp);
                    flag = 1;
               }
                if(flag == 1){
                  //  cout<<"In 3 If \n";
                break;
                }
            }
            if(flag == 0){
               // cout<<"In 3 If \n";
                int v = (p[i].c * p1.getCoef(j));
              //    cout<<"val of v "<<v<<endl;
                temp.putcoef(t,v,exp);
                t++;
                c++;
              //  cout<<"val of c "<<c<<endl;
            }


        }
        j++;
        }
        temp.n = c;
        temp.showOutput();
     }
    void operator * (polynomial p1){
        int noTerms = (n*p1.n);
        polynomial temp(noTerms);
        int c = 0,i=0,j=0,t=0,exp,flag;
        while(j<p1.n){
        for(i=0;i<n;i++){
            exp = p[i].e + p1.getExp(j);
           // cout<<"Expo is "<<exp<<endl;
            for(int k = 0 ; k<noTerms;k++){
               // cout<<"In first if \n";
                flag = 0;
                int m = temp.getExp(k);
                 // cout<<"val of m "<<m<<endl;
                if(m == exp){
                   // cout<<"In 2 If \n";
                    int v = (temp.getCoef(k) + (p[i].c * p1.getCoef(j)));
                    temp.putcoef(k,v,exp);
                    flag = 1;
               }
                if(flag == 1){
                  //  cout<<"In 3 If \n";
                break;
                }
            }
            if(flag == 0){
               // cout<<"In 3 If \n";
                int v = (p[i].c * p1.getCoef(j));
              //    cout<<"val of v "<<v<<endl;
                temp.putcoef(t,v,exp);
                t++;
                c++;
              //  cout<<"val of c "<<c<<endl;
            }


        }
        j++;
        }
        temp.n = c;
        temp.showOutput();
    }

    void operator + (polynomial p1){
        int cal = calcnoterms(p1);
        polynomial temp(cal);
       int i=0,j=0,k=0;
       while(i<n && j<p1.n)
       {
           if(p[i].e>p1.getExp(j))
           {
               temp.putcoef(k,p[i].c,p[i].e);
               k++;
               i++;
           }
           else if(p[i].e<p1.getExp(j))
           {
                temp.putcoef(k,p1.getCoef(j),p1.getExp(j));
                j++;
                k++;
           }
           else{
           int v;
           v=p[i].c + p1.getCoef(j);
           temp.putcoef(k,v,p[i].e);
           k++;
           j++;
           i++;
           }
       }
       while(i<n){
           temp.putcoef(k,p[i].c,p[i].e);
           i++;
           k++;
       }
       while(j<p1.n){
        temp.putcoef(k,p1.getCoef(j),p1.getExp(j));
        j++;
        k++;
       }
       cout<<"The addition is : ";
       temp.showOutput();
    }

friend void operator >>(istream &in,polynomial p);
friend void operator <<(ostream &out,polynomial p);
};
 void operator >>(istream &in,polynomial p1)
{
    cout<<"Enter the coefficient and the exponent\n";
    for(int i = 0; i<p1.n ; i++){
        in>>p1.p[i].c;
        in>>p1.p[i].e;
    }
}

void operator <<(ostream &out,polynomial p1){
    for(int i = 0;i<p1.n;i++){
        if(i!=(p1.n-1))
        cout<<p1.p[i].c<<"x^"<<p1.p[i].e<<" + ";
        else
        cout<<p1.p[i].c<<"x^"<<p1.p[i].e<<endl;
        }

}



int main() {
    int x;
    polynomial p1;
   // p1.getInput();
    cin>>p1;
    //p1.showOutput();
    cout<<p1;
    polynomial p2;
    p2.getInput();
    p2.showOutput();
   // p1.add(p2);
    p1.multiply(p2);
    cout<<endl;
    p1 * p2;

    p1 + p2;
    /*cout<<"Enter value for x \n";
    cin>>x;
    int value = p1.eval(x);
    cout<<"The value of polynomial at "<<value<<endl;*/
    //cout << "Assignment 3 POLYNOMIALS" << endl; // prints Assignment 3 POLYNOMIALS
	return 0;
}
