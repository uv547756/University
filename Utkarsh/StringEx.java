import java.io.*;
import java.util.Scanner;
public class StringEx{
public static void main(String args[]){
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter a String: ");	
	String str = sc.nextLine();
	System.out.println("Converting Lower to Upper Case: "+str.toUpperCase());
	System.out.println("Converting Upper to Lower Case: "+str.toLowerCase());
	System.out.println("Replace first character with last character: \n");
	System.out.println(str.replace(str.charAt(0),str.charAt(str.length()-1)));
	System.out.println("Removing white/empty spaces from string: \n"+str.trim());
	
	System.out.println("The length of string is: "+str.length());
	System.out.println("The character at 3rd position is: "+str.charAt(2));
	System.out.println("Substring from 5th position is: "+str.substring(4));
	}
}