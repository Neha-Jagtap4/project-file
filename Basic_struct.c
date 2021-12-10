#include<stdio.h>
#include<stdlib.h>

struct node{  //Size int =4,pointer=8 ......=12 sizeaah
    int data;
    struct node *next;   //Self-referincal DS
};

typedef struct node NODE;
typedef struct node *PNODE;
typedef struct node **PPNODE;

int main(){
    PNODE First = NULL;  //memory 8 byte gheil
    NODE obj; //kiti bytes store hoil.....12
    //struct node * first = NULL;
    


return 0;
}
 