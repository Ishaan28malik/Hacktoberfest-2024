import java.util.Scanner;
public class Main {
    public void bubble_sort(){
        Scanner sc=new Scanner(System.in);
        System.out.println("How many numbers you want to sort ? ");
        int a=sc.nextInt();
        int temp;
        int[] b=new int[a];
        System.out.println("Enter The Numbers :- ");
        for(int i=0;i<a;i++)
        {
            b[i]=sc.nextInt();
        }
        System.out.print("Numbers you entered :- ");
        for(int k:b)
        {
            System.out.print(k+" ");
        }
        System.out.println();
        for(int j=0;j<b.length;j++){
            for(int z=0;z<b.length-1-j;z++){
                if(b[z]>b[z+1])
                {
                    temp=b[z];
                    b[z]=b[z+1];
                    b[z+1]=temp;
                }
            }
        }
        System.out.print("Sorted :- ");
        for(int p:b){
            System.out.print(p+" ");
        }
    }
    public static void main(String[] args) {
        Main obj=new Main();
        obj.bubble_sort();
    }
}