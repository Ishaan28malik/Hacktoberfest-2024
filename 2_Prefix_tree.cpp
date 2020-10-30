/*Program to Construct an Expression Tree for a Given Prefix Expression and perform recursive and non-recursive traversals*/

#include<iostream>

using namespace std;

struct TreeNode  //Representing the node template
{
	char data;
	struct TreeNode *left,*right;
}*root;

class StackNode  //For stacking the operands and nodes
{    
    public:
        TreeNode *tNode;
        StackNode *next; //a pointer representing next member of stack
        
        StackNode(TreeNode *tNode)//constructor
        {
            this->tNode = tNode;
            next = NULL;
        }
};

class ExpressionTree
{
    private:
        StackNode *top;
    public:
        ExpressionTree() //constructor
        {
            top = NULL;
        }

	//function prototypes for tree creation
	void buildTree(string);
	void insert(char);
	//function prototypes for stack operations
        void push(TreeNode *);
	TreeNode* pop();
	//function prototypes for tree display
	void display();
	void inorder(TreeNode *);
	void inorder_nonR(TreeNode *);
	void preorder(TreeNode *);
	void preorder_nonR(TreeNode *);
	void postorder(TreeNode *);
}; //End of class ExpressionTree declaration



void ExpressionTree :: buildTree(string eqn)
{
	for ( int i = eqn.length() - 1; i >= 0; i--) //Reserve the string
	{
                insert(eqn[i]);
	}

	root = top->tNode;
}//buildTree


void ExpressionTree :: insert(char ch)
{
	TreeNode *temp = new TreeNode;
	temp->left = temp->right = NULL;
	temp->data = ch;

	if ( ch >='0' && ch <='9')  //is digit-Operand?
		push(temp);
	else if (ch == '+' || ch == '-' || ch == '*' || ch == '/')//is Operator?
	{
		temp->left = pop();
		temp->right = pop();
		push(temp);
	}
	else { cout<<"Invalid Expression"<<endl; return;}
	
}//insert()

void ExpressionTree :: push(TreeNode *ptr)
{
	if (top == NULL)
		top = new StackNode(ptr);
	else
	{
		StackNode *nptr = new StackNode(ptr); //calls constructor of stack class
		nptr->next = top; 
		top = nptr;
	}
}//Push

TreeNode* ExpressionTree :: pop()
{
	if (top == NULL) { cout<<"Stack empty"<<endl; return 0; }
	else {
		TreeNode *ptr = top->tNode;
		top = top->next;
		return ptr;  //we r returning node
	}
}//Pop

void ExpressionTree::display()
{
	cout<<"\n Inorder : \t\t";
	inorder(root);
	cout<<"\n Inorder Nonrecursive : ";
	inorder_nonR(root);
	cout<<"\n Preorder : \t\t";
	preorder(root);
	cout<<"\n Preorder Nonrecursive : ";
	preorder_nonR(root);
	cout<<"\n Postorder : \t\t";
	postorder(root);
	cout<<"\n";
}//display

void ExpressionTree :: inorder(TreeNode *ptr)
{
            if (ptr != NULL)
            {
                inorder(ptr->left);
                cout<<"  "<<ptr->data;   
                inorder(ptr->right);            
            }    
}//inorder












void ExpressionTree ::preorder(TreeNode *ptr)
{
            if (ptr != NULL){
		cout<<"  "<<ptr->data;
                preorder(ptr->left);                   
                preorder(ptr->right);            
            }    
}//preorder

void ExpressionTree ::postorder(TreeNode *ptr)
{
            if (ptr != NULL){
                postorder(ptr->left);                  
                postorder(ptr->right);            
		cout<<"  "<<ptr->data; 
            }    
}//postorder

void ExpressionTree :: inorder_nonR(TreeNode *temp){
	top=NULL;
	while(temp!=NULL || top!=NULL)
	{
		while(temp!=NULL) { push(temp); temp=temp->left; } //Left subtree
		temp = pop();
		cout<<"  "<<temp->data;    //Print data
		temp=temp->right;     		//Right subtree
	}//outer while (temp!=NULL)
}//inorder_nonR()


void ExpressionTree :: preorder_nonR(TreeNode *temp){
	top=NULL;
	while(temp!=NULL || top!=NULL)
	{
		while(temp!=NULL) 
		{ 
			cout<<"  "<<temp->data;    //Print data
			push(temp); 
			temp=temp->left; 
		} //Left subtree
		temp = pop();
		temp=temp->right;     		//Right subtree
	}//outer while (temp!=NULL)
}//inorder_nonR()

 



int main()
{
	string s;
	cout<<"Expression Tree Test"<<endl;
	ExpressionTree et;
	cout<<"\nEnter equation in Prefix form: ";
	cin>>s;
	et.buildTree(s);
	cout <<"Traversals:\n";
	et.display();
	return 0;
}//main    






