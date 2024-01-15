txt1= "My name is {fname}, I'm {age}".format(fname ="John", age ="36")
print(txt1)

txt2= "My name is {0}, I'm {1}".format("John",60)
print(txt2)

mylist = ["John", "Peter", "Vicky"]
x = "#".join(mylist)
print(x)

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#",2)
print(x)

first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)
second_greek = ['omega', 'alpha', 'pi', 'gamma']
second_greek.sort()
print(second_greek)


