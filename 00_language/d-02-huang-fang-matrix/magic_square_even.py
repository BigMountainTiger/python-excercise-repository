# Python program to print magic square of double order 

def DoublyEven(n): 
	
	arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)] 

	for i in range(0,n//4): 
		for j in range(0,n//4): 
			arr[i][j] = (n*n + 1) - arr[i][j]; 
	
	for i in range(0,n//4): 
		for j in range(3 * (n//4),n): 
			arr[i][j] = (n*n + 1) - arr[i][j]; 

	for i in range(3 * (n//4),n): 
		for j in range(0,n//4): 
			arr[i][j] = (n*n + 1) - arr[i][j]; 
	

	for i in range(3 * (n//4),n): 
		for j in range(3 * (n//4),n): 
			arr[i][j] = (n*n + 1) - arr[i][j]; 
			
 
	for i in range(n//4,3 * (n//4)): 
		for j in range(n//4,3 * (n//4)): 
			arr[i][j] = (n*n + 1) - arr[i][j]; 
	

	for i in range(n): 
		for j in range(n): 
			print ('%2d ' %(arr[i][j]),end=" ") 
		print() 
		

n = 8
DoublyEven(n) 

 
