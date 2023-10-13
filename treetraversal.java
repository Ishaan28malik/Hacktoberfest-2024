import java.util.*;
public class Tree
{
    Listnode root;
    class Listnode
    {
        int data;
        Listnode left;
        Listnode right;
        public Listnode()
        {
            this.left = null;
            this.right = null;
        }
        public Listnode(int val)
        {
            this.data = val;
            this.left = null;
            this.right = null;
        }
    }
    public Tree()
    {
        this.root = null;
    }
    public void create()
    {                                                        //      1
        Listnode temp = new Listnode(1);                     //     / \
        this.root = temp;                                    //    2   3
        temp.left = new Listnode(2);                         //    /\  /\
        temp.right = new Listnode(3);                        //   4  5 6 7
        temp.left.left = new Listnode(4);
        temp.left.right = new Listnode(5);
        temp.right.left = new Listnode(6);
        temp.right.right = new Listnode(7);
    }
    public void preorder(Listnode root)
    {
        if(root == null)
            return;
        System.out.print(root.data+" ");
        preorder(root.left);
        preorder(root.right);
    }
    public void postorder(Listnode root)
    {
        if(root == null)
            return;
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.data+" ");
    }
    public void inorder(Listnode root)
    {
        if(root == null)
            return;
        inorder(root.left);
        System.out.print(root.data+" ");
        inorder(root.right);
    }
    public static void main(String[] args)
    {
        Tree t = new Tree();                                 
        t.create();
        System.out.print("Preorder: ");
        t.preorder(t.root);
        System.out.println();
        System.out.print("Postorder: ");
        t.postorder(t.root);
        System.out.println();
        System.out.print("Inorder: ");
        t.inorder(t.root);
    }
}
