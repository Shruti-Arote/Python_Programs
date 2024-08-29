## if elif:

if age >= 18:
    print("You are an Adult")
    print("You can Vote")
elif age < 18 and age > 3:
    print("You are in school")
else:
    print("You are a child")

print("thank you")


#Loops
# While loop

i = 1
while i<= 5:
    print(i)
    i = i+1

# outut:
    1
    2
    3
    4
    5

i = 1
while i <=5 :
    print(i * "*")
    i = i+1

#output:
    #*
    #**
    #***
    #****
    #*****
#Inverted triangle
i = 5
while i>=0:
    print(i * "*")
    i = i - 1

# for loop:

for item in range(5):
    print(item)
# output: 0 1 2 3 4

for i in range(5):
    print(i + 1)
# output: 1 2 3 4 5


# List : collection of items
#        store in [] brackets

marks = [95, 98, 97]
print(marks)
# output: [95, 98, 97]

print(marks[0])
#output: 95

print(marks[-1])  # Note:- there are negative index in python which means it will start counting from back side or from right to left
# output: 97

print(marks[0:2]) # will return the list having 0th and 1st index items
# output: [95, 98]   , here 2nd index value will not print

# how to print list using loop

marks = [95, 98, 92]

for score in marks:
    print(score)
# output:
    # 95
    # 98
    # 92

## Operations on list: Mutable, Ordered

   # Append Operation: Add elements at the end of the list

marks = [95, 98, 92]
marks.append(99)
print(marks)
   # output: [95, 98, 92, 99]


  # Insert Operation : We can add element at any index

marks = [95, 98, 92]
marks.insert(0,91)  # first attribute is index and second one is item
print(marks)
   # Output : [91, 95, 98, 92]


  # 'in' Keyword : It will check if the element is exist in the list or not

marks = [95, 98, 92]
print(98 in marks)
  # output : True


  # len() : print the lenght of the list

marks = [95, 98, 92]
print(len(marks))
  # output: 3

marks = [95, 98, 92]
i = 0
while i < len(marks):
    print(marks[i])
    i = i+1

# print empty list : []
marks = [95, 98, 92]
marks.clear()
print(marks)


## Break Keyword:

students = ["ram","shyam","kishan","radha","radhika"]

for student in students:
    if student == "radha":
        break;
    print(student)

 # output: ram shyam kishan

## continue keyword:
students = ["ram","shyam","kishan","radha","radhika"]

for student in students:
    if student == "kishan":
        continue;    # everything will print except kishan
    print(student)

 # output : ram sham radha radhika


 ## Tuple : Immutable, (), if we do not apply perenthesis and directly write the values, by default it will considered as a tuple
           # ordered

 #marks = (95,93,97,97,97)
 #print(marks.count(97))  # output:3
 #print(marks.index(97))  # output:2  first index of 97


## Sets: {}, index does not exist in the sets, only unique values are stored into the sets
       # sets are unordered

marks = {95,93,97,97,97}
print(marks)
# output: {95,93,97}  , 97 will print only once because sets have unique values

marks = {95,93,97,97,97}
for score in marks:
    print(score)

# output: 95 93 97


## Dictionory: key-value pairs,

marks = {"english" : 95, "chemistry" : 98}

print(marks["chemistry"])  # output: 98
marks["physics"] = 90;
print(marks)               # {"english" : 95, "chemistry" : 98, "physics" : 90}

marks["physics"] = 99;
print(marks)               # {"english" : 95, "chemistry" : 98, "physics" : 99}


## Functions:
    # 1. In-build functions : e.g- int(), str(), bool()

    # 2. Module functions : when releted functions and related variales are stored in the same file that is called as a module
                          # import math
                          # print(dir(math))   - all thefunctions exist in math will print

                          # from math import sqrt
                          # print(sqrt(25))

                          # from math import *   - will import all the functions

    # 3. User-Defined functions: syntax
                          # def fuct_name (parameters):
                              # // do something
                          # function call()

                          e.g :
                            def print_sum (first, second):
                                print(first+second)

                            print_sum(1,3)   # output: 4



                            def print_sum (first, second=4):
                                print(first+second)

                            print_sum(1)   # output: 5






