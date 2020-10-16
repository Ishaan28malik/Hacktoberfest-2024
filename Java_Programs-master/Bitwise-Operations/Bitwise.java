import java.io.*;

public class Bitwise {
	public static void main(String args[])throws IOException {
		DataInputStream d=new DataInputStream(System.in);
		System.out.println("enter value for x:");
		int x=Integer.parseInt(d.readLine());
		System.out.println("\n enter value for y:");
		int y= Integer.parseInt(d.readLine());
		int choice;
		do {
			System.out.println("**********************");
			System.out.println("1.Bitwise AND");
			System.out.println("2.Bitwise OR");
			System.out.println("3.Bitwise XOR");
			System.out.println("4.Bitwise LEFT SHIFT");
			System.out.println("5.Bitwise RIGHT SHIFT");
			System.out.println("6.Bitwise NOT");
			System.out.println("7.EXIT");
			System.out.println("***********************");
			System.out.println("enter your choice:");
			choice=Integer.parseInt(d.readLine());
			switch(choice) {
				case 1:
					System.out.println("Bitwise AND OPERATION:"+(x&y));
					break;
				case 2:
					System.out.println("Bitwise OR OPERATION:"+(x|y));
					break;
				case 3:
					System.out.println("Bitwise XOR OPERATION:"+(x^y));
					break;
				case 4:
					System.out.println("LEFT SHIFT:"+(x<<y));
					break;
				case 5:
					System.out.println("RIGHT SHIFT:"+(x>>y));
					break;
				case 6:
					System.out.println("NOT of x :"+(~x));
					System.out.println("NOT of y :"+(~y));
					break;
				case 7:
					System.out.println("Thankyou");
					System.exit(1);
					break;
				default:
					System.out.println("Invalid chioce, Please enter the correct choice");
				}
		} while(choice!=7);
	}
}
