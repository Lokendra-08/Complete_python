# def file_open(file):
#     try:
#         with open(file,'r') as f:
#             content=f.read()
#             print("File name : ",f.name)
#             print("File mode : ",f.mode)
#             print("File is readable : ",f.readable())
#             print("File is writable : ",f.writable())
#             print("Content : ",content)
#     except FileNotFoundError as e:
#         print(e)

# file_open("abc.txt")

# import os
# print(os.path.isfile("abcd.txt"))





# with open("abc.txt",'w') as f:
    

    #   read() function
    
    # data=f.read(10)
    # print(data)
    # data1=f.read(5)
    # print(data1)



    #   readline() function

    # data=f.readline()
    # print(data,end="")
    # data1=f.readline()
    # print(data1,end="")



    #   readlines() function

    # data=f.readlines()
    # print(data)



    #   seek() and tell() method

    # print(f.tell())
    # data=f.read(5)
    # print(data)
    # print(f.tell())
    # f.seek(0)
    # data1=f.read(5)
    # print(data1)






    # Find number of characters, words and lines in a file

    # number_of_lines, number_of_words, number_of_chars = 0,0,0

    # for line in f:
    #     number_of_lines+=1
    #     line=line.strip("\n")
    #     number_of_chars +=len(line)
    #     words=line.split()
    #     number_of_words+=len(words)
    # print("Number of lines : ", number_of_lines)
    # print("Number of words : ", number_of_words)
    # print("Number of chars : ", number_of_chars)




    #   Writing to a file ---> write() method overwrite the exiting data in a file

    # f.write("How are you ")



# Q. Create a file and write data in it

# with open("hello.txt",'w') as f:
#     line_no=1
#     while True:
#         text=input(f"Enter the line number {line_no} : ")
#         f.write(text+"\n")
#         line_no+=1
#         ans=input("Do you want to input another line (y/n) : ")
#         if ans.lower()!="y":
#             break



# Q. Create a binary file and write data in it

import pickle
# with open("hello.dat",'ab') as bf:
#     while True:
#         e_no=int(input("Enter employee number : "))
#         e_name=input("Enter employee name : ")
#         basic_pay=float(input("Enter basic pay : "))
#         allowance= float(input("Enter allowance : "))
#         total_sal=basic_pay+allowance
#         print(total_sal)
#         data=[e_no,e_name,basic_pay,allowance,total_sal]
#         pickle.dump(data,bf)
#         ans=input("Do you want to enter another entry(y/n) : ")
#         if ans.lower()!='y':
#             break




# Q. Read data from binary file 

try:
    with open("hello.dat",'rb') as f:
        while True:
            data=pickle.load(f)
            print(data)
except EOFError as e:
    print(e)