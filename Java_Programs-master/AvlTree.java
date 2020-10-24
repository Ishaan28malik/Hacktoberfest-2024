import java.util.*; 
public class Avltree
{
    
    static class node
     { 
       public long xkey,ykey; 
        public node left; 
        public node right; 
       public  int height; 
        public int count; 
        public Vector<Integer> wc;
        public node()
        {
            xkey=0;
            ykey=0;
            left=null;
            right=null;
            height=0;
            count=0;
            wc=new Vector<Integer>();
        }
    } 
    static class t
    {
       static int post;
        static long data;
        public t()
        {
            post=0;
            long data=0;
        }
    }
 
    static int height(node N) 
    { 
        if (N == null) 
            return 0; 
        return N.height; 
    }  
    static int max(int a, int b) 
    { 
        return (a > b) ? a : b; 
    } 

   static node newNode(long xkey,long ykey,int pos) 
    { 
        node node = new node(); 
        node.xkey = xkey;
        node.ykey = ykey; 
        node.left = null; 
        node.right = null; 
        node.height = 1;  
        node.count = 1; 
        node.wc.add(pos);
        return (node); 
    }  
    static node rightRotate(node y) 
    { 
        node x = y.left; 
        node T2 = x.right; 
        x.right = y; 
        y.left = T2;  
        y.height = max(height(y.left), height(y.right)) + 1; 
        x.height = max(height(x.left), height(x.right)) + 1; 
        return x; 
    } 
   static node leftRotate(node x) 
    { 
        node y = x.right; 
        node T2 = y.left; 
        y.left = x; 
        x.right = T2; 
        x.height = max(height(x.left), height(x.right)) + 1; 
        y.height = max(height(y.left), height(y.right)) + 1; 
        return y; 
    } 

   static int getBalance(node N) 
    { 
        if (N == null) 
            return 0; 
        return height(N.left) - height(N.right); 
    } 
  
    static node insert(node node, long xkey,long ykey,int pos) 
    { 
        
        if (node == null) 
            return (newNode(xkey,ykey,pos)); 
  
        if (xkey == node.xkey) { 
            (node.count)++; 
            node.wc.add(pos);
            return node; 
        } 
        if (xkey < node.xkey) 
            node.left = insert(node.left, xkey,ykey,pos); 
        else
            node.right = insert(node.right, xkey,ykey,pos); 
        node.height = max(height(node.left), height(node.right)) + 1; 
        int balance = getBalance(node); 
        if (balance > 1 && xkey < node.left.xkey) 
            return rightRotate(node); 

        if (balance < -1 && xkey > node.right.xkey) 
            return leftRotate(node); 

        if (balance > 1 && xkey > node.left.xkey) { 
            node.left = leftRotate(node.left); 
            return rightRotate(node); 
        } 
        if (balance < -1 && xkey < node.right.xkey) { 
            node.right = rightRotate(node.right); 
            return leftRotate(node); 
        } 
        return node; 
    } 
static void inorder(node r,t toy)
    {  t node=null;
        if (r != null)
        {
            inorder(r.left,toy);
            if(r.count==1)
            {
                toy.data=r.xkey;
                toy.post=r.wc.get(0);
                
            }
            inorder(r.right,toy);
        }
    }
     static void search(node r, long val,Vector<Integer> u)
    {
        
        while ((r != null))
        {
            long rval = r.xkey;
            if (val < rval)
                r = r.left;
            else if (val > rval)
                r = r.right;
            else
            {
                u=r.wc;
            
            }
        }
    } 
    public static void main (String[] args)
    {
        try
        {
            solution obj = new solution();
            obj.run(args);
        }
        catch (Exception e)
        {
            e.printStackTrace ();
        }
        }
    public void run (String[] args) throws Exception
    {
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in)); 
        StringTokenizer st = new StringTokenizer(scan.readLine()); 
        long t=Long.parseLong(next());
        long n;
        for(int i=1;i<=t;i++)
        {
            n=Long.parseLong(next());
            long key=4*n-1;
            node rootx=null;
            node rooty=null;
            Long[] x=new Long[2000001];
            Long[] y=new Long[2000001];
            for(int k=1;k<=n;k++)
            {
                
                x[k]=scan.nextLong();
                y[k]=scan.nextLong();
            }
            for(int k=1;k<=n;k++)
            {
                rootx=insert(rootx,x[k],y[k],k);
                rooty=insert(rooty,y[k],x[k],k);
            }
            t tx=new t();
            t ty=new t();
            inorder(rootx,tx);
            inorder(rooty,ty);
            Vector<Integer> txw=new Vector<Integer>();
            search(rootx,x[ty.post],txw);
            Vector<Integer> tyw=new Vector<Integer>();
            search(rooty,y[tx.post],tyw);
            int npos;
            if(txw.size()==1)
            {
                npos=txw.get(1);
            }
            else{
                npos=tyw.get(1);
            }
            long finalx,finaly;
            finalx=x[tx.post]+x[ty.post]-x[npos];
            finaly=y[tx.post]+y[ty.post]-y[npos];
            System.out.println(finalx +" "+finaly);

        } 
    }

}
    
  
