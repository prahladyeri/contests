import java.util.*;
import java.lang.Math;

public class different {
	
	public static void main(String[] args) {
		Scanner n=new Scanner(System.in);
		String input;
		long a; long b;
		
		while(n.hasNextLine()) {
			input = n.nextLine();
			String[] parts = input.split(" ");
			a  = Long.parseLong(parts[0]);
			b = Long.parseLong(parts[1]);
			System.out.println(Math.abs(a-b));
		}
	}

}
