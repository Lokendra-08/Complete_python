# def a():
#     name="pp"
#     age=22

#     var=locals()
#     print(var)

# a()



#   Global variable

# age=22
# def a():
#     global age
#     age+=5
#     print(age)

# a()
# print(age)


# def outer():
#     def inner():
#         print("hello")
#     return inner()

# outer()



# def b(name: str, age: int):
#     print("Name : ",name)
#     print("Age : ",age)

# b(25,"abc")


def ab(name,l=[]):
    l.append(name)
    print(l)

ab("pp")
ab("dd")
ab("cc")