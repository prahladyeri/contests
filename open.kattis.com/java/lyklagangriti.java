import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class lyklagangriti {
	
	public static void main(String[] args) throws IOException {
		//Scanner sc = new Scanner(System.in);
		BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
		String s = bi.readLine();

		//String s = sc.nextLine();
		Deque<Character> l = new ArrayDeque<Character>();
		Deque<Character> r = new ArrayDeque<Character>();
		for(int i=0;i<s.length();i++) {
			char c = s.charAt(i);
			char item;
			switch(c) {
				case 'L':
					item = l.pollLast();
					r.addFirst(item);
					break;
				case 'R':
					item =r.pollFirst();
					l.addLast(item);
					break;
				case 'B':
					l.pollLast();
					break;
				default:
					l.addLast(c);
			}
		}
		StringBuilder sb  = new StringBuilder(l.size() + r.size());
		for(char c : l) {
			sb.append(c);
		}
		for(char c : r) {
			sb.append(c);
		}
		System.out.println(sb);
	}
}