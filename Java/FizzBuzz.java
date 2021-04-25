import java.util.ArrayList;

public class FizzBuzz {

	public static void main(String[] args) {
		
		int n = 25; 
		long sum = 0; 
		ArrayList <String> words = new ArrayList<>();
		
		for (int i = 0; i < n; i++ ) {
			// if i is divisble by 3
			if ((i+1) % 3 ==0 && (i+1)% 5 != 0)
			{
				words.add("Fizz");
			}
			else if ((i+1)%5 ==0 && (i+1)% 3 != 0)
			{
				words.add("Buzz");
			}
			else if ((i+1)%5 ==0 && (i+1)% 3 == 0)
			{
				words.add("FizzBuzz");
			}
			else
				words.add(String.valueOf(i+1));	
			
		}
		
	
		
		System.out.println(words);

	}

	@Override
	public String toString() {
		return "FizzBuzz [toString()=" + super.toString() + "]";
	}

}
