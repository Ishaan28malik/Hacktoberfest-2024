#include <malloc.h>
#include <stdio.h>
typedef struct treenode
{
    int data;
    struct treenode* lchild;
    struct treenode* rchild;
} node;
node* newnode(int data)
{
    node* newnode = (node*)malloc(sizeof(node));
    newnode->data = data;
    newnode->lchild = NULL;
    newnode->rchild = NULL;
    return newnode;
}
void inorder(node* root)
{
    if (root == NULL)
        return;
    inorder(root->lchild);
    printf("%d ", root->data);
    inorder(root->rchild);
}
void Mirrorify(node* root, node** mirror)
{
    if (root == NULL) {
        mirror = NULL;
        return;
    }
    *mirror = newnode(root->data);
    Mirrorify(root->lchild, &((*mirror)->rchild));
    Mirrorify(root->rchild, &((*mirror)->lchild));
}
int main()
{
    printf("\n\n\t\t\t19BCT0117\n\n");
    node* tree = newnode(10);
    tree->lchild = newnode(15);
    tree->rchild = newnode(29);
    tree->lchild->lchild = newnode(13);
    tree->lchild->rchild = newnode(5);
    printf("\nInorder traversal of original tree:\n");
    inorder(tree);
    node* mirror = NULL;
    Mirrorify(tree, &mirror);
    printf("\nInorder traversal of mirror tree:\n");
    inorder(mirror);
    printf("\n");
    return 0;
}
