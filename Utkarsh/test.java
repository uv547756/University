import java.util.Scanner;
public class test{
static void checkMarks(int marks){
	if (marks > 100){
		throw new ArithmeticException("Marks Out Of Bounds");
	}
	else{
		System.out.println("Marks are " + marks);
	}
}

public static void main(String[] args){
	checkMarks(100);
	}
}