#include <stdio.h>
 // for malloc()
#include <stdlib.h>


// Node structure for stack
struct node {
        // store the remainder 
        int info;
        // self-referencing pointer to store address of next node
        struct node * next;
};

// last inserted node indicating an empty stack
struct node * head = NULL;

// push the remainder to stack
void push(int rem) {
        // Create a new node  
        struct node * new_node = malloc(sizeof(struct node));
        new_node -> info = rem;

        // new node points to the head node
        new_node -> next = head;

        // make new node as the head node so that it points to last inserted data
        head = new_node;
}



// printing function
void traverse() {
        struct node * temp;
        temp = head;

        printf("The Binary Equivalence = ");
        while (temp != NULL) {
                printf("%i", temp -> info);
                temp = temp -> next;
        }
        printf("\n");
        return;
}

// conversion function
void DecimalToBin(int number) {
        int r;

        while (number != 0) {
                r = number % 2;
                number = number / 2;
                push(r);
        }
}


int main() {

        int n,m;
         

        printf("\nEnter Any Decimal Numbers ");
        scanf("%i", & n);
        scanf("%i", & m);
        printf("\n");
        struct Node* res = NULL;
        struct Node* first = NULL;
        struct Node* second = NULL;

        DecimalToBin(n);
        // struct node * new_node1 = malloc(sizeof(struct node));
        // new_node1 -> info = NULL;
        // new_node1 -> next = head;
        traverse();

        head = NULL;

        DecimalToBin(m);
        // struct node * new_node2 = malloc(sizeof(struct node));
        // new_node2 -> info = NULL;
        // new_node2 -> next = head;
        traverse();
        
        return 0;
}
 