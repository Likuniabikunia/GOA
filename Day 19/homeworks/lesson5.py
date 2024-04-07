#Abbreviate a Two Word Name

def abbrev_name(name):
    name = name.upper()
    splited_name = name.split(" ")
    first_name = splited_name[0]
    lastname = splited_name[1]
    result = first_name[0] + "." + lastname[0]
    return result
print(abbrev_name("lika gigiashvili"))






