def sample():
    name = "Dharani"
    
    def sample2():
        nonlocal name
        print(name)
        name = "Tested"
        print(name)
        
    sample2()
    print(name)
    
sample()