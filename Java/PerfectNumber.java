public class PerfectNumber {

	public static void main(String[] args) {
		
		int num = 28; 
		 int div = 1; 
		    int sum = 0;
		     
		        
		        while (div < num)
		        {
		        	if (num%div == 0)
		            {
		              sum += div;
		               
		            }
		        	div++;
		        }
		        
		        System.out.println(num == sum);
	            
	        

	}

}
