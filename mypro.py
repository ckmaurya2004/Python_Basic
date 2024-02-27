for i in range(5):
    for j in range(5):
        if j==0 and i!=4 and i>0 and i<=4  or i==0 and j>0 and j<=4 or i==4 and j>0 and j<=4  :
            print("* ", end=" ")
        else:
            print(end="   ")
    for k in range(3):
        print("  ",end=" ")

   
    for  j in range(5):
        if (i==0 and j>=0 and j<=5 or j==0 and i>0 and i<=5 or j==4 and i>0 and i<=2 or i==2 and j>0 and j<=3):
            print("* ", end=" ")
        else:
            print(end="   ")
    for k in range(3):
        print("  ",end=" ") 
    for  j in range(7):
        #if( j==0 and i>0 and i<4  or i==0 and j>=1 and j<=2   or i==1 and j==3  or j==5 and i>0 and i<4 or j==4 and i>=0 or i==4 and j>=2 and j<=3):
        if j==0 and i>0 and i<3  or i==0 and j>=1 and j<=2  or i==1 and j==3 or i==0 and j>=4 and j<=5 or j==6 and i!=3 and i!=0 and i!=4   or i==3 and j==1 or i==3 and j==5 or i==4 and j==3:
            print("* ", end=" ")
        else:
            print(end="   ")
    for k in range(3):
        print(" ",end=" ") 
    for  j in range(5):
        if (i==0 and j>=0 and j<=5 or j==0 and i>0 and i<=5 or j==4 and i>0 and i<=2 or i==2 and j>0 and j<=3 or i==3 and j==3 or i==4 and j==4):
            print("* ", end=" ")
        else:
            print(end="   ")
    for k in range(3):
        print(" ",end=" ") 
    
   

   


# for i in range(5):
#     for j in range(5):
#         print("* ", end="")
#     for k in range(2):
#         print("  ",end="")
# for i in range(5):
#     for j in range(5):
#         print("* ", end="")
    print("\n")