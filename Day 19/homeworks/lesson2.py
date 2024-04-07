#2)remove spaces

def no_space(x):
    result = ""
    for char in x:
        if char != " ":
            result = result + char
    return result
print(no_space("l i k a"))