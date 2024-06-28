#შექმენით ფუნქცია,რომელსაც გადაეცემა რიცხვების კოლექცია. თქვენ უნდა განიხილოთ მთლიანი კოლექცია: 
# თუ რიცხვი იქნება მთელი - გაამრავლეთ ორზე,
# ხოლო თუ რიცხვი იქნება ათწილადი - გაამრავლეთ ოთხზე. 
#ყველა რიცხვი დაამატეთ ახალ სიაში და დააბრუნეთ ეს სია.

# def numbers(n):
#     new_list = []
#     for num in n:
#         if num.is_integer():
#             new_list.append(num * 2)
#         else:
#             new_list.append(num * 4)
#     return new_list
# nums = [77,30,65,24,80]
# result = numbers(nums)
# print(result)




#შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. 
#ლუწ ინდექსებზე მყოფი სახელები გადაიყვანეთ uppercase-ში, ხოლო კენტ ინდექსებზე მყოფნი კი lowercase-ში.


# def word(arr):
#     names_list = []
#     for i in range(len(arr)):
#         if i % 2 == 0:
#             names_list.append(arr[i].upper())
#         else:
#             names_list.append(arr[i].lower())
#     return names_list

# names = ["lika", "AlEqSANdRe", "MATE"]f
# result = word(names)
# print(result)


#შექმენით ფუნქცია, რომელსაც გადაეცემა სია. თქვენი დავალებაა, რომ დააბრუნოთ ამ სიაში არსებული დუპლიკატები.


# def remove_same_numbers(lst):
#     my_list = []
#     for item in lst:
#         if item not in my_list:
#             my_list.append(item)
#     return my_list

# nums= [90,6,9,5,90,4,5,10,5,80]
# result = remove_same_numbers(nums)
# print(result)    


