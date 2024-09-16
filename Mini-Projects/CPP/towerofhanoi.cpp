/*Link to base topic or base problem:-https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/*/
/*Link to problem:-https://practice.geeksforgeeks.org/problems/help-the-old-man/0*/
#include <iostream>
using namespace std;

void towerOfHanoi(int first, int auxilary, int last, int noOfPlates, int  moveNo, int &from1, int &to1, int &move) {
    /*if the move remaining is last move or there is only one dish left to shift from 1 to 3*/
    if(noOfPlates==1) {
		move++;
    	if(move==moveNo ) {
    		from1=first;
    		to1=last;
		}
        return;
    }
    /* else shift from last rod to auxilary rod*/
    towerOfHanoi(first,last,auxilary,noOfPlates-1,moveNo,from1,to1,move);
	move++;
	if(move==moveNo) {
    	from1=first;
    	to1=last;
    	return;
	}
	/* else shift from auxilary rod to first rod*/
    towerOfHanoi(auxilary,first,last,noOfPlates-1,moveNo,from1,to1,move);
}

int main() {
	//code
	int t;
	cin >> t;
	
	while(t--) {
	    
	    int noOfPlates, moveNo, from=0, to=0,move=0;
	    cin >> noOfPlates >> moveNo;
	    
	    towerOfHanoi(1,2,3,noOfPlates,moveNo,from,to,move);
	    
	    cout << from << " " <<to<<endl;
    }
	return 0;
}
/*
For Input:
2
2 2
3 2
your output is: 
1 3
1 2*/
/*
For Input:
3
2 2
3 4
4 5
your output is: 
1 3
1 3
3 1
time complexity:O(2^n-1)
*/
