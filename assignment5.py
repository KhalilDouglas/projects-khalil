num1 = input ('Enter the first number:')
num2 = input ('Enter the second number:') 
func = input ('Enter the function:')
if func == 'add':
    result = int (num1) + int (num2) 
elif func == 'sub':
    result = int(num1) - int(num2)
elif func == 'mult':
    result = int(num1) * int(num2)
elif func == 'div':
    result = int(num1) / int(num2)
elif func == 'power':
    result = int(num1) ** int(num2)  
else:
    print('Invalid function')
print (result)             