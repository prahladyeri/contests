using System;

class Spavanac {
	static void Main() {
		//Console.WriteLine("Foo baar");
		String line = "";
		DateTime now = DateTime.Now;
		while((line = Console.ReadLine()) != null) {
			string[] split = line.Split(new char[] { ' ' }, StringSplitOptions.None);
			int h = Int32.Parse(split[0]);
			int m = Int32.Parse(split[1]);
			//Console.WriteLine(b + " " +  a);
			DateTime to = new DateTime(now.Year, now.Month, now.Day, h, m, 0);
			DateTime from = to.AddMinutes(-45);
			//Console.WriteLine(from.Hours + " " + from.Minutes);
			Console.WriteLine(Int32.Parse(from.ToString("HH")) + " " + Int32.Parse(from.ToString("mm")));
		}
	}
}