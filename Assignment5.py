#Q.1 leapyear
x=int(input("enter the leap year"))
if x%4==0:
 print("leap yaer")
else:
 print("not leap year")
 print("\n")


#Q.2 square or rectangle
length=input("enter the length")
breadth=input("enter the breadth")
if length==breadth:
    print("square")
else:
    print("rectangle")


#Q.3 oldest and youngest people
x=input("age of first people")
y=input("age of second people")
z=input("age of third people")
if x>=y and x>=z:
  print("first is  oldest")
elif  y>=x and y>=z:
    print("second people is oldest")
elif z>=x and z>=y:
    print ("third is oldest")
else :
    print ("all threes are equal")

#Q.4 Write an if statement for prize disturbution on their points
x=float(input("Enter marks"))
if x<=50:
    print("Sorry this time  no prize")
else :
    if x<=150:
        print(" you won wooden dog")
    else:
     if x<=180:
        print("you win a book")
     else:
        print("you win a Chocolates")


#Q.5 Shop will give account
x=int(input("Enter the quantity"))
if x*100>1000:
    print("cost is",((100*x)-(.1*100*x)))
else:
    print("cost is",x*100)
        
        
    


    
