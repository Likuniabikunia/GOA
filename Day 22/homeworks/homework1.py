# შექმენით ფუნქცია სახელად manual_pop, რომელსაც გადაეცემა სია და ასევე შესაძლოა ინდექსი. როდესაც გადაეცემა ინდექსი,
# სიიდან უნდა ამოიშალოს ამ ინდექსზე მყოფი ელემენტი და დაბრუნდეს სია ამ სახით. თუ ფუნქციას არ გადაეცემა index,
# მაშინ default მნიშვნელობა უნდა იყოს სიის ბოლო ელემენტი 
# ზოგადად pop როგორც მუშაობს. ამ დავალებაში რათქმაუნდა pop არ უნდა გამოიყენოთ

def manual_pop(lst, index=-1):
    if index == -1:
        index = len(lst) -1
    if index < 0 or index >= len(lst):
        return "Out of range"
    
    new_list = []
    for i in range(len(lst)):
        if i != index:
            new_list.append(lst[i])
    return new_list

my_list = [1,2,3,4,5,6,7,8,9]

index_input = input("enter an index: ")
if index_input:
    index = int(index_input)
    result = manual_pop(my_list, index)
else:
    result = manual_pop(my_list)

print("result: ", result)



