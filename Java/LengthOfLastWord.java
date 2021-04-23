public class LengthOfLastWord {

	public static void main(String[] args) {
		
		String s = " ";
		
		String [] words = s.split(" ");
		
		if (s.isBlank())
		{
			System.out.println(0);
			
		}
		
        if (words.length >= 1 && words [words.length-1].equals(" "))
        {
            System.out.println(0);
        }
        
		System.out.println(words [words.length-1].length());
		
		

	}

}
