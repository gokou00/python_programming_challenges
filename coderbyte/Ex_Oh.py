def ExOh(str):
    str = str.lower()
    num_of_x = str.count("x")
    num_of_o = str.count("o")
    return str.count("x") == str.count("o")


print(ExOh("xox"))



    