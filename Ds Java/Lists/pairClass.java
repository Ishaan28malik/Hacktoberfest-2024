package Ds.Lists;

public class pairClass<X,Y> {

	X x;
	Y y ;
	
	public pairClass(X x, Y y) {
		this.x=x;
		this.y= y;
	
		
	}
	public void getDescription() {
		System.out.println(x+" and "+y);
	}
}
