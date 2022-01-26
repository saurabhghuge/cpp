def arrange (x,y):
    
    xn = len(x)
    yn = len(y)
    
    if(xn>yn):
        temp = x
        x = y
        y = temp


    for i in range(len(y)):
        flag = 0
        for j in range(len(x)):
            # print(y[i])
            # print(x[j])

            if y[i] == x[j]:
                flag = 1
                break
        if flag == 0:
            # print('hell')
            return(y[i])    
# x=[13, 5, 6, 2, 5]
# y= [5, 2, 5, 13]
x= [14, 27, 1, 4, 2, 50, 3, 1]
y =[2, 4, -4, 3, 1, 1, 14, 27, 50]
print(arrange(x,y))  
  # n= len(arr)
    # for i in range(0,n):
    #     arr[i] += (arr[arr[i]]%n)* n

    # for i in range(0,n):
    #     arr[i] = int(arr[i]/n)