a = int(input("Enter your age : "))

# if statement no 1
if( a%2==0 ):
    print("a is even")
else:
    print("a is odd")

# if statement number 2
if(a>18):
    print("you are adult")
    print("You are allowed to watch this movie")
elif(a<0):
    print("you are entering invalid age")
elif(a==0):
    print("you are entering zeor as age")
else:
    print("your not allowed to watch this movie")