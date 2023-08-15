
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin >> n;
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  int x;
  for (int i = 0; i < n;i++){
    cin >> x;
    a[i] = x;
  }


   Node* temp = driverList->head;
  
    // Check for empty list.
   
  
    // Traverse the list.
    while (temp != NULL) {
        if(temp->data%X!=0){
          y->insert_node(temp->data);}
                }

        temp = temp->next;
    }
}
 

void deleteN(Node** head, int position)
{
    Node* temp;
    Node* prev;
    temp = *head;
    prev = *head;
    for (int i = 0; i < position; i++) {
        if (i == 0 && position == 1) {
            *head = (*head)->next;
            free(temp);
        }
        else {
            if (i == position - 1 && temp) {
                prev->next = temp->next;
                free(temp);
            }
            else {
                prev = temp;
                if (prev == NULL)
                    break;
                temp = temp->next;
            }
        }
    }
}

SinglyLinkedList *x = new SinglyLinkedKist();
