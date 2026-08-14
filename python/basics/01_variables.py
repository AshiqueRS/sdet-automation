# variables
name = "Tony Stark"
age = 60
role = "Iron Man"

print(name)
print(age)
print(role)

print(f"And I am {name}")
print(f"I have {age} years expreience of arc reactor")

a = int(input("Give a's value:"))
b = 20

sum = (a+b)
diff = (a-b)
prod = (a*b)
# quotient = (a/b)
# quotient = (b/a)
print(f"The sum is: {sum}")
print(f"The sum is: {diff}")
print(f"The sum is: {prod}")
if a!=0 and b!=0:
    quotient = (b/a)
    print(f"The sum is: {quotient}")
    quotient = (a/b)
    print(f"The sum is: {quotient}")
else:
    print("Cannot devided by Zero")

#String

c = """Tony Stark died in endgame
but will come with as Dr. Doom"""
print(c)
d = "Hello, World"
print(d[1])
print(len(c))
print("endgame" in c)
if "died" in c:
    print("Yes Died in c")
if "World" not in c:
    print("There is no World")
for x in "banana":
    print(x)
