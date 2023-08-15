#include <stdio.h>
#include <stdlib.h>

struct Node {
    int value;
    int height;
    int size;
    struct Node* left;
    struct Node* right;
};

int max(int a, int b) {
    return (a > b) ? a : b;
}

int height(struct Node* node) {
    if (node == NULL) {
        return 0;
    }
    return node->height;
}

int size(struct Node* node) {
    if (node == NULL) {
        return 0;
    }
    return node->size;
}

int getBalance(struct Node* node) {
    if (node == NULL) {
        return 0;
    }
    return height(node->left) - height(node->right);
}

struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;
    newNode->height = 1;
    newNode->size = 1;
    return newNode;
}

struct Node* rotateRight(struct Node* y) {
    struct Node* x = y->left;
    struct Node* T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left), height(y->right)) + 1;
    y->size = size(y->left) + size(y->right) + 1;

    x->height = max(height(x->left), height(x->right)) + 1;
    x->size = size(x->left) + size(x->right) + 1;

    return x;
}

struct Node* rotateLeft(struct Node* x) {
    struct Node* y = x->right;
    struct Node* T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left), height(x->right)) + 1;
    x->size = size(x->left) + size(x->right) + 1;

    y->height = max(height(y->left), height(y->right)) + 1;
    y->size = size(y->left) + size(y->right) + 1;

    return y;
}

struct Node* insert(struct Node* root, int value) {
    if (root == NULL) {
        return createNode(value);
    }

    if (value < root->value) {
        root->left = insert(root->left, value);
    } else {
        root->right = insert(root->right, value);
    }

    root->height = max(height(root->left), height(root->right)) + 1;
    root->size = size(root->left) + size(root->right) + 1;

    int balance = getBalance(root);

    if (balance > 1 && value < root->left->value) {
        return rotateRight(root);
    }

    if (balance < -1 && value > root->right->value) {
        return rotateLeft(root);
    }

    if (balance > 1 && value > root->left->value) {
        root->left = rotateLeft(root->left);
        return rotateRight(root);
    }

    if (balance < -1 && value < root->right->value) {
        root->right = rotateRight(root->right);
        return rotateLeft(root);
    }

    return root;
}

int getNFSNumber(struct Node* root, int k) {
    if (root == NULL || k <= 0 || k > root->size) {
        return -1;
    }

    int leftSize = size(root->left);

    if (k == leftSize + 1) {
        return root->value;
    } else if (k <= leftSize) {
        return getNFSNumber(root->left, k);
    } else {
        return getNFSNumber(root->right, k - leftSize - 1);
    }
}

void printNFSNumbers(int arr[], int length) {
    struct Node* root = NULL;

    for (int i = 0; i < length; i++) {
        root = insert(root, arr[i]);
       int k;
        if((i+1)%5!=0){
            k = (i + 1) / 5 + 1; } 
        if((i+1)%5==0){
            k = (i + 1) / 5 ; } 
        // Calculate the NFS index
        int nfsNumber = getNFSNumber(root, k);
        printf("%d\n",nfsNumber);
    }
}

int main() {
    int length;

    scanf("%d", &length);

    int* arr = (int*)malloc(length * sizeof(int));

    for (int i = 0; i < length; i++) {
        scanf("%d", &arr[i]);
    }

    printNFSNumbers(arr, length);

    free(arr);

    return 0;
}
