import java.util.*;
import java.text.*;

class Spavanac {
	static final long ONE_MINUTE_IN_MILLIS=60000;//millisecs
	static final SimpleDateFormat fmt = new SimpleDateFormat("HH mm");

	public static void main(String[] args) throws ParseException {
		//System.out.println("Welcome!");
		//SimpleDateFormat fmt = new SimpleDateFormat("dd-MM-yyyy HH:mm");
		Scanner sc = new Scanner(System.in);
		// System.out.println("calling hasNextLong");
		// sc.hasNextLong();
		// System.out.println("calling nextLong1");
		// sc.nextLong();
		// System.out.println("calling nextLong2");
		// sc.nextLong();
		// System.out.println("called");
		while(sc.hasNextLong()) {
			long a = sc.nextLong(), b = sc.nextLong();
			long dtTo = fmt.parse(a + " " + b).getTime();
			Date dtFrom = new Date(dtTo + (-45 * ONE_MINUTE_IN_MILLIS)); //subtract 45 minutes
			String sr = fmt.format(dtFrom);
			String[] ss = sr.split(" ");
			int h = Integer.parseInt(ss[0]);
			int m = Integer.parseInt(ss[1]);
			System.out.println( h + " " + m);
		}
	}
}
