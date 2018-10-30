def funcMax (a,b):
    if a < b:
        return b
    else:
        return a

def funcMin (a,b):
    if a > b:
        return b
    else:
        return a
    
    

c = funcMax(6,95)
print('max',c)
c = funcMin(8,6)
print('min',c)

b = generator = [ i for i in range(1,100) if i % 6 == 0 ]
a = generator = ( i for i in range(1,100) if i % 6 == 0 ) 
print(b)
print(a) 



