import java.util.*;

class lyklagangriti {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		Stack<Character> l = new Stack<>();
		Stack<Character> r = new Stack<>();
		for(int i=0;i<s.length();i++) {
			char c = s.charAt(i);
			char item;
			switch(c) {
				case 'L':
					item = l.pop();
					r.push(item);
					break;
				case 'R':
					item =r.pop();
					l.push(item);
					break;
				case 'B':
					l.pop();
					break;
				default:
					l.push(c);
			}
		}
		for(char c : l) {
			System.out.print(c);
		}
		while(r.size() > 0) {
			char c = r.pop();
			System.out.print(c);
		}
		System.out.println("");
	}
}