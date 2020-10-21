import java.util.*;
class matrix{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the number of rows you want to make in the Matrix: ");
        int a= sc.nextInt();
        System.out.println("Enter the number of columns you want to make in the Matrix: ");
        int b= sc.nextInt();
        int[][] arr=new int[a][b];
        System.out.println("Enter the values in the matrix: ");
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
                arr[i][j]=sc.nextInt();
            }
        }
        System.out.println("The matrix you entered is: ");
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("The transpose of the matrix you enetered is: ");
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
                System.out.print(arr[j][i]+" ");
            }
            System.out.println();
        }
    }
}