class pr2{
	public static void main(String args[]){
	System.out.println("Pattern for Z: ");
	for(int i=0; i<4; i++){
		System.out.print("*");
	if(i==3){
		System.out.println();
		for(int j=0; j<(i-1); j++)
			for(int k=0; k<=j; j++){
				System.out.print(" ");
