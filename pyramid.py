
def triangle(n): 
    for i in range(n):
        for j in range(i+1):
            print(end = "* ")
        for j in range(n-i-1):
            print("  ",end ="  " )
        for j in range(i+1):
            print(end = "* ")
    #for i in range(n):
        for j in range(i+1):
            print(end = "* ")
        for j in range(n-i-1):
            print("  ",end ="  " )
        for j in range(i+1):
            print(end = "* ")   
        print()    
      

    for i in range(0, n): 
       
        for j in range(0,n-i): 
            print(end="* ") 
     
        for j in range(0,i): 
          
            print("  ", end="  ")
        for j in range(0,n-i): 
            print(end="* ")
      
        print() 
"""    for i in range(n):
        for j in range(i+1):
            print(end = "* ")
        for j in range(n-i-1):
            print("  ",end ="  " )
        for j in range(i+1):
            print(end = "* ")
        print()"""    
  
n = 5
triangle(n) 