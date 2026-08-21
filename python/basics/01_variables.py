# # variables
# name = "Tony Stark"
# age = 60
# role = "Iron Man"

# print(name)
# print(age)
# print(role)

# print(f"And I am {name}")
# print(f"I have {age} years expreience of arc reactor")

# a = int(input("Give a's value:"))
# b = 20

# sum = (a+b)
# diff = (a-b)
# prod = (a*b)
# # quotient = (a/b)
# # quotient = (b/a)
# print(f"The sum is: {sum}")
# print(f"The sum is: {diff}")
# print(f"The sum is: {prod}")
# if a!=0 and b!=0:
#     quotient = (b/a)
#     print(f"The sum is: {quotient}")
#     quotient = (a/b)
#     print(f"The sum is: {quotient}")
# else:
#     print("Cannot devided by Zero")

#                                   #String

# c = """Tony Stark died in endgame
# but will come with as Dr. Doom"""
# print(c)
# d = " Hello, World ! "
# e = "How are you?"
# f = d + e
# de = "It's High time to leave the Job and go to Land and \"Cultivate\" Rice"
# print(de)
# print(d[1])
# print(len(c))
# print("endgame" in c)
# print(d[-5:-2])
# print(d[2:5])
# print(d.upper())
# print(d.lower())
# print(d.strip())
# print(d.replace("H", "G"))
# print(d.split(","))
# print(f)
# if "died" in c:
#     print("Yes Died in c")
# if "World" not in c:
#     print("There is no World")
# for x in "banana":
#     print(x)


#                                       Number


# x= 1
# y =2.8
# z = 1j
# x1 = -35
# y1 = 35e4
# z1 = -87.7e100
# x2 = 3+5j
# print(x)
# print(x2)
# print(y)
# print(y1)
# print(x1)
# print(z)
# print(z1)
# a = float(x)
# b = int(y)
# c = complex(x)
# print(a)
# print(b)
# print(c)

# # Note Complex number can not be converted into another number type 

# # generate random number using random module 
# import random
# print(random.randrange(1,10))

#                               Boolean 

# print( 10>9)
# print(10 == 9)
# print(10<9)
# print(bool("Hello"))
# print(bool(15))


#                               LIST

# thisislist = ["PM", "GM", "TM", "PM"]
# thisislist1 = (("PM", "GM", "TM", "PM"))
# list1 = [1,2,3,4,5]
# list2 = [True, False, False]
# list3 = ["Aam", "Jam", "Kola", "Lichu","Kathal"]
# list4 = ["Doyel", "3", "shalik", 5, False]
# print(thisislist)
# print(thisislist1)
# print(len(thisislist))
# print(list1)
# print(type(list1))
# print(list2)
# print(type(list2))
# print(list3)
# print(type(list3))
# print(list4)
# print(type(list4))

# for x in thisislist:
#     print(x)
# i=0
# while i<len(list3):
#     print(list3[i])
#     i = i+1

# [print(x) for x in list4]


#                           Dictionary

thisdict = {
    "Name" : "Julaibib",
    "Religion" : "Islam",
    "Year" : "670",
    "Year" : "672"

}
print(thisdict)
print(thisdict["Religion"])
print(len(thisdict))
print(type(thisdict))
x = thisdict.keys()
print(x)
thisdict["Country"] = "KSA"
print(x)
print(thisdict.values())
thisdict["Country"]= "Saudi Arabia"
print(thisdict.values())
z = thisdict.items()
print(z)
if "Country" in thisdict:
    print("Yse, Country is one of the keys in the this dict")
for x in thisdict:
    print(x)
    print(thisdict[x])
for x in thisdict.values():
    print(x)
for x in thisdict.keys():
    print(x)
thisdict.update({"Age":"100"})
thisdict.update({"Year":"960"})
print(thisdict)
thisdict.pop("Year")
print(thisdict)
thisdict.clear()
print(thisdict)
