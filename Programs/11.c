#include<stdio.h>
#include<stdlib.h>
#include <limits.h>


// A structure to represent a stack
struct Stack {
    int top;
    unsigned capacity;
    int* array;
};

struct Stack* createStack(unsigned capacity)
{
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}

// Stack is full when top is equal to the last index
int isFull(struct Stack* stack)
{
    return stack->top == stack->capacity - 1;
}
 
// Stack is empty when top is equal to -1
int isEmpty(struct Stack* stack)
{
    return stack->top == -1;
}
 
// Function to add an item to stack.  It increases top by 1
void push(struct Stack* stack, int item)
{
    if (isFull(stack))
        return;
    stack->array[++stack->top] = item;
    // printf("%d pushed to stack\n", item);
}
 
// Function to remove an item from stack.  It decreases top by 1
int pop(struct Stack* stack)
{
    if (isEmpty(stack))
        return INT_MIN;
    return stack->array[stack->top--];
}

// Function to return the top from stack without removing it
int TOP(struct Stack* stack)
{
    if (isEmpty(stack))
        return INT_MIN;
    return stack->array[stack->top];
}



int main()
{   
    int n;
    int i;
    scanf("%i" , &n);
    struct Stack* stack = createStack(n);

    for(i = 0 ; i < n ; i++ ){
        int m;
        scanf("%i" , &m  );
        push(stack , m);
   
    }
    
    int c = stack->top;
    while(c > 0){
        int x;
        int i = c;

        if((stack->array[i])*(stack->array[i-1]) <0 ){
            if(abs(stack->array[i]) > abs(stack->array[i-1])){
                x = stack->array[i];
                pop(stack);
                pop(stack);
                push(stack , x);
                c--;
            }
            else if(abs(stack->array[i]) < abs(stack->array[i-1])){
                x = stack->array[i-1];
                pop(stack);
                c--;
            } 
            else{
                pop(stack);
                pop(stack);
                c=c-2;
            }       
        }
        else{
            c--;
        }
    }

    for(i = 0 ; i <= stack->top ; i++ ){
        printf("%d " , stack->array[i]);
    }
    
    return 0;
}