class FactorialException(Exception):
    def __init__(self, msg):
        self.msg=msg
    def printMessage(self):
        print("Factorial Error:",self.msg)

def decorator(func):
    def wrapper(*args,**kwargs):
        ans=None
        try:
            ans=func(*args,**kwargs)
        except FactorialException as e:
            e.printMessage()
        finally:
            return ans
    return wrapper

@decorator
def factorial(i):
    if isinstance(i,int) and i>=0:
        factor=1
        for d in range(1,i+1):
            factor*=d
        return factor
    else:
        raise FactorialException("Enter applicable value for factorial")
    
if __name__=="__main__":
    print(str(factorial(9)))