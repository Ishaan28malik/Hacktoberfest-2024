import java.util.Scanner;
class LeftistMethods{
    class Node{
        int element;
        int rank;
        Node left, right;

        Node(int element){
            this.element = element;
            left = null;
            right = null;
        }
    }
   private Node root;

    LeftistMethods(){
        root = null;
    }

    public void insert(int value){
        root = merge(new Node(value), root);
    }

    public void delete(){
        if(root == null){
            System.out.println("Tree is empty!");
        }
        System.out.println("Deleted element is "+root.element);
        root = merge(root.left, root.right);
    }

    private Node merge(Node x, Node y) {
        if (x == null)
            return y;
        if (y == null)
            return x;
        if (x.element > y.element) {
            Node temp = x;
            x = y;
            y = temp;
        }

        x.right =  merge(x.right, y);

        if(x.left == null){
            x.left = x.right;
            x.right = null;
        }
        else{
            if(x.left.rank < x.right.rank){
                Node temp = x.left;
                x.left = x.right;
                x.right = temp;
            }
            x.rank = x.right.rank + 1;
        }
        return x;
    }
    public void display(){
        displayRec(root,"", true);
    }
    public void displayRec(Node root, String indent, boolean last){
        if(root != null){
            System.out.print(indent);
            if(last){
                System.out.print("R----");
                indent += "  ";
            }
            else{
                System.out.print("L----");
                indent += "|  ";
            }
            System.out.println(root.element);
            displayRec(root.left, indent, false);
            displayRec(root.right, indent, true);
        }
    }
}


public class LeftistHeap {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        LeftistMethods obj = new LeftistMethods();
        while(true) {
            System.out.println("\nLeftist Heap Operations\n");
            System.out.println("1. Insert ");
            System.out.println("2. Delete");
            System.out.println("3. Display");
            System.out.println("4. Exit");

            int choice = scan.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter an element to insert: ");
                    obj.insert(scan.nextInt());
                    break;
                case 2:
                     obj.delete();
                     break;
                case 3:
                    obj.display();
                    break;
                default:
                    System.out.println("Invalid operation being performed. \n ");
                    return;
            }
        }
    }
}
