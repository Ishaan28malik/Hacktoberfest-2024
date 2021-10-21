import java.util.*;
public class ArrayInsertDynmic{
	public static void main(String args[]){
		
		ArrayList arr = new ArrayList();

		//insertion
		arr.add(4);
		arr.add(3);

		System.out.println(arr);
		//insert at start
		arr.set(0,34);

		System.out.println(arr);

		//check wheter it exists or not
		System.out.println(arr.contains(34));

		arr.remove(1);

		System.out.println(arr);

		arr.clear();

	}
}

