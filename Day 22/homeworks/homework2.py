#შექმენით ფუნქცია სახელად manual_count: 
#ფუნქციას გადაეცემა სია და ასევე შესაძლოა ელემენტი. როდესაც ფუნქციას ელემენტიც გადაეცემა, თქვენ უნდა დაითვალოთ სიაში ამ ელემენტის რაოდენობა
#არ გამოიყენოთ count. როდესაც არ გადაეცემა ელემენტი, მისთვის გამოიყენეთ default მნიშვნელობა და გაუტოლეთ საწყისი სიის საშუალო არითმეტიკულს
#ოღონდ მთელი რიცხვის სახით (int(აქ საშუალოს კოდი)).

def manual_count(lst, element=-1):
    if element == -1:
        avarage = int(sum(lst) / len(lst))
    else:
        count = 0
        for i in lst:
            if i == element:
                count += 1
        return count
    
my_list = [1,2,3,4,3,5,6,7,3,8,9,3,8,4]

element_input = input("enter an element: ")
if element_input:
    element = int(element_input)
    result = manual_count(my_list, element)
else:
    result = manual_count(my_list)
print("result: ", result)

