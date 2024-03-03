import java.util.Scanner;
class prime{
	public static void main(String args[]){
	Scanner no = new Scanner(System.in);
	System.out.print("Enter a Number: ");
	int num = no.nextInt();
	int count = 0;
	for(i=0;i<=num;i++){
	if(num%2 == 0){
		System.out.println(