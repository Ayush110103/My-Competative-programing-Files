#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
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
int top(struct Stack* stack)
{
    if (isEmpty(stack))
        return INT_MIN;
    return stack->array[stack->top];
}

int main(){
    int n;
    scanf("%i" , &n);
    struct Stack* stack = createStack(n);
    for (int i = 0; i < n;i++){
        int a;
        scanf("%i" , &a);
        push(stack, a);

    }
    struct Stack* pos = createStack(n);
    struct Stack* neg = createStack(n);
    while(stack->top>=0){
        if(top(stack)<0){
            int x = top(stack);
            push(neg, x);
            pop(stack);
        }
        if(top(stack)>0){
            if(isEmpty(neg)){
                int y = top(stack);
                push(pos, y);
                pop(stack);
            }
            else{
                if(abs(top(neg))>abs(top(stack))){
                    pop(stack);
                }
                else if(abs(top(neg))==abs(top(stack))){
                    pop(stack);
                    pop(neg);
                }
                else if(abs(top(neg))<abs(top(stack))){
                    pop(neg);

                }

            }
        }



    }
    while(neg->top>=0){
        printf("%d ", neg->array[neg->top]);
        pop(neg);
    }
    while(pos->top>=0){
        printf("%d ", pos->array[pos->top]);
        pop(pos);
    }

    

}