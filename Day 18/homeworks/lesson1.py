#შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია. 
#თქვენ უნდა დააბრუნოთ გაფილტრული სია, სადაც უკვე მარტო 4-ის ჯერადები იქნება.


def sum_of_numbers(nums):
    result = []
    for num in nums:
        if num % 4 == 0:
            result.append(num)
    return result
numbers_list = [88,888,98,67]
print(sum_of_numbers(numbers_list))

