import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;
public class queue{
public static void main(String[] args){
	Queue<Integer> q= new LinkedList<>();
	System.out.println("Element pushed in Queue: " + q.add(10));
	System.out.println("Element pushed in Queue: " + q.add(20));
	System.out.println("Queue is: " + q);
	System.out.println("Element removed in Queue: " + q.remove()); 
	System.out.println("Queue is: " + q);
	}
}
