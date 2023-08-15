#include <stdio.h>
 // for malloc()
#include <stdlib.h>
#include <math.h>

typedef struct Node {
    int data;
    struct Node* next;
}Node;
 
/* Function to create a
new node with given data */
Node* newNode(int data)
{
    Node* new_node = (Node *)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}
 
/* Function to insert a node at the
beginning of the Singly Linked List */
void push(Node** head_ref, int new_data)
{
    /* allocate node */
    Node* new_node = newNode(new_data);
    /* link the old list off the new node */
    new_node->next = (*head_ref);
    /* move the head to point to the new node */
    (*head_ref) = new_node;
}
 
/* Adds contents of two linked lists and
return the head node of resultant list */
Node* addTwoLists(Node* first, Node* second)
{
    // res is head node of the resultant list
    Node* res = NULL;
    Node *temp, *prev = NULL;
    int carry = 0, sum;
 
    // while both lists exist
    while (first != NULL || second != NULL) {
        
        sum = carry + (first ? first->data : 0) + (second ? second->data : 0);
        
        if(sum==1){
            carry = 0;
        }
        if(sum==2){
            carry = 1;
            sum = 0;
        }
        if(sum==3){
            carry = 1;
            sum = 1;
        }

        // update sum if it is greater than 10
        // sum = sum % 10;
        // Create a new node with sum as data
        temp = newNode(sum);
        // if this is the first node then set it as head of the resultant list
        if (res == NULL)
            res = temp;
        // If this is not the first node then connect it to the rest.
        else
            prev->next = temp;
       
        // Set prev for next insertion
        prev = temp;
 
        // Move first and second pointers to next nodes
        if (first)
            first = first->next;
        if (second)
            second = second->next;
    }
    if (carry > 0)
        temp->next = newNode(carry);
    // return head of the resultant list
    return res;
}
 
Node* reverse(Node* head)
{
    if (head == NULL || head->next == NULL)
        return head;
    // reverse the rest list and put the first element at the end
    Node* rest = reverse(head->next);
    head->next->next = head;
    head->next = NULL;
    // fix the head pointer
    return rest;
}
 
// A utility function to print a linked list
void printList(Node* node)
{
    while (node != NULL) {
        printf("%d  ",node->data);
        node = node->next;
    }
    printf("\n");
}
int bintoDec(Node* node,int l){
    int ans=0,c=0;
    while (node != NULL) {
        if(node->data ==1){
            ans += pow(2, l - c - 1);
        }
        c++;
        node = node->next;
    }
    return ans;
}
int getCount(struct Node* head)
{
    int count = 0; // Initialize count
    struct Node* current = head; // Initialize current
    while (current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}
/* Driver code */
int main(void)
{    int n,m;
        

    printf("\nEnter Any Decimal Numbers ");
    scanf("%i", & n);
    scanf("%i", & m);
    printf("\n");
    Node* res = NULL;
    Node* first = NULL;
    Node* second = NULL;
 
    
    if (n == 0){
        first->data=0;
        first->next = NULL;
    }
    else{
        while(n>0){
            int a = n % 2;
            n = n / 2;

            push(&first, a);
        }

    }
    if (m == 0){
        second->data=0;
        second->next = NULL;
    }
    else{
        while(m>0){
            int a = m % 2;
            m = m/ 2;

            push(&second, a);
        }

    }
    
    // reverse both the lists
    first = reverse(first);
    second = reverse(second);
    printf("Linked list fter reversing-");
    printList(first);
    printList(second);
    // Add the two lists
    printf("%d\n", first->data);
    res = addTwoLists(first, second);
 
    // reverse the res to get the sum
    res = reverse(res);
       printf("Resultant list is ");
    printList(res);
    int k = getCount(res);
    printf("%d\n", k);
    printf("%d" ,bintoDec(res, k));
    return 0;
}