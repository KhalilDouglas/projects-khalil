count = 100
while (count > 0):
    if(count % 3 == 0 and count % 5 == 0):
        print("fizz buzz") 
    elif(count % 5):
        print("Buzz")
    elif(count % 3):
        print("fizz")
    count = count -1