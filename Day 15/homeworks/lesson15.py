#task 1

#Write a program that takes asks user for number (use input).
#If number is even, print that number is even. Else print that number is not even, also print next even number, 
#for example if input is 15, print 16.


# number = int(input("enter the number: "))
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")
#     print(number + 1)


#task 2
#Create a while loop that asks the user to enter a password. 
#Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.

# password = "Goa Best"

# number = input("Enter the password : ")

# while number != password:
#     print("password incorrent try again")
#     number = input("Enter the password: ")

# if number == password:
#     print("correct")


#task 3
#Write an algorithm that takes a string as input and returns True if first character of that string is "G".

# string = input("enter a string: ")

# if string[0] == "G" or string[0] == "g":
#     print("True")
# else:
#     print(False)

#task 4

#Ask user for five names (use input five times). Add all of them in one list and print only first three names.

# first_name = input("enter the name: ")
# second_name = input("enter the second name: ")
# third_name = input("enter the third name: ")
# fourth_name = input("enter the fourth name: ")
# fifth_name = input("enter the fifth name: ")

# list = [first_name, second_name, third_name, fourth_name, fifth_name]
# print(list[0:3])

#task 5

#Create a while loop that prints numbers from 10 to 0 (10-იდან 0-მდე).

# number = 10
# while number > 0:
#     print(number)
#     number = number - 1




#Implement a simple calculator that takes two numbers and an operator (+, -, *, /)
#as input from the user and performs the corresponding operation. 

# operations = input("choose an poerator +,-,*,/ :")

# num1 = int(input("enter the first number: "))
# num2 = int(input("enter the second number: "))

# if operations == "+":
#     print(num1 + num2)

# elif operations == "-":
#     print(num1 - num2)

# elif operations == "*":
#     print(num1 * num2)

# else:
#     if operations == "/":
#         print(num1 / num2)        



#ask the user to enter a name,and print last character of that string.



# name = input("enter the name: ")

# print(name[-1])


# using for loop ask user for a number.
# then create a list which will have even numbers in next range: from 0 to users number, then print the whole list

# number = int(input("enter the number: "))
# even_num_list = []

# for i in range(number):
#     if i % 2 == 0:
#         even_num_list.append(i)
# print(even_num_list)


