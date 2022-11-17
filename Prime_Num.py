print("Hello! welocme "
      "To prime world")

def prime ():
    num = int(input("Enter the number"))
    for i in range(2,num):
            if num % i==0:
                print('Not a prime number')
                break
    else:
        print('prime number')


prime ()
    
while (1):
    user_wish = int(input("To continue press 1 otherwise press 0 to exit"))
    if user_wish == 1:
        prime()
    elif user_wish == 0:
        break 

print("Thank You!")




    


