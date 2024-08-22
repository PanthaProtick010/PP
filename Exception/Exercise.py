class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class AdultException(Exception):
    def __init__(self, msg):
        self.msg=msg
    def printMessage(self):
        print("Exception Error:",self.msg)

def ageCheck(age):
    if age<18:
        return age
    else:
        raise AdultException("Adult")
    
def displayPerson(person):
    try:
        name=person.name
        age=ageCheck(person.age)
    except AdultException as e:
        age=person.age
        e.printMessage()
    finally:
        print(f"Name: {name}, Age: {age}")

if __name__=="__main__":
    p=Person("Pantha",32)
    displayPerson(p)