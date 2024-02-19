def outer():
    name = "Dharani"
    
    def inner():
        nonlocal name
        print(name)
        name = "Gowtham"
        
    inner()
    print(name)
    

outer()
