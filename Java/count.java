import java.util.Scanner;
public class count{
public static int CountWords(String str){
	int count = 1;
	for(int i = 0; i<=str.length()-1; i++){
		if(str.charAt(i) == '' && str.charAt(i+1)!=''){
			count++;
		}
	}
	return count;
}

public static void main(String[] args){
	String Sentence;
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter a Sentence: ");
	sentence = nextLine();
	System.out.println("Total number of words in given Sentence: "+CountWords(sentence));
	}
}