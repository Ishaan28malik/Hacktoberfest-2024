package Ds.Recursion;

import java.util.ArrayList;
import java.util.Scanner;

public class practice10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
      Scanner sc = new Scanner(System.in);
      String str = sc.next();
      ArrayList<String> res = gss(str);
      System.out.println(res);
	}
   static ArrayList<String> gss(String str){
	  if(str.length()==0) {
		  ArrayList<String> bln = new ArrayList<>();
		  bln.add("");
		  return bln;
	  }
	   char ch = str.charAt(0);
	   String ros = str.substring(1);
	   ArrayList<String> rres = gss(ros);
	   
	   ArrayList<String> my = new ArrayList<>();
	   for(String rtes : rres) {
		   my.add("" +rtes);
		
	   }
	   for(String rtes : rres) {
	
		   my.add(ch + rtes);
	   }
	   return my;
   }
}
