#include <stdio.h>
#include <stdlib.h>
 
typedef struct Node Node;
 
// Define the Tree Node here
struct Node {
    int value;
    // Pointers to the left and right children
    Node* left, *right;
};
 
 
Node* init_tree(int data) {
    // Creates the tree and returns the
    // root node
    Node* root = (Node*) malloc (sizeof(Node));
    root->left = root->right = NULL;
    root->value = data;
    return root;
}
 
Node* create_node(int data) {
    // Creates a new node
    Node* node = (Node*) malloc (sizeof(Node));
    node->value = data;
    node->left = node->right = NULL;
    return node;
}
 
void free_tree(Node* root) {
    // Deallocates memory corresponding
    // to every node in the tree.
    Node* temp = root;
    if (!temp)
        return;
    free_tree(temp->left);
    free_tree(temp->right);
    if (!temp->left && !temp->right) {
        free(temp);
        return;
    }
}
 
int tree_height(Node* root) {
    // Get the height of the tree
    if (!root)
        return 0;
    else {
        // Find the height of both subtrees
        // and use the larger one
        int left_height = tree_height(root->left);
        int right_height = tree_height(root->right);
        if (left_height >= right_height)
            return left_height + 1;
        else
            return right_height + 1;
    }
}
 
int main() {
    // Program to demonstrate finding the height of a Binary Tree
 
    // Create the root node having a value of 10
    Node* root = init_tree(10);
     
    // Insert nodes onto the tree
    root->left = create_node(20);
    root->right = create_node(30);
    root->left->left = create_node(40);
    root->left->right = create_node(50);
 
    // Find the height of the tree
    int height = tree_height(root);
    printf("Height of the Binary Tree: %d\n", height);
 
    // Free the tree!
    free_tree(root);
    return 0;
}

// Our task is to complete the function tree_height() which takes the root node of the tree as an input parameter and returns an integer denoting the height of the tree. If the tree is empty, return 0. 
