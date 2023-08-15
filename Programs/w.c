#include<stdio.h>
#include<stdlib.h>
#include <math.h>

struct Node
{
    int data;
    struct Node *next;
};
struct Node *no_2 = NULL;




//  fuction for displaying linked list 
void Display(struct Node *p){
    while(p != NULL){
        printf("%d" , p->data);
        p=p->next;
    }

}


int bintoDec(struct Node* node){
    int ans=0,c=0;
    while (node != NULL) {
        if(node->data ==1){
            ans += pow(2,c);
        }
        c++;
        node = node->next;
    }
    return ans;
}
struct Node* newnode(int data){
    struct Node* new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;

}



struct Node* Sum_b(struct Node*no_1 , struct Node*no_2){

    struct Node* ans=NULL , *temp , *last=NULL;
    int sum = 0;
    int carry = 0;

    while( no_1 != NULL || no_2 != NULL){

        sum = ( carry + (no_1 ? no_1->data : 0 ) +(no_2 ? no_2->data : 0 ) );

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
    

        temp = newnode(sum);
        if(ans ==NULL){
            ans = temp;

        }
        else{

            last->next = temp;
            
        }
        last = temp;

        if (no_1){
            no_1 = no_1->next;
        }
        if (no_2){
            no_2 = no_2->next;
     
        }
    }
    if (carry>0){
        last->next = newnode(carry);
    }
    // printf("%d", ans->data);
    return ans ;

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

    }
    else{

        struct Node *temp , *last;
        no_1 = (struct Node *)malloc(sizeof(struct Node));
        no_1->data = n%2;
        no_1->next = NULL;
        last = no_1;
        int a =n/2;
        
        while (a>0){
            temp= (struct Node*)malloc(sizeof(struct Node));
            temp->data = a%2;
            temp->next = NULL;
            last->next = temp;
            last = temp;
            
            a = a/2;}

    }

    if( m == 0){
        no_2->data=0;
        no_2->next = NULL;

    }
    else{

        struct Node *temp , *last;
        no_2 = (struct Node *)malloc(sizeof(struct Node));
        no_2->data = m%2;
        no_2->next = NULL;
        last = no_2;
        int a =m/2;
        
        while (a>0){
            temp= (struct Node*)malloc(sizeof(struct Node));
            temp->data = a%2;
            temp->next = NULL;
            last->next = temp;
            last = temp;
            
            a = a/2;}

    }


    Display(no_1);
    printf("\n");
    Display(no_2);
    printf("\n");

    struct Node* ans = NULL;
    ans = Sum_b(no_1, no_2);
    // printf("%d", ans);
    // printf("%d", ans->data);
    Display(ans);
    int r=bintoDec(ans);
    printf("\n");
    printf("%d",r);
}