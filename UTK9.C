#include <stdio.h>
#include <conio.h>
void main(){
int arr[10][10];
int i, j, m, n, a, b, val, temp, tem, d1, d2;
clrscr();
printf("Enter size of array: ");
scanf("%d %d",&m,&n);
//TAKING VALUES
printf("ENter value in array: \n");
for(i=0; i<m; i++){
	for(j=0; j<n; j++)
		scanf("%d",&arr[i][j]);
		}
//DISPLAYING
printf("The array is: \n");
for(i=0; i<m; i++){
	for(j=0; j<n; j++)
		printf("%d \t", arr[i][j]);
		printf("\n");
	}
//INSERTION
printf("Enter position of the element: ");
scanf("%d%d", &a, &b);
printf("Enter the value to be inserted: ");
scanf("%d",&val);
arr[a][b] = val;

printf("The modified array is: \n");
for(i=0;i<m;i++){
	for(j=0;j<n;j++)
	printf("%d \t",arr[i][j]);
	printf("\n");
	}
//DELETION
printf("Enter position of the element: ");
scanf("%d%d",&d1, &d2);
arr[d1][d2] = 0;
printf("The modified array is: \n");
for(i=0;i<m;i++){
	for(j=0;j<n;j++)
	printf("%d \t",arr[i][j]);
	printf("\n");
	}
//SPARSE MATRIX
getch();
}