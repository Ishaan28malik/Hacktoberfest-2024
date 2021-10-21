import java.util.LinkedList;
import java.util.Iterator;

public class LLInbuildReverse{
	public static void main(String args[]){
		LinkedList<String> ll = new LinkedList<String>();
		ll.add("Yaswanth");
		ll.add("Ajay");
		ll.add("Ajith");
		ll.add("Vijay");
		ll.add("Arun");

		Iterator<String> itr = ll.descendingIterator();
		while(itr.hasNext()){
			System.out.println(itr.next());
		}
	}
}


