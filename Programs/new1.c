 #include<stdio.h>
#include<stdlib.h>




struct Node
{
    int data;
    struct Node *next;
    struct Node *prev;
};
struct Node* newNode(int data)
{
    struct Node* new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->prev = NULL;
    new_node->next = NULL;
    return new_node;
}
 
void Sum_b(struct Node**no_1 , struct Node**no_2){

    struct Node* ans=NULL , *temp , *last=NULL;
    int sum = 0;
    int carry = 0;

    while( *no_1 != NULL || *no_2 != NULL){

        sum = ( carry + (*no_1 ? (*no_1)->data : 0 ) +(*no_2 ? (*no_2)->data : 0 ) );

        if(sum==1){
            carry = 0;}
        
        else if(sum == 0){
            carry = 0;
        }
        else if(sum == 2){
            carry = 1;
            sum =0;
        }
        else{
            carry = 1;
            sum = 1;
        }
        (*no_1)->data = sum;

        if (*no_1){
            *no_1 = (*no_1)->next;
        }
        if (*no_2){
            *no_2 = (*no_2)->next;
     
        }
    }


    if (carry>0){
        temp = newNode(carry);
        temp->prev=(*no_1);
        (*no_1)->next = temp;
        
    }
    (*no_1) = temp;
    // printf("%d", ans->data);
    // return no_1 ;

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

void Display(struct Node *p){
    while(p != NULL){
        printf("%d" , p->data);
        p=p->next;
    }

}
void OppTransversal(struct Node *p){
    while(p != NULL){
        printf("%d" , p->data);
        p=p->prev;
    }

}

int main()
{
    int n , m;
    printf("enter");
    scanf("%i" , &n);
    scanf("%i" , &m);

    struct Node* no_1 = NULL;
    struct Node* no_2 = NULL;

    if( n == 0){
        no_1->data=0;
        no_1->next = NULL;
        no_1->prev = NULL;

    }
    else{

        struct Node *temp , *last;
        no_1 = (struct Node *)malloc(sizeof(struct Node));
        no_1->data = n%2;
        no_1->next = NULL;
        no_1->prev = NULL;
        last = no_1;
        int a =n/2;
        
        while (a>0){
            temp= (struct Node*)malloc(sizeof(struct Node));
            temp->data = a%2;
            temp->next = NULL;
            temp->prev = last;
            last->next = temp;
            last = temp;
            
            a = a/2;}

    }

    if( m == 0){
        no_2->data=0;
        no_2->next = NULL;
        no_2->next = NULL;

    }
    else{

        struct Node *temp , *last;
        no_2 = (struct Node *)malloc(sizeof(struct Node));
        no_2->data = m%2;
        no_2->next = NULL;
        no_2->prev = NULL;
        last = no_2;
        int a =m/2;
        
        while (a>0){
            temp= (struct Node*)malloc(sizeof(struct Node));
            temp->data = a%2;
            temp->next = NULL;
            temp->prev = last;
            last->next = temp;
            last = temp;
            
            a = a/2;}
        
}
Display(no_1);
printf("\n");
Display(no_2);
printf("\n");
int x = getCount(no_1);
int y = getCount(no_2);
// struct Node *ans = NULL;

if(x>=y){
    Sum_b(&no_1, &no_2);
}
else{
     Sum_b(&no_2, &no_1);
}
printf("%d", no_1->data);
Display(no_1);
OppTransversal(no_1);
return 0;
}