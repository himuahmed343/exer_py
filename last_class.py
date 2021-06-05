# def print_name(name):
#     msz = 'Hi'

#     def print_details():
#         print(msz, name)

#     print_details()

# print_name(input())


#Defining a closer function

def print_name(name):
    msz = 'Hi'

    def print_details():
        print(msz, name)

    return print_details

# func_obj = print_name('Karim')
# func_obj()
# print(func_obj.__closure__[0].cell_contents)
# print(func_obj.__closure__[1].cell_contents)

# func2_obj = print_name('Rahim')
# func2_obj()






"""
========   Decoration   ========

"""

def print_msz(msz):
    print(msz)

# print_msz('Python')
# func_obj = print_msz
# func_obj('Django')





#================================================================


def number():
    return 10

def add_number(func):

    def add():
        res = func()
        output = res + 20
        print(output)
    	
    return add()

# add_number(number)
        

"""

from time import time

def timer(function):

    def count_time():
        start = time()
        function()
        end = time()
        print(end - start, 'second')
        return
    return count_time()


@timer
def add():
    print(10+10+10)

@timer
def lst():
    for item in [1, 2, 3, 4, 5, 6, 7]:
        print(item)
    
            

"""


#================================================================

def print_value(func):
    def return_add():
        result = func()
        return result
    
    return return_add


@print_value
def sub():
    a = 20
    b = 10
    return a - b

# print(sub())



#==============================


# def f():

#     def g():
#         print("I am g")
    
#     print("I am f")
#     g()
# f()        


        

#==============================

def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!" 
    return result

# print(temperature(28))



def factorial(n):
    """ calculates the factorial of n, 
        n should be an integer and n <= 0 """
    if n >= 0 and type(n) == int:    
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    else:
        print("Negative values doesn't exist")
    
# print(factorial(int(input("Please enter an integer number to check factorial: "))))


#================================================================


def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
    
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
          
# f(g)


def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
    
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
    print("func's real name is " + func.__name__) 

          
# f(g)



import math

def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res

# print(foo(math.sin))
# print(foo(math.cos))


class Maths:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        sum = self.x + self.y
        if sum >= 0:
            print(sum)
        else:
            pass
    
    def mul(self):
        print(self.x * self.y)
        

m1 = Maths(10, 20)
# m1.add()



#==============================

def f(x):
    def g(y):
        return y + x + 3 
    return g

nf1 = f(1)
nf2 = f(3)

# print(nf1(1))
# print(nf2(1))



#==============================


def greeting_func_gen(lang):
    def customized_greeting(name):
        if lang == "de":   # German
            phrase = "Guten Morgen "
        elif lang == "fr": # French
            phrase = "Bonjour "
        elif lang == "it": # Italian
            phrase = "Buongiorno "
        elif lang == "tr": # Turkish
            phrase = "Günaydın "
        elif lang == "gr": # Greek
            phrase = "Καλημερα "
        else:
            phrase = "Hi "
        return phrase + name + "!"
    return customized_greeting


# say_hi = greeting_func_gen("tr")
# print(say_hi("Gülay")) 



class Mathematical:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def add(self):
        res_add = self.number1 + self.number2
        return res_add
        
    def multiplication(self):
        res_mul = (self.number1*self.number2)
        return res_mul
    
    def condition(self):
        sum = self.number1*self.number2
        if sum <= 100:
            print(sum)
        else:
            print(self.add())
        
        

    
m1 = Mathematical(30,70)
# m1.condition()




#==============================

def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial
    
p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

# for x in range(-2, 2, 1):
#     print(x, p1(x), p2(x))









#==============================

# def our_decorator(func):
#     def function_wrapper(x):
#         print("Before calling " + func.__name__)
#         func(x)
#         print("After calling " + func.__name__)
#     return function_wrapper

# def foo(x):
#     print("Hi, foo has been called with " + str(x))

# print("We call foo before decoration:")
# foo("Hi")
    
# print("We now decorate foo with f:")
# foo = our_decorator(foo)

