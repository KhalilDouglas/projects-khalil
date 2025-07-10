for num in range(12):
    if(num % 3 == 0 and num % 5 == 0):
        print(num, "fizz buzz") 
    elif(num % 5):
        print(num, "Buzz")
    elif(num % 3):
        print(num, "fizz")
    else:
      print("none") 
    if num%2 ==0:
        print(num, "even")
    else:
        print(num, "odd")