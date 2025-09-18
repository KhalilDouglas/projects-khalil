def count_down_to_bday( days_left):
    if days_left <=0: 
        print("The bday is happening today")

    else:
        for i in range(days_left,0,-1):
              print(f"{i} days left until bday") 
              print("It's time for bday")

count_down_to_bday(45)             