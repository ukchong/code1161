"""
save a file
"""
file1 = open("random.txt", 'w')
file1.write("RANDOM TEXT")
file1.close()

filename = open("desktop_file.txt", 'w')
filepath = "../../../"
print("filepath + filename")


"""
Dictionary
"""

value ="hello"
my_dict = {"key" : value}
my_nested_dict = {"Name" : {"Last_Name" : "Kerr", "First_Name" : "Ewan"}, 
                            {"Date of Birth" : {"Day" : 4, "Month" : "November"}
                            }
    print(my_nested_dict["Date of Birth"])
