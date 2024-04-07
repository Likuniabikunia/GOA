# მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. ეს რიცხვები გადაეცით ფუნქციას,
# for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები. შემდეგ მოახდინეთ გაფილტვრა,
# ისევ for ციკლით განიხილეთ თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, ახალ სიაში დაამატეთ მისი მეორე ხარისხი, 
# ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი კვადრატული ფესვი (0.5 ხარისხი).



def filtered_numbers(start_num,end_num):
    filtered_list = []
    for i in range(start,end):
        if i % 2 == 0:
            filtered_list.append(i ** 2)
        else:
            filtered_list.append(i ** 0.5)
    return filtered_list
start = int(input("enter the starter number: "))
end = int(input("enter the ending number: "))

list = filtered_numbers(start,end)
print(list)