# print("We call foo after decoration:")
# # foo(42)







class Check:

    def __init__(self,number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def sum(self):
        res_sum = self.number1 + self.number2
        return res_sum
    
    def multi(self):
        res_multi = self.number1 * self.number2
        return res_multi
        
    def term(self):
        x = self.multi()
        if x <= 600:
            print(self.sum())
        
        else:
            print("Hello")
            
           
    
    
    # def term(self):
    #     multiplications = multi()
       
        

chk_obj = Check(30, 70)
# print(chk_obj.multi())
# print(chk_obj.sum())
# chk_obj.term()
            



#================================================================



# str = "pynative"
# # print(str)

# # modified_string = str[0::2]
# # print(modified_string)


# # iterate over string
# for index in range(len(str)):
#     # check if index is divisible by 2
#     if index % 2 == 0:
#         # print character at index
#         # print(str[index])









#==============================


class Str:

    def __init__(self, string):
        self.string = string
        
    def func(self):
        print(self.string)
    
    def modified_str1(self):
        for item in range(len(self.string)):
            if item % 2 == 0:
                print(self.string[item], end = "")

    
    def modified_str2(self):
        modify = self.string[::2]
        print(modify)        

        
                   

print_details = Str("pynative")
# print_details.func()
# print_details.modified_str1()
# print_details.modified_str2()







#==============================


class Test:

    def __init__(self, lst):
        self.lst = lst
    
    def chk_value(self):
        first_item = self.lst[0]
        last_item = self.lst[-1]
        if first_item == last_item:
            return True
        else:
            return False


# lst = input("list: ").split()
# print_test = Test(lst)
# print(print_test.chk_value())
    



#==============================



class  Test:
    def __init__(self, numLst):
        self.numLst = numLst
    #visible with 5
    def visibleEle(self):
        for item in self.numLst:
            if item % 5 != 0:
                print(item)
    
    def divisibleEle(self):
        for item in self.numLst:
            if item % 5 == 0:
                print(item)
        
numLst = [10, 22, 30, 33]
print_test = Test(numLst)
# print_test.visibleEle()
# print_test.divisibleEle()





#================================================================

# class Test():
#     def __init__(self, number):
#         self.number = number
    
#     def numPattern(self):
#         for item in range(self.number):
#             for i in range(item):
#                 print(item, end= ' ')
#             print('\n')
            
# print_test = Test(6)
# print_test.numPattern()      





#===================================

 
# n = int(input())
# num = 121
# rev = 0
 
# while(num > 0):
#     a = num % 10
#     rev = rev * 10 + a
#     num = num // 10

# if rev == num:
#     print("accepted")
# else:
#     print("Not accepted")
        
 
# print(rev)
 



def palindrome(number):
    rev = 0
    num = number
    while(num > 0):
        a = num % 10
        rev = rev * 10 + a
        num = num // 10
    return rev

# palin_func = palindrome(int(input("Enter A Palindrome Integer: ")))



def chk_palin():
    print(palin_func)
    # if palin_func == 121:
    #     print("Accepted")
    # else:
    #     print("Not accepted")

# chk_palin()



class Test:
    def __init__(self, number):
        self.number = number
    
    def palindrome(self):
        rev = 0
        num = self.number
        while(num > 0):
            a = num % 10
            rev = rev * 10 + a
            num = num // 10
        return rev
    
    def chk_palin(self):
        x = print_palin
        y = self.number
        
        if x == y:
            print("Accepted")
        
        else:
            print("Not Accepted")

            
# palin_test = Test(int(input("Enter integer: ")))
# print_palin = palin_test.palindrome()
# palin_test.chk_palin()





#==============================

def mergeList(list1, listTwo):
    print("First List ", list1)
    print("Second List ", list2)
    List3 = []
    
    for num in list1:
        if (num % 2 != 0):
            List3.append(num)
    for num in list2:
        if (num % 2 == 0):
            List3.append(num)
    return List3

list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

print("result List is", mergeList(list1, list2))













# str = 1234
# print(str[::-1])