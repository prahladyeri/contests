import java.util.*;
import java.lang.Math;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class threedprinter {
	
	public static void main(String[] args) throws IOException {
		BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bi.readLine());
		int minDays = 999;
		int totDays; int pp; int st;
		//for p in range(1, n+1): // these many printing days
		int p;
		for (p=1; p<n+1; p++); {
			pp = (int)Math.pow(2, (p-1)); // total printers created
			st = (int)Math.ceil(n/pp); // no. of days to create statues
			totDays = st + p -1;
			if (totDays <= minDays) minDays = totDays;
		}
		System.out.println(minDays);
	}
	
}