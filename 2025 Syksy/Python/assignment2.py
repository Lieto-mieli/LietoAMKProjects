#asks the user for their name and prints a hello message using it
name=input('What is your name?')
print(f"Hello {name}.")

#asks for two integers from the user then tells them the sum of those numbers and an equation to explain it
num0=int(input('Give me a whole number:'))
num1=int(input('Now give me another whole number:'))
result=int.__add__(num0,num1)
print(f"The sum of both given numbers is {result}. ( {num0} + {num1} = {result} )")