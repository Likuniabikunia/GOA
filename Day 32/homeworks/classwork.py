#codewars 1

def get_count(sentence):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in sentence:
        if char in vowels:
            count += 1
    return count


#codewars 2
def square_digits(num):
    res_str = ""
    num_str = str(num)
    for i in num_str:
        res_str += str(int(i)**2)
    return int(res_str)


