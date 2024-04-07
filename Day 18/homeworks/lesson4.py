
#შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს. გვარის თითოეული ასო გადაიტანეთ ახალ სიაში. 
#შემდეგ for ციკლის გამოყენებით იმუშავეთ ამ სიაზე 
#მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია.

#solution 1

# def even_indexes(lastname):
#     char_list = []
#     even_index_char = []

#     for char in lastname:
#         char_list.append(char)

#     for index in range(len(char_list)):
#         if index % 2 == 0:
#             even_index_char.append(char_list[index])

#     return even_index_char
# lastname = input("what is your lastname: ")
# print(even_indexes(lastname))



#solution 2 

# def even_indexes(lastname):
#     even_indexes_char = []

#     for index in range(len(lastname)):
#         if index % 2 == 0:
#             even_indexes_char.append(lastname[index])

#     return '+'.join(even_indexes_char)

# lastname = input("enter your lastname: ")

# print(even_indexes(lastname))


#solution 3 

# def even_indexes(lastname):
#     result = ''

#     for index in range(len(lastname)):
#         if index % 2 == 0:
#             result = result + lastname[index]
#     return result

# lastname = input("enter your lastname: ")
# print(even_indexes(lastname))






