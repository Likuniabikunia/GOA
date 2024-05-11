#შექმენით ფუნქცია სახელად manual_min, რომელსაც შესაძლოა გადაეცეს მთელი რიცხვების სია 
#გაიხსენეთ function default argument.
#თუ ფუნქციას სია გადაეცემა, დააბრუნეთ ამ სიის მინიმალური მნიშვნელობა, არ გამოიყენოთ min. 
#თუ ფუნქციას არ გადაეცემა სია, მაშინ იმუშავეთ 1-იდან 10-ის ჩათვლით არსებული მთელი რიცხვების სიაზე.

def manual_min(lst=[]):
    if len(lst)== 0:
        lst = list(range(1,10 + 1))
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value
my_list = [4,7,10,3,5,1000,454,242,7896]

result = manual_min(my_list)
print("min: ", result)

