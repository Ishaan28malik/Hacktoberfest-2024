package Ds.LinkedList;
import java.util.*;
public class Intro {

	public static void main(String[] args) {
		
      MyLinkedList<String> myLL = new MyLinkedList();
      
      for (int i=0; i<10;i++) {
    	  myLL.add(i+" hemlo");
      }
      myLL.print();
		
	}
}
