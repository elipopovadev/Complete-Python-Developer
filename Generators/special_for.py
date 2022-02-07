def special_for(iterable):
    iterator = iter(iterable) 
    
    while True:
        try:
           print(iterator) 
           print(next(iterator)* 2)
            
        except StopIteration:
            break
        
special_for([1,2,3])
