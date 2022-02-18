

def primestring(s):
     se = set(s)
     print(se)
     if len(se) % 2 == 1 or len(se)== 2 :
          for i in se:
              # print(i)
               count = 0
               c = s.count(i)
               if c == 1:
                  return  print("c == 1 No")
                  #  break
                    #break
               
               elif c%2 == 1 or c == 2:
               
                    #print(f"{c} Yes\n")
                    continue
               
               else:
                   return  print("No count not prinme")
                    
                   # break
          print("Yes For loop")
                    #break
     else:
         return print("No 1st if")
        
        






if __name__ == "__main__":

    T = int(input())
    st = []
    for i in range(T):
        st.append(input())
    for s in st:
        primestring(s)