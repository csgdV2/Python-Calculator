# Getting the  Numbers

a = int(input("What is your first no? \n"))
b = int(input("What is your second no? \n"))

# Asking for specific operation

ask = input("What you want to do? \nMultiply = 1 \nDivide = 2 \nAdd = 3 \nSubstract = 4 \nPress the number corresponding to your need. \n")

# Printing the answer

if ask == "1" : {
    print("Your answer is ", a*b)
}
    
elif ask == "2" : {
    print("Your answer is ", a/b)
}
    
elif ask == "3" : {
    print("Your answer is ", a+b)
}
    
else ask == "4" : {
    print("Your answer is ", a-b)
}

# Printing the line we get when the Operation Input "ask" is wrong

else : {
    print("Your input is wrong please try again.")
}
