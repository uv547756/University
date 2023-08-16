#include <stdio.h>
#include <conio.h>
int top=-1;
int stack[10];
void pop(int n){
	if(top==-1)
	printf("Stack underflow");
	else{
	     printf("%d",stack[top]);
	     top = top-1;
	     }
	}
void push(int n){
	if(top==size-1)
	printf("Stack overflow");
	else{
	     top = top + 1;
	     stack[top] = n;
	     }
	}
void display(int n){
	for(int i=0; i<
void main(){
int size;
clrscr();
printf("Enter size of stack: ");
scanf("%d",&size);
printf("Enter values of stack: ");
for(int i=0; i<size; i++){
	scanf("%d",&stack[i]);
	}
getch();
}




