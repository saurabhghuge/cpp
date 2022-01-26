import math 
  
# Returns true if n can be written 
# as x ^ y 
def isPower(n) : 
  
    # Base case 
    if (n <= 1) : 
        return True
  
    # Try all numbers from 2 to sqrt(n) 
    # as base 
    print(math.sqrt(n))
    for x in range(2, (int)(math.sqrt(n)) + 1) : 
        p = x 
  
        # Keep multiplying p with x while 
        # is smaller than or equal to x 
        while (p <= n) : 
            print (f'p = {p}')

            p = p * x 
            print (f'p = {p} and {x}')

              
            if (p == n) : 
                return True
          
    return False
      
# Driver Program 
# for i in range(2, 100) : 
      
    # if (isPower(i)) : 
    #     print( i, end =" ")
print(isPower(165))