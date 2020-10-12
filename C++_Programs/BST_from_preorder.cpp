#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:
    int data;
     Node* left;
     Node* right;

};
Node* NewNode(int key)
{
    Node* temp=new Node();
    temp->data=key;
    temp->left=temp->right=NULL;
    return temp;
}
Node* buildTreeHelper(int pre[],int* preIndex,int preS,int preE,int size)
{

    if(*preIndex>=size||preS>preE)
    {

        return NULL;
    }
    Node* root= NewNode(pre[*preIndex]);
    *preIndex=*preIndex+1;
    if(preS==preE)
    {

        return root;
    }
    int i;
    for(i=preS;i<=preE;i++)
    {

        if(pre[i]>=root->data)
        {
            break;
        }
    }
    root->left=buildTreeHelper(pre,preIndex,*preIndex,i-1,size);
    root->left=buildTreeHelper(pre,preIndex,i,preE,size);
    return root;
}
Node *buildTree(int* pre,int size)
{
    int preIndex=0;
    return buildTreeHelper(pre,&preIndex,0,size-1,size);
}
void printInorder (Node* node)
{
    if (node == NULL)
        return;
    printInorder(node->left);
    cout<<node->data<<" ";
    printInorder(node->right);
}
int main()
{
   int pre[]={10,5,1,7,40,50};
   int size=sizeof(pre)/sizeof(pre[0]);
   Node* root=buildTree(pre,size);

   cout<<Inorde traversal of the constructed tree is;
   printInorder(root);
   return 0;
}
