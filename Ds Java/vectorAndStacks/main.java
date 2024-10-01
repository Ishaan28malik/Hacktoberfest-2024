package Ds.vectorAndStacks;

public class main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
//        Vector <Integer> v = new Vector (); 
//        v.add(34);
//        v.add(4);
//        System.out.println(v); 
//		myStack <Integer> s = new myStack ();
//		s.push(12);
//		s.push(2);
//		s.push(36);
//		
//		int pop=s.pop();
//        System.out.println(pop);
//        pop=s.pop();
//        System.out.println(pop);
//        
//        int peek = s.peek();
//        System.out.println(peek);
		stack st = new stack();
		st.push(1);
		st.push(2);
		st.push(3);
		System.out.println(st.Top());
		st.pop();
		System.out.println(st.Top());
		st.pop();
		st.pop();
		st.pop();
		System.out.println(st.empty());
	}

}
