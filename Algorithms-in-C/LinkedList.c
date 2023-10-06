#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insert(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
}

void deleteAtIndex(struct Node** head, int index) {
    if (*head == NULL) {
        printf("Linked list is empty. Deletion is not possible.\n");
        return;
    }
    if (index == 0) {
        struct Node* temp = *head;
        *head = (*head)->next;
        free(temp);
        return;
    }
    struct Node* current = *head;
    struct Node* prev = NULL;
    int count = 0;
    while (current != NULL && count != index) {
        prev = current;
        current = current->next;
        count++;
    }
    if (count != index) {
        printf("Index out of range. Deletion is not possible.\n");
        return;
    }
    prev->next = current->next;
    free(current);
}

int search(struct Node* head, int key) {
    struct Node* current = head;
    int position = 0;
    while (current != NULL) {
        if (current->data == key) {
            return position;
        }
        current = current->next;
        position++;
    }
    return -1; // Element not found
}

void display(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node* head = NULL;
    int choice, data, index, key;
    while (1) {
        printf("\nLinked List Operations:\n");
        printf("1. Insert at the end\n");
        printf("2. Delete a node at an index\n");
        printf("3. Search for a value\n");
        printf("4. Display the linked list\n");
        printf("5. Exit\n\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter data to insert: ");
                scanf("%d", &data);
                insert(&head, data);
                break;
            case 2:
                printf("Enter the index to delete: ");
                scanf("%d", &index);
                deleteAtIndex(&head, index);
                break;
            case 3:
                printf("Enter the value to search: ");
                scanf("%d", &key);
                int position = search(head, key);
                if (position != -1) {
                    printf("Element %d found at position %d.\n", key, position);
                } else {
                    printf("Element %d not found in the linked list.\n", key);
                }
                break;
            case 4:
                printf("Linked List: ");
                display(head);
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice!\n");
        }
    }
    return 0;
}
