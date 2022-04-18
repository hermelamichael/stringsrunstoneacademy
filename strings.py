'''
ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt) # original string remains unchanged and a new string tt is created 
'''

'''
ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***" + ss.strip() + "***")  #removes l and t(r)
print("***" + ss.lstrip() + "***")
print("***" + ss.rstrip() + "***")

news = ss.replace("o", "***") #, indicates what you replace it with 
print(news)

'''

'''
food = "banana bread"
print(food.capitalize())

print("*" + food.center(25) + "*")
print("*" + food.ljust(25) + "*")     # stars added to show bounds
print("*" + food.rjust(25) + "*")

print(food.find("e"))
print(food.find("na"))
print(food.find("b"))

print(food.rfind("e"))
print(food.rfind("na"))
print(food.rfind("b"))

print(food.index("e"))
'''


food = "banana bread"
print(food.index("n"))

