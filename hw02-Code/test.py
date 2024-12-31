


def and_func(x,y):
    if(not x):
        return x
    else:
        return y
    


def shift(k,f):
    return lambda x: f(x+k) 
def shifter(k):
    def shifted(f):
        return shift(k,f)
    return shifted
def unshift(shifted):
    def funcg(g):
        
        def funcx(x):
            return shifted(shift(-2*(shifted(lambda x:x)(0))))(0,g)(x)    
        return funcx
    return  funcg
cubic=lambda x:x**3-5*x*x+1
k=4
f=cubic
x=2.0
print(unshift(shifter(k))(shifter(k)(f))(x))




# shift(-shifted(lambda x: x)(0), g) shifter(-shifted(lambda x: x)(0))(g)