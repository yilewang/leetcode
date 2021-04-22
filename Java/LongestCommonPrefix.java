public class LongestCommonPrefix {

	public static void main(String[] args) {
		
		String [] strs = {"flower", "flow", "flight"};
	
		
		// if there is no component 
		if (strs.length == 0) {
			System.out.println(""); 
		}
		else if (strs.length == 1)
		{
			System.out.println(strs[0]);
		}
		
		 
		//Set length to be the shortest component's length 
		 int length = strs[0].length();
		for (int f = 1; f < strs.length; f++) {
			if (strs[f].length() <= strs[f-1].length())
			{
				length = strs[f].length();
			}
		}
		
		System.out.println(length);
		
		
		
		for (int i = 1; i < length; i++)
		{
			
			for (int j = 0; j < length; j++)
			{
				char a = strs[0].charAt(j);
				char b = strs[i].charAt(j);
				
				if (a!=b)
				{
					length = j;
				}
			}
			
			
			
		}
		
		System.out.println(strs[0].substring(0, length));
		
		
		
	}

}
