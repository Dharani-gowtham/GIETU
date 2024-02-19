#Python program to demonstrate the use of the yield keyword with the generator function.     
# A generator function's definition    
def generator_func():    
    yield "Yield"    
    yield "Keyword"    
    yield "in"    
    yield "Python"    
    yield "Python"    
    
    
# constructing a generator object and calling the generator function    
generator_object = generator_func()    
# print( type(generator_object) ) # printing the generator object's type    
for i in generator_object:    
    print(i)    

def outer():
    name = []
    def add():
        nonlocal name
        name.append(10)

    def sub():
        nonlocal name
        name.append(-2)
    
    
    print(name)
    add()
    sub()
    print(name)
    
outer()